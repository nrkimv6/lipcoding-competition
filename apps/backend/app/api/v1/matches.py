"""
매칭 관리 API 엔드포인트
"""
from typing import Annotated, List
from datetime import datetime, timezone
from fastapi import APIRouter, Depends, HTTPException, status, Query
from sqlalchemy.orm import Session, joinedload
from app.database import get_db
from app.models import User, Match, MatchStatus, UserRole
from app.schemas.match import MatchCreate, MatchResponse, MatchWithUsers, MatchUpdate
from app.dependencies import get_current_user, get_current_mentee, get_current_mentor

router = APIRouter()

@router.post("/request", response_model=MatchResponse, status_code=status.HTTP_201_CREATED)
async def create_match_request(
    match_data: MatchCreate,
    current_user: Annotated[User, Depends(get_current_mentee)],
    db: Annotated[Session, Depends(get_db)]
):
    """매칭 요청 생성 (멘티만 가능)"""
    
    # 멘토 존재 확인
    mentor = db.query(User).filter(
        User.id == match_data.mentor_id,
        User.role == UserRole.MENTOR,
        User.is_active == True
    ).first()
    
    if not mentor:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="멘토를 찾을 수 없습니다"
        )
    
    # 중복 요청 확인 (이미 진행 중인 요청이 있는지)
    existing_match = db.query(Match).filter(
        Match.mentor_id == match_data.mentor_id,
        Match.mentee_id == current_user.id,
        Match.status.in_([MatchStatus.PENDING, MatchStatus.ACCEPTED])
    ).first()
    
    if existing_match:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="이미 이 멘토에게 진행 중인 요청이 있습니다"
        )
    
    # 새 매칭 요청 생성
    new_match = Match(
        mentor_id=match_data.mentor_id,
        mentee_id=current_user.id,
        message=match_data.message,
        status=MatchStatus.PENDING
    )
    
    db.add(new_match)
    db.commit()
    db.refresh(new_match)
    
    return new_match

@router.get("/sent", response_model=List[MatchWithUsers])
async def get_sent_requests(
    current_user: Annotated[User, Depends(get_current_mentee)],
    db: Annotated[Session, Depends(get_db)]
):
    """내가 보낸 매칭 요청 목록"""
    
    matches = db.query(Match).filter(
        Match.mentee_id == current_user.id
    ).options(
        joinedload(Match.mentor),
        joinedload(Match.mentee)
    ).all()
    
    return matches

@router.get("/received", response_model=List[MatchWithUsers])
async def get_received_requests(
    current_user: Annotated[User, Depends(get_current_mentor)],
    db: Annotated[Session, Depends(get_db)]
):
    """내가 받은 매칭 요청 목록"""
    
    matches = db.query(Match).filter(
        Match.mentor_id == current_user.id
    ).options(
        joinedload(Match.mentor),
        joinedload(Match.mentee)
    ).all()
    
    return matches

@router.put("/{match_id}/accept", response_model=MatchResponse)
async def accept_match(
    match_id: int,
    update_data: MatchUpdate,
    current_user: Annotated[User, Depends(get_current_mentor)],
    db: Annotated[Session, Depends(get_db)]
):
    """매칭 요청 수락 (멘토만 가능)"""
    
    # 매칭 요청 조회
    match = db.query(Match).filter(
        Match.id == match_id,
        Match.mentor_id == current_user.id,
        Match.status == MatchStatus.PENDING
    ).first()
    
    if not match:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="매칭 요청을 찾을 수 없거나 이미 처리되었습니다"
        )
    
    # 매칭 수락
    match.status = MatchStatus.ACCEPTED
    match.response_message = update_data.response_message
    match.matched_at = datetime.now(timezone.utc)
    
    db.commit()
    db.refresh(match)
    
    return match

@router.put("/{match_id}/reject", response_model=MatchResponse)
async def reject_match(
    match_id: int,
    update_data: MatchUpdate,
    current_user: Annotated[User, Depends(get_current_mentor)],
    db: Annotated[Session, Depends(get_db)]
):
    """매칭 요청 거절 (멘토만 가능)"""
    
    # 매칭 요청 조회
    match = db.query(Match).filter(
        Match.id == match_id,
        Match.mentor_id == current_user.id,
        Match.status == MatchStatus.PENDING
    ).first()
    
    if not match:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="매칭 요청을 찾을 수 없거나 이미 처리되었습니다"
        )
    
    # 매칭 거절
    match.status = MatchStatus.REJECTED
    match.response_message = update_data.response_message
    
    db.commit()
    db.refresh(match)
    
    return match

@router.get("/current", response_model=MatchWithUsers)
async def get_current_match(
    current_user: Annotated[User, Depends(get_current_user)],
    db: Annotated[Session, Depends(get_db)]
):
    """현재 활성 매칭 조회"""
    
    # 사용자 역할에 따라 다른 조건 적용
    if current_user.role == UserRole.MENTOR:
        match = db.query(Match).filter(
            Match.mentor_id == current_user.id,
            Match.status == MatchStatus.ACCEPTED
        ).options(
            joinedload(Match.mentor),
            joinedload(Match.mentee)
        ).first()
    else:  # MENTEE
        match = db.query(Match).filter(
            Match.mentee_id == current_user.id,
            Match.status == MatchStatus.ACCEPTED
        ).options(
            joinedload(Match.mentor),
            joinedload(Match.mentee)
        ).first()
    
    if not match:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="현재 활성 매칭이 없습니다"
        )
    
    return match
async def get_mentee_matches():
    """멘티의 매칭 요청 목록"""
    return {"message": "멘티 매칭 목록 조회 기능이 구현될 예정입니다"}

@router.get("/mentor")
async def get_mentor_matches():
    """멘토의 매칭 요청 목록"""
    return {"message": "멘토 매칭 목록 조회 기능이 구현될 예정입니다"}

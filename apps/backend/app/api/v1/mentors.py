"""
멘토 관리 API 엔드포인트
"""
from typing import Annotated, List, Optional
from fastapi import APIRouter, Depends, HTTPException, status, Query
from sqlalchemy.orm import Session, joinedload
from app.database import get_db
from app.models import User, MentorProfile, UserRole
from app.schemas.mentor import MentorProfileCreate, MentorProfileUpdate, MentorProfileResponse
from app.schemas.user import UserResponse
from app.dependencies import get_current_user, get_current_mentor

router = APIRouter()

@router.get("/", response_model=List[UserResponse])
async def get_mentors(
    db: Annotated[Session, Depends(get_db)],
    skip: int = Query(0, ge=0, description="건너뛸 항목 수"),
    limit: int = Query(10, ge=1, le=100, description="반환할 항목 수"),
    skills: Optional[str] = Query(None, description="기술 스택 필터 (쉼표로 구분)"),
    min_experience: Optional[int] = Query(None, ge=0, description="최소 경력 년수")
):
    """멘토 목록 조회 (필터링 및 페이징)"""
    
    # 기본 쿼리: 멘토 역할을 가진 활성 사용자
    query = db.query(User).filter(
        User.role == UserRole.MENTOR,
        User.is_active == True
    ).options(joinedload(User.mentor_profile))
    
    # 기술 스택 필터링
    if skills:
        skill_list = [skill.strip() for skill in skills.split(",")]
        for skill in skill_list:
            query = query.filter(User.skills.any(skill))
    
    # 경력 필터링 (멘토 프로필이 있는 경우)
    if min_experience is not None:
        query = query.join(MentorProfile).filter(
            MentorProfile.experience_years >= min_experience
        )
    
    # 페이징 적용
    mentors = query.offset(skip).limit(limit).all()
    
    return mentors

@router.get("/{mentor_id}", response_model=UserResponse)
async def get_mentor_by_id(
    mentor_id: int,
    db: Annotated[Session, Depends(get_db)]
):
    """특정 멘토 상세 정보 조회"""
    
    mentor = db.query(User).filter(
        User.id == mentor_id,
        User.role == UserRole.MENTOR,
        User.is_active == True
    ).options(joinedload(User.mentor_profile)).first()
    
    if not mentor:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="멘토를 찾을 수 없습니다"
        )
    
    return mentor

@router.post("/profile", response_model=MentorProfileResponse, status_code=status.HTTP_201_CREATED)
async def create_mentor_profile(
    profile_data: MentorProfileCreate,
    current_user: Annotated[User, Depends(get_current_mentor)],
    db: Annotated[Session, Depends(get_db)]
):
    """멘토 프로필 생성"""
    
    # 이미 프로필이 있는지 확인
    existing_profile = db.query(MentorProfile).filter(
        MentorProfile.user_id == current_user.id
    ).first()
    
    if existing_profile:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="이미 멘토 프로필이 존재합니다"
        )
    
    # 새 프로필 생성
    new_profile = MentorProfile(
        user_id=current_user.id,
        experience_years=profile_data.experience_years,
        expertise_areas=profile_data.expertise_areas,
        availability=profile_data.availability,
        max_mentees=profile_data.max_mentees
    )
    
    db.add(new_profile)
    db.commit()
    db.refresh(new_profile)
    
    return new_profile

@router.put("/profile", response_model=MentorProfileResponse)
async def update_mentor_profile(
    profile_data: MentorProfileUpdate,
    current_user: Annotated[User, Depends(get_current_mentor)],
    db: Annotated[Session, Depends(get_db)]
):
    """멘토 프로필 수정"""
    
    # 기존 프로필 조회
    profile = db.query(MentorProfile).filter(
        MentorProfile.user_id == current_user.id
    ).first()
    
    if not profile:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="멘토 프로필을 찾을 수 없습니다. 먼저 프로필을 생성해주세요."
        )
    
    # 업데이트할 필드만 수정
    if profile_data.experience_years is not None:
        profile.experience_years = profile_data.experience_years
    if profile_data.expertise_areas is not None:
        profile.expertise_areas = profile_data.expertise_areas
    if profile_data.availability is not None:
        profile.availability = profile_data.availability
    if profile_data.max_mentees is not None:
        profile.max_mentees = profile_data.max_mentees
    
    db.commit()
    db.refresh(profile)
    
    return profile

@router.get("/profile/me", response_model=MentorProfileResponse)
async def get_my_mentor_profile(
    current_user: Annotated[User, Depends(get_current_mentor)],
    db: Annotated[Session, Depends(get_db)]
):
    """내 멘토 프로필 조회"""
    
    profile = db.query(MentorProfile).filter(
        MentorProfile.user_id == current_user.id
    ).first()
    
    if not profile:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="멘토 프로필을 찾을 수 없습니다"
        )
    
    return profile

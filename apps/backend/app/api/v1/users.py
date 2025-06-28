"""
사용자 관리 API 엔드포인트
"""
from typing import Annotated
from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from app.database import get_db
from app.models import User
from app.schemas.user import UserResponse, UserUpdate
from app.dependencies import get_current_user

router = APIRouter()

@router.get("/profile", response_model=UserResponse)
async def get_my_profile(
    current_user: Annotated[User, Depends(get_current_user)]
):
    """현재 사용자 프로필 조회"""
    return current_user

@router.put("/profile", response_model=UserResponse)
async def update_my_profile(
    profile_data: UserUpdate,
    current_user: Annotated[User, Depends(get_current_user)],
    db: Annotated[Session, Depends(get_db)]
):
    """현재 사용자 프로필 수정"""
    
    # 업데이트할 필드만 수정
    if profile_data.name is not None:
        current_user.name = profile_data.name
    if profile_data.bio is not None:
        current_user.bio = profile_data.bio
    if profile_data.skills is not None:
        current_user.skills = profile_data.skills
    if profile_data.interests is not None:
        current_user.interests = profile_data.interests
    
    db.commit()
    db.refresh(current_user)
    
    return current_user

@router.get("/{user_id}", response_model=UserResponse)
async def get_user_by_id(
    user_id: int,
    db: Annotated[Session, Depends(get_db)]
):
    """특정 사용자 정보 조회 (공개 정보만)"""
    
    user = db.query(User).filter(User.id == user_id, User.is_active == True).first()
    if not user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="사용자를 찾을 수 없습니다"
        )
    
    return user

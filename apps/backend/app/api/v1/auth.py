"""
인증 관련 API 엔드포인트
"""
from typing import Annotated
from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from app.database import get_db
from app.models import User, UserRole
from app.schemas.auth import LoginRequest, RegisterRequest, Token
from app.schemas.user import UserResponse
from app.utils.auth import verify_password, get_password_hash, create_access_token
from app.dependencies import get_current_user

router = APIRouter()

@router.post("/register", response_model=UserResponse, status_code=status.HTTP_201_CREATED)
async def register(
    user_data: RegisterRequest,
    db: Annotated[Session, Depends(get_db)]
):
    """사용자 회원가입"""
    
    # 이메일 중복 확인
    existing_user = db.query(User).filter(User.email == user_data.email).first()
    if existing_user:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="이미 등록된 이메일입니다"
        )
    
    # 역할 검증
    if user_data.role not in [UserRole.MENTOR, UserRole.MENTEE]:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="역할은 'mentor' 또는 'mentee'만 가능합니다"
        )
    
    # 비밀번호 해싱
    hashed_password = get_password_hash(user_data.password)
    
    # 새 사용자 생성
    new_user = User(
        email=user_data.email,
        name=user_data.name,
        password_hash=hashed_password,
        role=UserRole(user_data.role),
        bio=user_data.bio,
        skills=user_data.skills or [],
        interests=user_data.interests or []
    )
    
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    
    return new_user

@router.post("/login", response_model=Token)
async def login(
    login_data: LoginRequest,
    db: Annotated[Session, Depends(get_db)]
):
    """사용자 로그인"""
    
    # 사용자 조회
    user = db.query(User).filter(User.email == login_data.email).first()
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="이메일 또는 비밀번호가 올바르지 않습니다",
            headers={"WWW-Authenticate": "Bearer"},
        )
    
    # 비밀번호 검증
    if not verify_password(login_data.password, user.password_hash):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="이메일 또는 비밀번호가 올바르지 않습니다",
            headers={"WWW-Authenticate": "Bearer"},
        )
    
    # 활성 사용자 확인
    if not user.is_active:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="비활성화된 계정입니다"
        )
    
    # JWT 토큰 생성
    access_token = create_access_token(data={"sub": str(user.id)})
    
    return {"access_token": access_token, "token_type": "bearer"}

@router.get("/me", response_model=UserResponse)
async def get_current_user_info(
    current_user: Annotated[User, Depends(get_current_user)]
):
    """현재 로그인한 사용자 정보 조회"""
    return current_user

@router.post("/logout")
async def logout():
    """사용자 로그아웃 (클라이언트에서 토큰 삭제)"""
    return {"message": "성공적으로 로그아웃되었습니다"}

# 테스트 호환을 위한 signup 엔드포인트 (register와 동일)
@router.post("/signup", response_model=UserResponse, status_code=status.HTTP_201_CREATED)
async def signup(
    user_data: RegisterRequest,
    db: Annotated[Session, Depends(get_db)]
):
    """사용자 회원가입 (테스트 호환용)"""
    return await register(user_data, db)

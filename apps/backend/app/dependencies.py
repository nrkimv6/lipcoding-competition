"""
FastAPI 의존성 함수들
"""
from typing import Annotated
from fastapi import Depends, HTTPException, status
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from sqlalchemy.orm import Session
from app.database import get_db
from app.models import User
from app.utils.auth import verify_token

# HTTP Bearer 토큰 스키마
security = HTTPBearer()

def get_current_user(
    credentials: Annotated[HTTPAuthorizationCredentials, Depends(security)],
    db: Annotated[Session, Depends(get_db)]
) -> User:
    """현재 로그인한 사용자 정보 반환"""
    
    # 토큰 검증
    payload = verify_token(credentials.credentials)
    
    # 사용자 ID 추출
    user_id: int = payload.get("sub")
    if user_id is None:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="토큰에서 사용자 정보를 찾을 수 없습니다",
            headers={"WWW-Authenticate": "Bearer"},
        )
    
    # 데이터베이스에서 사용자 조회
    user = db.query(User).filter(User.id == user_id).first()
    if user is None:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="사용자를 찾을 수 없습니다",
            headers={"WWW-Authenticate": "Bearer"},
        )
    
    # 활성 사용자 확인
    if not user.is_active:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="비활성화된 사용자입니다"
        )
    
    return user

def get_current_active_user(
    current_user: Annotated[User, Depends(get_current_user)]
) -> User:
    """현재 활성 사용자 (별칭)"""
    return current_user

def get_current_mentor(
    current_user: Annotated[User, Depends(get_current_user)]
) -> User:
    """현재 멘토 사용자"""
    if current_user.role != "mentor":
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="멘토 권한이 필요합니다"
        )
    return current_user

def get_current_mentee(
    current_user: Annotated[User, Depends(get_current_user)]
) -> User:
    """현재 멘티 사용자"""
    if current_user.role != "mentee":
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="멘티 권한이 필요합니다"
        )
    return current_user

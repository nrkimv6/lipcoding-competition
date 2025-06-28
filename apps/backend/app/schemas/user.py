"""
사용자 관련 스키마
"""
from pydantic import BaseModel
from typing import Optional, List
from datetime import datetime
from app.schemas.common import UserRole

class UserBase(BaseModel):
    """사용자 기본 스키마"""
    email: str
    name: str
    role: UserRole
    bio: Optional[str] = None
    skills: List[str] = []
    interests: List[str] = []

class UserCreate(UserBase):
    """사용자 생성 스키마"""
    password: str

class UserUpdate(BaseModel):
    """사용자 업데이트 스키마"""
    name: Optional[str] = None
    bio: Optional[str] = None
    skills: Optional[List[str]] = None
    interests: Optional[List[str]] = None

class User(UserBase):
    """사용자 응답 스키마"""
    id: int
    created_at: datetime
    is_active: bool = True

    class Config:
        from_attributes = True

class UserLogin(BaseModel):
    """로그인 스키마"""
    email: str
    password: str

class Token(BaseModel):
    """토큰 스키마"""
    access_token: str
    token_type: str

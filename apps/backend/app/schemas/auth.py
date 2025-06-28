"""
인증 관련 스키마
"""
from pydantic import BaseModel, EmailStr

class Token(BaseModel):
    """토큰 응답"""
    access_token: str
    token_type: str = "bearer"

class TokenData(BaseModel):
    """토큰 데이터"""
    user_id: int | None = None

class LoginRequest(BaseModel):
    """로그인 요청"""
    email: EmailStr
    password: str

class RegisterRequest(BaseModel):
    """회원가입 요청"""
    email: EmailStr
    password: str
    name: str
    role: str  # "mentor" 또는 "mentee"
    bio: str | None = None
    skills: list[str] | None = None
    interests: list[str] | None = None

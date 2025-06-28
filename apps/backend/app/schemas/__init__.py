"""
Pydantic 스키마 모델
"""
from app.schemas.common import UserRole, MatchStatus, BaseSchema, TimestampSchema
from app.schemas.auth import Token, TokenData, LoginRequest, RegisterRequest
from app.schemas.user import UserBase, UserCreate, UserUpdate, UserResponse, UserLogin
from app.schemas.mentor import (
    MentorProfileBase, MentorProfileCreate, MentorProfileUpdate, MentorProfileResponse,
    MenteeProfileBase, MenteeProfileCreate, MenteeProfileUpdate, MenteeProfileResponse
)
from app.schemas.match import MatchBase, MatchCreate, MatchResponse, MatchWithUsers, MatchUpdate, MatchListResponse

__all__ = [
    # Common
    "UserRole", "MatchStatus", "BaseSchema", "TimestampSchema",
    
    # Auth
    "Token", "TokenData", "LoginRequest", "RegisterRequest",
    
    # User
    "UserBase", "UserCreate", "UserUpdate", "UserResponse", "UserLogin",
    
    # Mentor/Mentee
    "MentorProfileBase", "MentorProfileCreate", "MentorProfileUpdate", "MentorProfileResponse",
    "MenteeProfileBase", "MenteeProfileCreate", "MenteeProfileUpdate", "MenteeProfileResponse",
    
    # Match
    "MatchBase", "MatchCreate", "MatchResponse", "MatchWithUsers", "MatchUpdate", "MatchListResponse"
]

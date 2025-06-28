"""
멘토 관련 스키마
"""
from pydantic import BaseModel
from typing import Optional, List
from app.schemas.common import TimestampSchema

class MentorProfileBase(BaseModel):
    """멘토 프로필 기본 스키마"""
    experience_years: int = 0
    expertise_areas: List[str] = []
    availability: Optional[str] = None
    max_mentees: int = 3

class MentorProfileCreate(MentorProfileBase):
    """멘토 프로필 생성 스키마"""
    pass

class MentorProfileUpdate(BaseModel):
    """멘토 프로필 업데이트 스키마"""
    experience_years: Optional[int] = None
    expertise_areas: Optional[List[str]] = None
    availability: Optional[str] = None
    max_mentees: Optional[int] = None

class MentorProfileResponse(MentorProfileBase, TimestampSchema):
    """멘토 프로필 응답 스키마"""
    id: int
    user_id: int

class MenteeProfileBase(BaseModel):
    """멘티 프로필 기본 스키마"""
    learning_goals: Optional[str] = None
    preferred_mentor_experience: Optional[int] = None

class MenteeProfileCreate(MenteeProfileBase):
    """멘티 프로필 생성 스키마"""
    pass

class MenteeProfileUpdate(BaseModel):
    """멘티 프로필 업데이트 스키마"""
    learning_goals: Optional[str] = None
    preferred_mentor_experience: Optional[int] = None

class MenteeProfileResponse(MenteeProfileBase, TimestampSchema):
    """멘티 프로필 응답 스키마"""
    id: int
    user_id: int

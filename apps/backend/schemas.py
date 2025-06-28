from pydantic import BaseModel
from typing import Optional, List
from datetime import datetime
from enum import Enum

class UserRole(str, Enum):
    MENTOR = "mentor"
    MENTEE = "mentee"
    ADMIN = "admin"

class MatchingStatus(str, Enum):
    PENDING = "pending"
    ACCEPTED = "accepted"
    REJECTED = "rejected"
    COMPLETED = "completed"

class UserBase(BaseModel):
    email: str
    name: str
    role: UserRole
    bio: Optional[str] = None
    skills: List[str] = []
    interests: List[str] = []

class UserCreate(UserBase):
    password: str

class User(UserBase):
    id: int
    created_at: datetime
    is_active: bool = True

    class Config:
        from_attributes = True

class MentorProfile(BaseModel):
    id: int
    user_id: int
    experience_years: int
    expertise_areas: List[str] = []
    availability: str
    max_mentees: int = 3

class MenteeProfile(BaseModel):
    id: int
    user_id: int
    learning_goals: List[str] = []
    current_level: str
    preferred_mentor_type: Optional[str] = None

class MatchingRequest(BaseModel):
    mentee_id: int
    mentor_id: int
    message: Optional[str] = None

class Matching(BaseModel):
    id: int
    mentor_id: int
    mentee_id: int
    status: MatchingStatus
    created_at: datetime
    updated_at: datetime
    message: Optional[str] = None

    class Config:
        from_attributes = True

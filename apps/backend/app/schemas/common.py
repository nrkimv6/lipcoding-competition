"""
공통 스키마 정의
"""
from enum import Enum
from pydantic import BaseModel
from datetime import datetime

class UserRole(str, Enum):
    """사용자 역할"""
    MENTOR = "mentor"
    MENTEE = "mentee"
    ADMIN = "admin"

class MatchStatus(str, Enum):
    """매칭 상태"""
    PENDING = "pending"
    ACCEPTED = "accepted"
    REJECTED = "rejected"
    CANCELLED = "cancelled"
    COMPLETED = "completed"

class BaseSchema(BaseModel):
    """기본 스키마 (ORM 모드 활성화)"""
    class Config:
        from_attributes = True

class TimestampSchema(BaseSchema):
    """타임스탬프가 포함된 기본 스키마"""
    created_at: datetime
    updated_at: datetime

"""
공통 스키마 정의
"""
from enum import Enum

class UserRole(str, Enum):
    """사용자 역할"""
    MENTOR = "mentor"
    MENTEE = "mentee"
    ADMIN = "admin"

class MatchingStatus(str, Enum):
    """매칭 상태"""
    PENDING = "pending"
    ACCEPTED = "accepted"
    REJECTED = "rejected"
    COMPLETED = "completed"

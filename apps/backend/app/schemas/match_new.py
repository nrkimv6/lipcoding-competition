"""
매칭 관련 스키마
"""
from pydantic import BaseModel
from typing import Optional, List
from datetime import datetime
from app.schemas.common import MatchStatus, TimestampSchema
from app.schemas.user import UserResponse

class MatchBase(BaseModel):
    """매칭 기본 스키마"""
    mentor_id: int
    message: Optional[str] = None

class MatchCreate(MatchBase):
    """매칭 요청 생성 스키마"""
    pass

class MatchResponse(MatchBase, TimestampSchema):
    """매칭 응답 스키마"""
    id: int
    mentee_id: int
    status: MatchStatus
    response_message: Optional[str] = None
    matched_at: Optional[datetime] = None

class MatchWithUsers(MatchResponse):
    """사용자 정보가 포함된 매칭 응답"""
    mentor: UserResponse
    mentee: UserResponse

class MatchUpdate(BaseModel):
    """매칭 상태 업데이트 스키마"""
    status: MatchStatus
    response_message: Optional[str] = None

class MatchListResponse(BaseModel):
    """매칭 목록 응답 스키마"""
    matches: List[MatchWithUsers]
    total: int

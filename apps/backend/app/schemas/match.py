"""
매칭 관련 스키마
"""
from pydantic import BaseModel
from typing import Optional
from datetime import datetime
from app.schemas.common import MatchingStatus

class MatchingRequestBase(BaseModel):
    """매칭 요청 기본 스키마"""
    mentor_id: int
    message: Optional[str] = None

class MatchingRequestCreate(MatchingRequestBase):
    """매칭 요청 생성 스키마"""
    pass

class MatchingRequest(MatchingRequestBase):
    """매칭 요청 응답 스키마"""
    id: int
    mentee_id: int
    status: MatchingStatus
    created_at: datetime
    updated_at: datetime

    class Config:
        from_attributes = True

class MatchingUpdate(BaseModel):
    """매칭 상태 업데이트 스키마"""
    status: MatchingStatus
    message: Optional[str] = None

class Matching(BaseModel):
    """매칭 응답 스키마"""
    id: int
    mentor_id: int
    mentee_id: int
    status: MatchingStatus
    created_at: datetime
    updated_at: datetime
    message: Optional[str] = None

    class Config:
        from_attributes = True

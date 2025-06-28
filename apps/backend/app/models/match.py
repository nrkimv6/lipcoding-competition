"""
매칭 관련 SQLAlchemy 모델
"""
from sqlalchemy import Integer, String, Text, ForeignKey, DateTime
from sqlalchemy.orm import Mapped, mapped_column, relationship
from enum import Enum
from datetime import datetime

from app.models.base import Base, TimestampMixin

class MatchStatus(str, Enum):
    """매칭 상태"""
    PENDING = "pending"      # 대기 중
    ACCEPTED = "accepted"    # 수락됨
    REJECTED = "rejected"    # 거절됨
    CANCELLED = "cancelled"  # 취소됨
    COMPLETED = "completed"  # 완료됨

class Match(Base, TimestampMixin):
    """매칭 모델"""
    __tablename__ = "matches"
    
    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)
    mentor_id: Mapped[int] = mapped_column(
        Integer,
        ForeignKey("users.id", ondelete="CASCADE"),
        nullable=False
    )
    mentee_id: Mapped[int] = mapped_column(
        Integer, 
        ForeignKey("users.id", ondelete="CASCADE"),
        nullable=False
    )
    status: Mapped[MatchStatus] = mapped_column(String(20), default=MatchStatus.PENDING, nullable=False)
    message: Mapped[str | None] = mapped_column(Text, nullable=True)  # 매칭 요청 메시지
    response_message: Mapped[str | None] = mapped_column(Text, nullable=True)  # 멘토의 응답 메시지
    matched_at: Mapped[datetime | None] = mapped_column(DateTime(timezone=True), nullable=True)  # 매칭 성사 시간
    
    # 관계 설정
    mentor: Mapped["User"] = relationship(
        "User",
        foreign_keys=[mentor_id],
        back_populates="received_match_requests"
    )
    mentee: Mapped["User"] = relationship(
        "User", 
        foreign_keys=[mentee_id],
        back_populates="sent_match_requests"
    )
    
    def __repr__(self):
        return f"<Match(id={self.id}, mentor_id={self.mentor_id}, mentee_id={self.mentee_id}, status='{self.status}')>"

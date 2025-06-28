"""
사용자 관련 SQLAlchemy 모델
"""
from sqlalchemy import Boolean, Integer, String, Text, ARRAY
from sqlalchemy.orm import Mapped, mapped_column, relationship
from enum import Enum

from app.models.base import Base, TimestampMixin

class UserRole(str, Enum):
    """사용자 역할"""
    MENTOR = "mentor"
    MENTEE = "mentee"
    ADMIN = "admin"

class User(Base, TimestampMixin):
    """사용자 모델"""
    __tablename__ = "users"
    
    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)
    email: Mapped[str] = mapped_column(String(255), unique=True, index=True, nullable=False)
    name: Mapped[str] = mapped_column(String(100), nullable=False)
    password_hash: Mapped[str] = mapped_column(String(255), nullable=False)
    role: Mapped[UserRole] = mapped_column(String(20), nullable=False)
    bio: Mapped[str | None] = mapped_column(Text, nullable=True)
    skills: Mapped[list[str] | None] = mapped_column(ARRAY(String), nullable=True)
    interests: Mapped[list[str] | None] = mapped_column(ARRAY(String), nullable=True)
    is_active: Mapped[bool] = mapped_column(Boolean, default=True, nullable=False)
    
    # 관계 설정
    mentor_profile: Mapped["MentorProfile"] = relationship(
        "MentorProfile", 
        back_populates="user",
        uselist=False
    )
    mentee_profile: Mapped["MenteeProfile"] = relationship(
        "MenteeProfile",
        back_populates="user", 
        uselist=False
    )
    
    # 매칭 관계 (멘티로서 보낸 요청)
    sent_match_requests: Mapped[list["Match"]] = relationship(
        "Match",
        foreign_keys="Match.mentee_id",
        back_populates="mentee"
    )
    
    # 매칭 관계 (멘토로서 받은 요청)
    received_match_requests: Mapped[list["Match"]] = relationship(
        "Match", 
        foreign_keys="Match.mentor_id",
        back_populates="mentor"
    )
    
    def __repr__(self):
        return f"<User(id={self.id}, email='{self.email}', role='{self.role}')>"

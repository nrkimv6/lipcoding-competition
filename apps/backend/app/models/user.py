"""
사용자 관련 SQLAlchemy 모델
"""
from sqlalchemy import Boolean, Integer, String, Text, Column, Enum as SQLEnum
from sqlalchemy.orm import relationship
from enum import Enum

from app.database import Base
from app.models.base import TimestampMixin

class UserRole(str, Enum):
    """사용자 역할"""
    MENTOR = "mentor"
    MENTEE = "mentee"
    ADMIN = "admin"

class User(Base, TimestampMixin):
    """사용자 모델"""
    __tablename__ = "users"
    
    id = Column(Integer, primary_key=True, index=True)
    email = Column(String(255), unique=True, index=True, nullable=False)
    name = Column(String(100), nullable=False)
    password_hash = Column(String(255), nullable=False)
    role = Column(SQLEnum(UserRole), nullable=False)
    bio = Column(Text, nullable=True)
    skills = Column(Text, nullable=True)  # JSON string으로 저장
    interests = Column(Text, nullable=True)  # JSON string으로 저장
    is_active = Column(Boolean, default=True, nullable=False)
    
    # 관계 설정
    mentor_profile = relationship(
        "MentorProfile", 
        back_populates="user",
        uselist=False
    )
    mentee_profile = relationship(
        "MenteeProfile",
        back_populates="user", 
        uselist=False
    )
    
    # 매칭 관계 (멘티로서 보낸 요청)
    sent_match_requests = relationship(
        "Match",
        foreign_keys="Match.mentee_id",
        back_populates="mentee"
    )
    
    # 매칭 관계 (멘토로서 받은 요청)
    received_match_requests = relationship(
        "Match", 
        foreign_keys="Match.mentor_id",
        back_populates="mentor"
    )
    
    def __repr__(self):
        return f"<User(id={self.id}, email='{self.email}', role='{self.role}')>"

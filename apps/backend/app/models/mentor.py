"""
멘토 관련 SQLAlchemy 모델
"""
from sqlalchemy import Integer, String, Text, Column, ForeignKey
from sqlalchemy.orm import relationship

from app.database import Base
from app.models.base import TimestampMixin

class MentorProfile(Base, TimestampMixin):
    """멘토 프로필 모델"""
    __tablename__ = "mentor_profiles"
    
    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(
        Integer, 
        ForeignKey("users.id", ondelete="CASCADE"),
        unique=True,
        nullable=False
    )
    experience_years = Column(Integer, default=0, nullable=False)
    expertise_areas = Column(Text, nullable=True)  # JSON string으로 저장
    availability = Column(Text, nullable=True)
    max_mentees = Column(Integer, default=3, nullable=False)
    
    # 관계 설정
    user = relationship("User", back_populates="mentor_profile")
    
    def __repr__(self):
        return f"<MentorProfile(id={self.id}, user_id={self.user_id}, experience_years={self.experience_years})>"

class MenteeProfile(Base, TimestampMixin):
    """멘티 프로필 모델"""
    __tablename__ = "mentee_profiles"
    
    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(
        Integer,
        ForeignKey("users.id", ondelete="CASCADE"),
        unique=True,
        nullable=False
    )
    learning_goals = Column(Text, nullable=True)
    preferred_mentor_experience = Column(Integer, nullable=True)
    
    # 관계 설정
    user = relationship("User", back_populates="mentee_profile")
    
    def __repr__(self):
        return f"<MenteeProfile(id={self.id}, user_id={self.user_id})>"

"""
멘토 관련 SQLAlchemy 모델
"""
from sqlalchemy import Integer, String, Text, ARRAY, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.models.base import Base, TimestampMixin

class MentorProfile(Base, TimestampMixin):
    """멘토 프로필 모델"""
    __tablename__ = "mentor_profiles"
    
    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)
    user_id: Mapped[int] = mapped_column(
        Integer, 
        ForeignKey("users.id", ondelete="CASCADE"),
        unique=True,
        nullable=False
    )
    experience_years: Mapped[int] = mapped_column(Integer, default=0, nullable=False)
    expertise_areas: Mapped[list[str] | None] = mapped_column(ARRAY(String), nullable=True)
    availability: Mapped[str | None] = mapped_column(Text, nullable=True)
    max_mentees: Mapped[int] = mapped_column(Integer, default=3, nullable=False)
    
    # 관계 설정
    user: Mapped["User"] = relationship("User", back_populates="mentor_profile")
    
    def __repr__(self):
        return f"<MentorProfile(id={self.id}, user_id={self.user_id}, experience_years={self.experience_years})>"

class MenteeProfile(Base, TimestampMixin):
    """멘티 프로필 모델"""
    __tablename__ = "mentee_profiles"
    
    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)
    user_id: Mapped[int] = mapped_column(
        Integer,
        ForeignKey("users.id", ondelete="CASCADE"),
        unique=True,
        nullable=False
    )
    learning_goals: Mapped[str | None] = mapped_column(Text, nullable=True)
    preferred_mentor_experience: Mapped[int | None] = mapped_column(Integer, nullable=True)
    
    # 관계 설정
    user: Mapped["User"] = relationship("User", back_populates="mentee_profile")
    
    def __repr__(self):
        return f"<MenteeProfile(id={self.id}, user_id={self.user_id})>"

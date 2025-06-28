"""
SQLAlchemy Base 클래스 및 공통 필드
"""
from sqlalchemy import Column, DateTime, func
from datetime import datetime

class TimestampMixin:
    """생성일/수정일 자동 관리 Mixin"""
    created_at = Column(
        DateTime(timezone=True),
        server_default=func.now(),
        nullable=False
    )
    updated_at = Column(
        DateTime(timezone=True),
        server_default=func.now(),
        onupdate=func.now(),
        nullable=False
    )

"""
pytest 설정 및 공통 픽스처
"""
import pytest
import sys
import os
from pathlib import Path
from fastapi.testclient import TestClient

# 프로젝트 루트를 Python 경로에 추가
project_root = Path(__file__).parent.parent.parent
backend_path = project_root / "apps" / "backend"
sys.path.insert(0, str(backend_path))

@pytest.fixture(scope="session")
def test_client():
    """FastAPI 테스트 클라이언트 픽스처"""
    from main import app
    return TestClient(app)

@pytest.fixture(scope="session")
def test_db():
    """테스트 데이터베이스 세션 픽스처"""
    from database import SessionLocal, engine
    from sqlalchemy import text
    
    # 테스트 데이터베이스 설정
    session = SessionLocal()
    try:
        # 테스트 전 초기화
        yield session
    finally:
        session.close()

@pytest.fixture
def sample_user_data():
    """샘플 사용자 데이터 픽스처"""
    return {
        "email": "test@example.com",
        "password": "test123",
        "full_name": "테스트 사용자",
        "role": "mentee"
    }

@pytest.fixture
def sample_mentor_data():
    """샘플 멘토 데이터 픽스처"""
    return {
        "email": "mentor@example.com",
        "password": "mentor123",
        "full_name": "테스트 멘토",
        "role": "mentor",
        "expertise": ["Python", "FastAPI"],
        "experience_years": 5
    }

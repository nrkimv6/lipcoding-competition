"""
애플리케이션 설정 관리
"""
import os
from dotenv import load_dotenv

# .env 파일 로드
load_dotenv()

class Settings:
    """애플리케이션 설정"""
    
    # 데이터베이스 설정 - PostgreSQL 기본값
    DATABASE_URL: str = os.getenv("DATABASE_URL", "postgresql://postgres:password@localhost:5432/mm_matching")
    
    # API 설정
    API_V1_STR: str = "/api/v1"
    PROJECT_NAME: str = "MM Matching API"
    PROJECT_VERSION: str = "1.0.0"
    PROJECT_DESCRIPTION: str = "멘토-멘티 매칭 서비스 API"
    
    # 서버 설정
    HOST: str = "0.0.0.0"
    PORT: int = int(os.getenv("PORT", "8080"))
    
    # CORS 설정
    ALLOWED_ORIGINS: list = ["http://localhost:3000"]
    
    # JWT 설정
    SECRET_KEY: str = os.getenv("SECRET_KEY", "mm-matching-secret-key-2024")
    ALGORITHM: str = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 30
    
    # 데이터베이스 연결 설정
    DB_POOL_PRE_PING: bool = True
    DB_POOL_RECYCLE: int = 300
    DB_ECHO: bool = False  # 테스트에서는 False로 설정

settings = Settings()

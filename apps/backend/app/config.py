"""
애플리케이션 설정 관리
"""
import os
from dotenv import load_dotenv

# .env 파일 로드
load_dotenv()

class Settings:
    """애플리케이션 설정"""
    
    # 데이터베이스 설정
    DATABASE_URL: str = os.getenv("DATABASE_URL", "")
    
    # API 설정
    API_V1_STR: str = "/api/v1"
    PROJECT_NAME: str = "MM Matching API"
    PROJECT_VERSION: str = "1.0.0"
    PROJECT_DESCRIPTION: str = "멘토-멘티 매칭 서비스 API"
    
    # CORS 설정
    ALLOWED_ORIGINS: list = ["http://localhost:3000"]
    
    # JWT 설정
    SECRET_KEY: str = os.getenv("SECRET_KEY", "your-secret-key-here")
    ALGORITHM: str = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 30
    
    # 데이터베이스 연결 설정
    DB_POOL_PRE_PING: bool = True
    DB_POOL_RECYCLE: int = 300
    DB_ECHO: bool = True  # 개발환경에서만 True
    
    def __init__(self):
        if not self.DATABASE_URL:
            raise ValueError("DATABASE_URL 환경변수가 설정되지 않았습니다.")

settings = Settings()

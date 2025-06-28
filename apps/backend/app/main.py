"""
FastAPI 애플리케이션 메인 모듈
"""
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from contextlib import asynccontextmanager
from sqlalchemy import text

from app.config import settings
from app.database import engine
from app.api.v1 import api_router

@asynccontextmanager
async def lifespan(app: FastAPI):
    """애플리케이션 생명주기 관리"""
    # 애플리케이션 시작 시 실행
    print(f"Starting {settings.PROJECT_NAME}...")
    
    # 데이터베이스 연결 확인
    try:
        with engine.connect() as connection:
            result = connection.execute(text("SELECT 1"))
            print("✅ 데이터베이스 연결 성공!")
    except Exception as e:
        print(f"❌ 데이터베이스 연결 실패: {e}")
    
    yield
    
    # 애플리케이션 종료 시 실행
    print(f"Shutting down {settings.PROJECT_NAME}...")

def create_app() -> FastAPI:
    """FastAPI 애플리케이션 생성"""
    app = FastAPI(
        title=settings.PROJECT_NAME,
        description=settings.PROJECT_DESCRIPTION,
        version=settings.PROJECT_VERSION,
        lifespan=lifespan
    )

    # CORS 설정
    app.add_middleware(
        CORSMiddleware,
        allow_origins=settings.ALLOWED_ORIGINS,
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

    # API 라우터 등록
    app.include_router(api_router, prefix=settings.API_V1_STR)

    # 기본 엔드포인트
    @app.get("/")
    async def root():
        return {"message": f"{settings.PROJECT_NAME}에 오신 것을 환영합니다!"}

    @app.get("/health")
    async def health_check():
        return {"status": "healthy", "service": "mm-matching-api"}

    return app

app = create_app()

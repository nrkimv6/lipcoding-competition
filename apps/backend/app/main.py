"""
FastAPI 애플리케이션 메인 모듈
"""
import os
import sys
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from contextlib import asynccontextmanager
from sqlalchemy import text

from app.config import settings
from app.database import engine
from app.api.v1 import api_router
from app.api.v1.auth import router as auth_router

# 디버깅을 위한 로그 추가
print("=" * 50)
print("🚀 MM Matching API Starting...")
print(f"📁 Python path: {sys.path}")
print(f"📂 Current working directory: {os.getcwd()}")
print(f"🌍 Environment variables:")
print(f"  DATABASE_URL: {os.getenv('DATABASE_URL', 'Not set - will use default')}")
print(f"  SECRET_KEY: {'Set' if os.getenv('SECRET_KEY') else 'Not set - will use default'}")
print(f"  PORT: {os.getenv('PORT', 'Not set - will use 8080')}")
print(f"  HOST: {os.getenv('HOST', 'Not set - will use 0.0.0.0')}")
print("=" * 50)

@asynccontextmanager
async def lifespan(app: FastAPI):
    """애플리케이션 생명주기 관리"""
    # 애플리케이션 시작 시 실행
    try:
        print(f"Starting {settings.PROJECT_NAME}...")
        
        # 데이터베이스 연결 확인
        try:
            with engine.connect() as connection:
                result = connection.execute(text("SELECT 1"))
                print("✅ 데이터베이스 연결 성공!")
        except Exception as e:
            print(f"⚠️ 데이터베이스 연결 실패: {e}")
            print("⚠️ 데이터베이스 없이 계속 진행합니다...")
        
        # 테이블 생성 (개발환경에서만)
        try:
            from app.database import create_tables
            create_tables()
            print("✅ 데이터베이스 테이블 확인/생성 완료!")
        except Exception as e:
            print(f"⚠️ 테이블 생성 중 오류: {e}")
            print("⚠️ 테이블 생성 없이 계속 진행합니다...")
            
        print("✅ 앱 시작 완료!")
        
    except Exception as e:
        print(f"⚠️ 시작 과정에서 오류 발생: {e}")
        print("⚠️ 기본 설정으로 계속 진행합니다...")
    
    yield
    
    # 애플리케이션 종료 시 실행
    try:
        print(f"Shutting down {settings.PROJECT_NAME}...")
    except:
        print("Shutting down...")

def create_app() -> FastAPI:
    """FastAPI 애플리케이션 생성"""
    app = FastAPI(
        title=settings.PROJECT_NAME,
        description=settings.PROJECT_DESCRIPTION,
        version=settings.PROJECT_VERSION,
        lifespan=lifespan,
        # OpenAPI 문서 경로 설정
        docs_url="/docs",  # Swagger UI 경로
        redoc_url="/redoc",  # ReDoc 경로  
        openapi_url="/openapi.json"  # OpenAPI JSON 경로
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
    
    # 테스트 호환을 위한 추가 엔드포인트
    app.include_router(auth_router, prefix="/api", tags=["테스트 호환"])

    # 기본 엔드포인트
    @app.get("/")
    async def root():
        return {"message": f"{settings.PROJECT_NAME}에 오신 것을 환영합니다!"}

    @app.get("/health")
    async def health_check():
        try:
            # 데이터베이스 연결 확인
            with engine.connect() as connection:
                connection.execute(text("SELECT 1"))
                db_status = "connected"
        except Exception as e:
            db_status = f"disconnected: {str(e)}"
            
        return {
            "status": "healthy", 
            "service": "mm-matching-api",
            "database": db_status,
            "port": settings.PORT,
            "host": settings.HOST
        }

    # 기본 테스트 엔드포인트 추가
    @app.get("/test")
    async def test_endpoint():
        return {"message": "Server is running!", "timestamp": "2024-01-01"}

    # 간단한 ping 엔드포인트
    @app.get("/ping")
    async def ping():
        return {"ping": "pong"}

    # /api/test 엔드포인트도 추가 (테스트 호환)
    @app.get("/api/test")
    async def api_test():
        return {"message": "API is working!", "service": "mm-matching-api"}

    return app

app = create_app()

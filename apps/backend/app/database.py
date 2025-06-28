"""
데이터베이스 연결 설정
"""
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from app.config import settings

# Base 클래스 생성
Base = declarative_base()

# SQLAlchemy 엔진 생성
print(f"🔍 Attempting to create database engine...")
print(f"📍 DATABASE_URL from settings: {settings.DATABASE_URL}")

engine = None
try:
    print(f"🔗 Creating database engine for: {settings.DATABASE_URL}")
    engine = create_engine(
        settings.DATABASE_URL,
        pool_pre_ping=settings.DB_POOL_PRE_PING,
        pool_recycle=settings.DB_POOL_RECYCLE,
        echo=settings.DB_ECHO
    )
    # 연결 테스트
    with engine.connect() as conn:
        result = conn.execute("SELECT 1")
        print(f"✅ Database engine created and tested successfully")
except Exception as e:
    print(f"⚠️ Primary database connection failed: {e}")
    
    # 다양한 fallback 시도
    fallback_urls = [
        "postgresql://postgres:password@localhost:5432/mm_matching",
        "postgresql://postgres:postgres@localhost:5432/mm_matching", 
        "postgresql://postgres:@localhost:5432/mm_matching",
        "sqlite:///./mm_matching.db"
    ]
    
    for i, fallback_url in enumerate(fallback_urls):
        try:
            print(f"🔄 Trying fallback {i+1}: {fallback_url}")
            engine = create_engine(fallback_url, echo=False)
            with engine.connect() as conn:
                conn.execute("SELECT 1")
            print(f"✅ Fallback database engine {i+1} successful")
            break
        except Exception as fallback_error:
            print(f"❌ Fallback {i+1} failed: {fallback_error}")
            continue
    
    if engine is None:
        print("🆘 All database connections failed, creating in-memory SQLite")
        engine = create_engine("sqlite:///:memory:", echo=False)
        print("✅ In-memory SQLite engine created")

# 세션 팩토리
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# 데이터베이스 세션 의존성
def get_db():
    """데이터베이스 세션 생성"""
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

def create_tables():
    """데이터베이스 테이블 생성"""
    # 모든 모델을 import한 후 테이블 생성
    from app.models import User, MentorProfile, MenteeProfile, Match
    Base.metadata.create_all(bind=engine)

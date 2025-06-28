#!/usr/bin/env python3
"""
서버 실행 테스트 스크립트
"""
import sys
import traceback

try:
    # 1. 모든 모듈 import 테스트
    print("🔄 모듈 import 테스트 중...")
    from app.main import app
    from app.config import settings
    from app.database import engine, get_db
    from app.models import User, UserRole, MentorProfile, MenteeProfile, Match, MatchStatus
    print("✅ 모든 모듈 import 성공!")
    
    # 2. 데이터베이스 연결 테스트
    print("🔄 데이터베이스 연결 테스트 중...")
    from sqlalchemy import text
    with engine.connect() as connection:
        result = connection.execute(text("SELECT 1"))
        print("✅ 데이터베이스 연결 성공!")
    
    # 3. 테이블 생성 테스트
    print("🔄 테이블 생성/확인 중...")
    from app.database import create_tables
    create_tables()
    print("✅ 테이블 생성/확인 완료!")
    
    # 4. FastAPI 앱 정보
    print(f"🚀 FastAPI 앱 준비 완료!")
    print(f"   - 프로젝트명: {settings.PROJECT_NAME}")
    print(f"   - 데이터베이스: {settings.DATABASE_URL}")
    print(f"   - API 경로: {settings.API_V1_STR}")
    
    # 5. API 라우터 확인
    print("🔄 API 라우터 확인 중...")
    routes = []
    for route in app.routes:
        if hasattr(route, 'path'):
            routes.append(f"{route.methods} {route.path}")
    
    print("✅ 등록된 API 라우터:")
    for route in sorted(routes):
        print(f"   - {route}")
    
    print("\n🎉 모든 테스트 통과! 서버 실행 준비 완료!")
    print("\n📝 다음 명령어로 서버를 실행하세요:")
    print("   python main.py")
    print("   또는")
    print("   uvicorn main:app --reload")
    
except Exception as e:
    print(f"❌ 오류 발생: {e}")
    print("\n🔍 상세 오류 정보:")
    traceback.print_exc()
    sys.exit(1)

#!/usr/bin/env python3
"""
API 수동 테스트 스크립트
"""
import asyncio
import sys
import os

# 현재 디렉토리를 Python 경로에 추가
sys.path.insert(0, os.getcwd())

async def test_imports():
    """모든 모듈이 정상적으로 import되는지 테스트"""
    try:
        print("🔍 모듈 import 테스트 시작...")
        
        # 기본 모듈들
        from app.config import settings
        print("✅ config 모듈 import 성공")
        
        from app.database import engine, get_db, create_tables
        print("✅ database 모듈 import 성공")
        
        # 모델들
        from app.models import User, UserRole, MentorProfile, MenteeProfile, Match, MatchStatus
        print("✅ models 모듈 import 성공")
        
        # 스키마들
        from app.schemas.auth import LoginRequest, RegisterRequest, Token
        from app.schemas.user import UserResponse, UserUpdate
        from app.schemas.mentor import MentorProfileResponse, MenteeProfileResponse
        from app.schemas.match import MatchCreate, MatchResponse
        print("✅ schemas 모듈 import 성공")
        
        # API 라우터들
        from app.api.v1 import auth, users, mentors, matches
        print("✅ API 라우터 import 성공")
        
        # 유틸리티들
        from app.utils.auth import verify_password, get_password_hash, create_access_token
        print("✅ auth utils 모듈 import 성공")
        
        # 의존성들
        from app.dependencies import get_current_user, get_current_mentor, get_current_mentee
        print("✅ dependencies 모듈 import 성공")
        
        # FastAPI 앱
        from app.main import create_app
        print("✅ main 모듈 import 성공")
        
        print("\n🎉 모든 모듈 import 성공!")
        return True
        
    except Exception as e:
        print(f"❌ Import 오류: {e}")
        import traceback
        traceback.print_exc()
        return False

async def test_database_connection():
    """데이터베이스 연결 테스트"""
    try:
        print("\n🔍 데이터베이스 연결 테스트 시작...")
        
        from app.database import engine
        from sqlalchemy import text
        
        with engine.connect() as connection:
            result = connection.execute(text("SELECT 1 as test"))
            row = result.fetchone()
            if row and row[0] == 1:
                print("✅ 데이터베이스 연결 성공")
                return True
            else:
                print("❌ 데이터베이스 연결 실패: 잘못된 응답")
                return False
                
    except Exception as e:
        print(f"❌ 데이터베이스 연결 오류: {e}")
        return False

async def test_table_creation():
    """테이블 생성 테스트"""
    try:
        print("\n🔍 테이블 생성 테스트 시작...")
        
        from app.database import create_tables, engine
        from sqlalchemy import text
        
        # 테이블 생성
        create_tables()
        print("✅ 테이블 생성 함수 실행 완료")
        
        # 테이블 존재 확인
        with engine.connect() as connection:
            # PostgreSQL에서 테이블 목록 조회
            result = connection.execute(text("""
                SELECT table_name 
                FROM information_schema.tables 
                WHERE table_schema = 'public'
                ORDER BY table_name
            """))
            
            tables = [row[0] for row in result.fetchall()]
            print(f"📋 생성된 테이블 목록: {tables}")
            
            expected_tables = ['users', 'mentor_profiles', 'mentee_profiles', 'matches']
            missing_tables = [table for table in expected_tables if table not in tables]
            
            if missing_tables:
                print(f"⚠️ 누락된 테이블: {missing_tables}")
                return False
            else:
                print("✅ 모든 필수 테이블이 존재합니다")
                return True
                
    except Exception as e:
        print(f"❌ 테이블 생성 오류: {e}")
        import traceback
        traceback.print_exc()
        return False

async def test_fastapi_app():
    """FastAPI 앱 생성 테스트"""
    try:
        print("\n🔍 FastAPI 앱 생성 테스트 시작...")
        
        from app.main import create_app
        
        app = create_app()
        print("✅ FastAPI 앱 생성 성공")
        
        # 라우터 확인
        routes = [route.path for route in app.routes]
        print(f"📋 등록된 라우트: {len(routes)}개")
        
        # 주요 라우트 확인
        expected_routes = [
            "/",
            "/health", 
            "/api/v1/auth/register",
            "/api/v1/auth/login",
            "/api/v1/users/profile",
            "/api/v1/mentors/",
            "/api/v1/matches/request"
        ]
        
        missing_routes = [route for route in expected_routes if route not in routes]
        if missing_routes:
            print(f"⚠️ 누락된 라우트: {missing_routes}")
        else:
            print("✅ 모든 주요 라우트가 등록되었습니다")
        
        return True
        
    except Exception as e:
        print(f"❌ FastAPI 앱 생성 오류: {e}")
        import traceback
        traceback.print_exc()
        return False

async def main():
    """메인 테스트 함수"""
    print("🚀 MM Matching API 테스트 시작\n")
    
    tests = [
        ("모듈 Import", test_imports),
        ("데이터베이스 연결", test_database_connection),
        ("테이블 생성", test_table_creation),
        ("FastAPI 앱", test_fastapi_app),
    ]
    
    results = []
    
    for test_name, test_func in tests:
        print(f"=" * 50)
        result = await test_func()
        results.append((test_name, result))
        print(f"{'✅' if result else '❌'} {test_name}: {'성공' if result else '실패'}")
    
    print(f"\n" + "=" * 50)
    print("📊 테스트 결과 요약:")
    
    success_count = sum(1 for _, result in results if result)
    total_count = len(results)
    
    for test_name, result in results:
        status = "✅ 성공" if result else "❌ 실패"
        print(f"  {test_name}: {status}")
    
    print(f"\n🏆 전체 결과: {success_count}/{total_count} 성공")
    
    if success_count == total_count:
        print("🎉 모든 테스트가 성공했습니다! API 서버를 실행할 수 있습니다.")
        print("\n💡 서버 실행 명령어:")
        print("   d:\\mm-matching-app\\apps\\backend\\venv\\Scripts\\uvicorn.exe main:app --reload --host 0.0.0.0 --port 8000")
        print("\n📖 API 문서:")
        print("   http://localhost:8000/docs")
    else:
        print("⚠️ 일부 테스트가 실패했습니다. 문제를 해결한 후 다시 시도해주세요.")

if __name__ == "__main__":
    asyncio.run(main())

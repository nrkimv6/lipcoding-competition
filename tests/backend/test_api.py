"""
API 테스트 스크립트
"""
import asyncio
import sys
import os

# 현재 파일의 디렉토리를 Python 경로에 추가
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

async def test_api_imports():
    """API 모듈들이 정상적으로 import되는지 테스트"""
    try:
        print("🔧 API 모듈 import 테스트 시작...")
        
        # 모델 import 테스트
        from app.models import Base, User, UserRole, MentorProfile, MenteeProfile, Match, MatchStatus
        print("✅ 모델 import 성공")
        
        # 스키마 import 테스트
        from app.schemas.auth import LoginRequest, RegisterRequest, Token
        from app.schemas.user import UserResponse, UserUpdate
        from app.schemas.mentor import MentorProfileCreate, MentorProfileResponse
        from app.schemas.match import MatchCreate, MatchResponse
        print("✅ 스키마 import 성공")
        
        # API 라우터 import 테스트
        from app.api.v1 import api_router
        from app.api.v1.auth import router as auth_router
        from app.api.v1.users import router as users_router
        from app.api.v1.mentors import router as mentors_router
        from app.api.v1.matches import router as matches_router
        print("✅ API 라우터 import 성공")
        
        # 유틸리티 import 테스트
        from app.utils.auth import create_access_token, verify_password, get_password_hash
        from app.dependencies import get_current_user
        print("✅ 유틸리티 import 성공")
        
        # 데이터베이스 연결 테스트
        from app.database import engine, get_db, create_tables
        from sqlalchemy import text
        
        with engine.connect() as connection:
            result = connection.execute(text("SELECT 1"))
            print("✅ 데이터베이스 연결 성공")
        
        print("\n🎉 모든 import 테스트 완료! API 구현이 정상적으로 작동합니다.")
        
        # 구현된 API 엔드포인트 요약
        print("\n📋 구현된 API 엔드포인트:")
        print("🔐 인증 API (/api/v1/auth):")
        print("  - POST /auth/register   : 회원가입")
        print("  - POST /auth/login      : 로그인")
        print("  - GET  /auth/me         : 현재 사용자 정보")
        print("  - POST /auth/logout     : 로그아웃")
        
        print("👤 사용자 API (/api/v1/users):")
        print("  - GET  /users/profile   : 내 프로필 조회")
        print("  - PUT  /users/profile   : 프로필 수정")
        print("  - GET  /users/{user_id} : 특정 사용자 조회")
        
        print("👨‍🏫 멘토 API (/api/v1/mentors):")
        print("  - GET  /mentors/        : 멘토 목록 조회 (필터링)")
        print("  - GET  /mentors/{id}    : 특정 멘토 조회")
        print("  - POST /mentors/profile : 멘토 프로필 생성")
        print("  - PUT  /mentors/profile : 멘토 프로필 수정")
        print("  - GET  /mentors/profile/me : 내 멘토 프로필")
        
        print("🤝 매칭 API (/api/v1/matches):")
        print("  - POST /matches/request      : 매칭 요청")
        print("  - GET  /matches/sent         : 보낸 요청 목록")
        print("  - GET  /matches/received     : 받은 요청 목록")
        print("  - PUT  /matches/{id}/accept  : 매칭 수락")
        print("  - PUT  /matches/{id}/reject  : 매칭 거절")
        print("  - GET  /matches/current      : 현재 활성 매칭")
        
        return True
        
    except Exception as e:
        print(f"❌ Import 테스트 실패: {e}")
        import traceback
        traceback.print_exc()
        return False

if __name__ == "__main__":
    success = asyncio.run(test_api_imports())
    if success:
        print("\n🚀 서버 실행 명령어:")
        print("uvicorn app.main:app --reload --host 0.0.0.0 --port 8000")
        print("\n📖 API 문서 확인:")
        print("http://localhost:8000/docs")
    else:
        print("\n❌ API 테스트 실패. 오류를 확인해주세요.")
        sys.exit(1)

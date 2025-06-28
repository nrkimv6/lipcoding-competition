"""
스탠드얼론 데이터베이스 연결 테스트 스크립트
독립적으로 실행 가능한 DB 연결 검증 도구
"""
import os
import sys
from sqlalchemy import text
from database import engine, SessionLocal

def main():
    """메인 실행 함수"""
    print("🔍 스탠드얼론 데이터베이스 연결 테스트를 시작합니다...")
    print("=" * 60)
    
    try:
        # 1. 엔진 연결 테스트
        with engine.connect() as connection:
            print("✅ SQLAlchemy 엔진 연결 성공!")
            
            # 2. PostgreSQL 버전 확인
            result = connection.execute(text("SELECT version();"))
            version = result.fetchone()[0]
            print(f"📊 PostgreSQL 버전: {version.split(',')[0]}")
            
            # 3. 현재 데이터베이스 확인
            result = connection.execute(text("SELECT current_database();"))
            db_name = result.fetchone()[0]
            print(f"💾 현재 데이터베이스: {db_name}")
            
            # 4. 테이블 목록 확인
            result = connection.execute(text("""
                SELECT table_name 
                FROM information_schema.tables 
                WHERE table_schema = 'public'
                ORDER BY table_name;
            """))
            tables = [row[0] for row in result.fetchall()]
            print(f"📋 테이블 목록: {', '.join(tables)}")
            
            # 5. 사용자 데이터 확인
            if 'users' in tables:
                result = connection.execute(text("SELECT COUNT(*) FROM users;"))
                user_count = result.fetchone()[0]
                print(f"👥 총 사용자 수: {user_count}명")
            
            # 6. 세션 테스트
            print("\n🔧 세션 테스트 중...")
            db = SessionLocal()
            try:
                result = db.execute(text("SELECT 'Session test successful' as message;"))
                message = result.fetchone()[0]
                print(f"✅ {message}")
            finally:
                db.close()
            
        print("\n" + "=" * 60)
        print("🎉 모든 데이터베이스 연결 테스트가 성공했습니다!")
        print("📝 이 스크립트는 pytest와 독립적으로 실행됩니다.")
        print("💡 전체 테스트 스위트는 'run_tests.bat' 명령을 사용하세요.")
        return True
        
    except Exception as e:
        print(f"\n❌ 데이터베이스 연결 실패: {str(e)}")
        print("🔧 트러블슈팅:")
        print("   1. PostgreSQL 서비스가 실행 중인지 확인")
        print("   2. 데이터베이스 'mm_matching'이 존재하는지 확인")
        print("   3. 환경변수 PGPASSWORD가 설정되어 있는지 확인")
        return False

if __name__ == "__main__":
    success = main()
    sys.exit(0 if success else 1)

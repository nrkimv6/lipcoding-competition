"""
데이터베이스 연결 테스트 스크립트
"""
import os
import sys
from sqlalchemy import text
from database import engine, SessionLocal

def test_database_connection():
    """PostgreSQL 데이터베이스 연결 테스트"""
    print("🔍 데이터베이스 연결 테스트를 시작합니다...")
    
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
            
        print("\n🎉 모든 데이터베이스 연결 테스트가 성공했습니다!")
        return True
        
    except Exception as e:
        print(f"\n❌ 데이터베이스 연결 실패: {str(e)}")
        return False

if __name__ == "__main__":
    success = test_database_connection()
    sys.exit(0 if success else 1)

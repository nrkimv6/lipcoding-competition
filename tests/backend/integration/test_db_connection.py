"""
데이터베이스 연결 통합 테스트
"""
import os
import sys
import pytest
from sqlalchemy import text

def test_database_connection(test_db):
    """PostgreSQL 데이터베이스 연결 테스트"""
    print("🔍 데이터베이스 연결 테스트를 시작합니다...")
    
    try:
        # 1. 기본 연결 테스트
        result = test_db.execute(text("SELECT 1 as test"))
        assert result.fetchone()[0] == 1
        print("✅ 기본 데이터베이스 연결 성공!")
        
        # 2. PostgreSQL 버전 확인
        result = test_db.execute(text("SELECT version();"))
        version = result.fetchone()[0]
        print(f"📊 PostgreSQL 버전: {version.split(',')[0]}")
        
        # 3. 현재 데이터베이스 확인
        result = test_db.execute(text("SELECT current_database();"))
        db_name = result.fetchone()[0]
        print(f"💾 현재 데이터베이스: {db_name}")
        assert db_name == "mm_matching"
        
        # 4. 테이블 목록 확인
        result = test_db.execute(text("""
            SELECT table_name 
            FROM information_schema.tables 
            WHERE table_schema = 'public'
            ORDER BY table_name;
        """))
        tables = [row[0] for row in result.fetchall()]
        print(f"📋 테이블 목록: {', '.join(tables)}")
        
        # 필수 테이블 존재 확인
        required_tables = ["users", "mentor_profiles", "mentee_profiles", "matchings"]
        for table in required_tables:
            assert table in tables, f"필수 테이블 '{table}'이 존재하지 않습니다."
        
        # 5. 사용자 데이터 확인
        result = test_db.execute(text("SELECT COUNT(*) FROM users;"))
        user_count = result.fetchone()[0]
        print(f"👥 총 사용자 수: {user_count}명")
        assert user_count >= 0
        
        print("🎉 모든 데이터베이스 연결 테스트가 성공했습니다!")
        
    except Exception as e:
        print(f"❌ 데이터베이스 연결 실패: {str(e)}")
        raise

def test_database_schema_integrity(test_db):
    """데이터베이스 스키마 무결성 테스트"""
    
    # users 테이블 구조 확인
    result = test_db.execute(text("""
        SELECT column_name, data_type, is_nullable
        FROM information_schema.columns
        WHERE table_name = 'users'
        ORDER BY ordinal_position;
    """))
    user_columns = {row[0]: {"type": row[1], "nullable": row[2]} for row in result.fetchall()}
    
    # 필수 컬럼 확인
    required_user_columns = ["id", "email", "password_hash", "full_name", "role"]
    for col in required_user_columns:
        assert col in user_columns, f"users 테이블에 '{col}' 컬럼이 없습니다."
    
    print("✅ 데이터베이스 스키마 무결성 검증 완료!")

def test_database_crud_operations(test_db):
    """기본 CRUD 연산 테스트"""
    
    try:
        # 테스트 데이터 삽입
        test_email = "test_crud@example.com"
        
        # 기존 테스트 데이터 삭제 (있다면)
        test_db.execute(text("DELETE FROM users WHERE email = :email"), {"email": test_email})
        test_db.commit()
        
        # CREATE 테스트
        insert_result = test_db.execute(text("""
            INSERT INTO users (email, password_hash, full_name, role, created_at)
            VALUES (:email, :password, :name, :role, NOW())
            RETURNING id
        """), {
            "email": test_email,
            "password": "hashed_password",
            "name": "CRUD 테스트 사용자",
            "role": "mentee"
        })
        user_id = insert_result.fetchone()[0]
        test_db.commit()
        
        # READ 테스트
        read_result = test_db.execute(text("""
            SELECT email, full_name, role FROM users WHERE id = :id
        """), {"id": user_id})
        user_data = read_result.fetchone()
        assert user_data[0] == test_email
        assert user_data[1] == "CRUD 테스트 사용자"
        assert user_data[2] == "mentee"
        
        # UPDATE 테스트
        test_db.execute(text("""
            UPDATE users SET full_name = :name WHERE id = :id
        """), {"name": "업데이트된 사용자", "id": user_id})
        test_db.commit()
        
        # 업데이트 확인
        read_result = test_db.execute(text("""
            SELECT full_name FROM users WHERE id = :id
        """), {"id": user_id})
        updated_name = read_result.fetchone()[0]
        assert updated_name == "업데이트된 사용자"
        
        # DELETE 테스트
        test_db.execute(text("DELETE FROM users WHERE id = :id"), {"id": user_id})
        test_db.commit()
        
        # 삭제 확인
        read_result = test_db.execute(text("""
            SELECT COUNT(*) FROM users WHERE id = :id
        """), {"id": user_id})
        count = read_result.fetchone()[0]
        assert count == 0
        
        print("✅ CRUD 연산 테스트 완료!")
        
    except Exception as e:
        # 테스트 실패 시 롤백
        test_db.rollback()
        raise

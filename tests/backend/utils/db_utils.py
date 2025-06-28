"""
데이터베이스 테스트 유틸리티
"""
from sqlalchemy import text
from typing import Dict, Any, List

class DatabaseTestUtils:
    """데이터베이스 테스트를 위한 유틸리티 클래스"""
    
    def __init__(self, db_session):
        self.db = db_session
    
    def create_test_user(self, email: str = "test@example.com", 
                        role: str = "mentee", **kwargs) -> int:
        """테스트 사용자 생성"""
        user_data = {
            "email": email,
            "password_hash": "hashed_password",
            "full_name": kwargs.get("full_name", "테스트 사용자"),
            "role": role
        }
        
        result = self.db.execute(text("""
            INSERT INTO users (email, password_hash, full_name, role, created_at)
            VALUES (:email, :password_hash, :full_name, :role, NOW())
            RETURNING id
        """), user_data)
        
        user_id = result.fetchone()[0]
        self.db.commit()
        return user_id
    
    def create_test_mentor_profile(self, user_id: int, **kwargs) -> int:
        """테스트 멘토 프로필 생성"""
        mentor_data = {
            "user_id": user_id,
            "expertise": kwargs.get("expertise", ["Python", "FastAPI"]),
            "experience_years": kwargs.get("experience_years", 3),
            "bio": kwargs.get("bio", "테스트 멘토 소개"),
            "is_available": kwargs.get("is_available", True)
        }
        
        # expertise 배열을 PostgreSQL 배열 형태로 변환
        expertise_str = "{" + ",".join(mentor_data["expertise"]) + "}"
        
        result = self.db.execute(text("""
            INSERT INTO mentor_profiles 
            (user_id, expertise, experience_years, bio, is_available, created_at)
            VALUES (:user_id, :expertise, :experience_years, :bio, :is_available, NOW())
            RETURNING id
        """), {
            "user_id": mentor_data["user_id"],
            "expertise": expertise_str,
            "experience_years": mentor_data["experience_years"],
            "bio": mentor_data["bio"],
            "is_available": mentor_data["is_available"]
        })
        
        profile_id = result.fetchone()[0]
        self.db.commit()
        return profile_id
    
    def create_test_matching(self, mentee_id: int, mentor_id: int) -> int:
        """테스트 매칭 생성"""
        result = self.db.execute(text("""
            INSERT INTO matchings (mentee_id, mentor_id, status, created_at)
            VALUES (:mentee_id, :mentor_id, 'pending', NOW())
            RETURNING id
        """), {
            "mentee_id": mentee_id,
            "mentor_id": mentor_id
        })
        
        matching_id = result.fetchone()[0]
        self.db.commit()
        return matching_id
    
    def cleanup_test_data(self, emails: List[str]):
        """테스트 데이터 정리"""
        for email in emails:
            # 관련된 모든 데이터 삭제 (외래키 제약 고려)
            user_result = self.db.execute(text("""
                SELECT id FROM users WHERE email = :email
            """), {"email": email})
            
            user_row = user_result.fetchone()
            if user_row:
                user_id = user_row[0]
                
                # 매칭 데이터 삭제
                self.db.execute(text("""
                    DELETE FROM matchings 
                    WHERE mentee_id = :user_id OR mentor_id = :user_id
                """), {"user_id": user_id})
                
                # 프로필 데이터 삭제
                self.db.execute(text("""
                    DELETE FROM mentor_profiles WHERE user_id = :user_id
                """), {"user_id": user_id})
                
                self.db.execute(text("""
                    DELETE FROM mentee_profiles WHERE user_id = :user_id
                """), {"user_id": user_id})
                
                # 사용자 데이터 삭제
                self.db.execute(text("""
                    DELETE FROM users WHERE id = :user_id
                """), {"user_id": user_id})
        
        self.db.commit()
    
    def get_table_count(self, table_name: str) -> int:
        """테이블 레코드 수 조회"""
        result = self.db.execute(text(f"SELECT COUNT(*) FROM {table_name}"))
        return result.fetchone()[0]
    
    def table_exists(self, table_name: str) -> bool:
        """테이블 존재 여부 확인"""
        result = self.db.execute(text("""
            SELECT EXISTS (
                SELECT FROM information_schema.tables 
                WHERE table_schema = 'public' 
                AND table_name = :table_name
            )
        """), {"table_name": table_name})
        return result.fetchone()[0]

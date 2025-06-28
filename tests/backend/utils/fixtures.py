"""
테스트 데이터 픽스처
샘플 데이터 및 테스트용 데이터셋
"""
from typing import Dict, List, Any

class TestDataFixtures:
    """테스트 데이터 픽스처 클래스"""
    
    @staticmethod
    def get_sample_users() -> List[Dict[str, Any]]:
        """샘플 사용자 데이터"""
        return [
            {
                "email": "mentor1@example.com",
                "password": "password123",
                "full_name": "김멘토",
                "role": "mentor"
            },
            {
                "email": "mentor2@example.com", 
                "password": "password123",
                "full_name": "이멘토",
                "role": "mentor"
            },
            {
                "email": "mentee1@example.com",
                "password": "password123", 
                "full_name": "박멘티",
                "role": "mentee"
            },
            {
                "email": "mentee2@example.com",
                "password": "password123",
                "full_name": "최멘티", 
                "role": "mentee"
            }
        ]
    
    @staticmethod
    def get_sample_mentor_profiles() -> List[Dict[str, Any]]:
        """샘플 멘토 프로필 데이터"""
        return [
            {
                "expertise": ["Python", "FastAPI", "PostgreSQL"],
                "experience_years": 5,
                "bio": "풀스택 개발자로 5년간 근무하며 다양한 프로젝트 경험이 있습니다.",
                "is_available": True
            },
            {
                "expertise": ["JavaScript", "React", "Node.js"],
                "experience_years": 3,
                "bio": "프론트엔드 전문가로 React 생태계에 특화되어 있습니다.",
                "is_available": True
            },
            {
                "expertise": ["DevOps", "AWS", "Docker"],
                "experience_years": 7,
                "bio": "클라우드 인프라 및 DevOps 전문가입니다.",
                "is_available": False
            }
        ]
    
    @staticmethod
    def get_sample_mentee_profiles() -> List[Dict[str, Any]]:
        """샘플 멘티 프로필 데이터"""
        return [
            {
                "learning_goals": ["Python 기초", "웹 개발"],
                "current_level": "beginner",
                "preferred_schedule": "weekday_evening",
                "bio": "프로그래밍을 처음 시작하는 초보자입니다."
            },
            {
                "learning_goals": ["React 심화", "상태 관리"],
                "current_level": "intermediate", 
                "preferred_schedule": "weekend",
                "bio": "프론트엔드 개발 경험이 있으며 React를 더 깊이 학습하고 싶습니다."
            }
        ]
    
    @staticmethod
    def get_sample_matching_requests() -> List[Dict[str, Any]]:
        """샘플 매칭 요청 데이터"""
        return [
            {
                "message": "Python 웹 개발을 배우고 싶어서 연락드립니다.",
                "preferred_duration": "3_months",
                "preferred_frequency": "weekly"
            },
            {
                "message": "React 프로젝트에서 상태 관리 패턴에 대해 멘토링 받고 싶습니다.",
                "preferred_duration": "1_month", 
                "preferred_frequency": "biweekly"
            }
        ]
    
    @staticmethod
    def get_invalid_user_data() -> List[Dict[str, Any]]:
        """유효하지 않은 사용자 데이터 (검증 테스트용)"""
        return [
            {
                "email": "invalid-email",  # 잘못된 이메일 형식
                "password": "123",  # 너무 짧은 비밀번호
                "full_name": "",  # 빈 이름
                "role": "mentee"
            },
            {
                "email": "",  # 빈 이메일
                "password": "password123",
                "full_name": "테스트 사용자",
                "role": "invalid_role"  # 잘못된 역할
            },
            {
                # 필수 필드 누락
                "email": "test@example.com",
                "password": "password123"
                # full_name, role 누락
            }
        ]
    
    @staticmethod
    def get_api_test_cases() -> Dict[str, List[Dict[str, Any]]]:
        """API 테스트 케이스"""
        return {
            "auth": [
                {
                    "name": "valid_login",
                    "data": {"email": "test@example.com", "password": "password123"},
                    "expected_status": 200
                },
                {
                    "name": "invalid_password", 
                    "data": {"email": "test@example.com", "password": "wrongpassword"},
                    "expected_status": 401
                },
                {
                    "name": "nonexistent_user",
                    "data": {"email": "nonexistent@example.com", "password": "password123"},
                    "expected_status": 401
                }
            ],
            "mentor_search": [
                {
                    "name": "search_by_expertise",
                    "params": {"expertise": "Python"},
                    "expected_status": 200
                },
                {
                    "name": "search_by_experience",
                    "params": {"min_experience": 3},
                    "expected_status": 200
                },
                {
                    "name": "search_available_only",
                    "params": {"available": True},
                    "expected_status": 200
                }
            ]
        }

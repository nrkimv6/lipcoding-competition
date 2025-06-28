"""
API 엔드포인트 단위 테스트
"""
import pytest
from fastapi.testclient import TestClient

def test_read_root(test_client):
    """루트 엔드포인트 테스트"""
    response = test_client.get("/")
    assert response.status_code == 200
    assert "message" in response.json()

def test_health_check(test_client):
    """헬스체크 엔드포인트 테스트"""
    response = test_client.get("/health")
    assert response.status_code == 200
    assert response.json()["status"] == "healthy"

def test_get_mentors(test_client):
    """멘토 목록 조회 테스트"""
    response = test_client.get("/api/v1/mentors")
    assert response.status_code == 200
    assert "mentors" in response.json()

def test_get_mentees(test_client):
    """멘티 목록 조회 테스트"""
    response = test_client.get("/api/v1/mentees")
    assert response.status_code == 200
    assert "mentees" in response.json()

class TestUserAPI:
    """사용자 API 테스트 클래스"""
    
    def test_user_registration(self, test_client, sample_user_data):
        """사용자 회원가입 테스트"""
        # TODO: 회원가입 API 구현 후 테스트 작성
        pass
    
    def test_user_login(self, test_client, sample_user_data):
        """사용자 로그인 테스트"""
        # TODO: 로그인 API 구현 후 테스트 작성
        pass

class TestMentorAPI:
    """멘토 API 테스트 클래스"""
    
    def test_mentor_profile_creation(self, test_client, sample_mentor_data):
        """멘토 프로필 생성 테스트"""
        # TODO: 멘토 프로필 API 구현 후 테스트 작성
        pass
    
    def test_mentor_search(self, test_client):
        """멘토 검색 테스트"""
        # TODO: 멘토 검색 API 구현 후 테스트 작성
        pass

class TestMatchingAPI:
    """매칭 API 테스트 클래스"""
    
    def test_create_matching_request(self, test_client):
        """매칭 요청 생성 테스트"""
        # TODO: 매칭 요청 API 구현 후 테스트 작성
        pass
    
    def test_accept_matching_request(self, test_client):
        """매칭 요청 수락 테스트"""
        # TODO: 매칭 수락 API 구현 후 테스트 작성
        pass

"""
멘토 관리 API 엔드포인트
"""
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.database import get_db

router = APIRouter()

@router.get("/")
async def get_mentors():
    """멘토 목록 조회"""
    return {"mentors": [], "message": "멘토 목록을 조회합니다"}

@router.get("/search")
async def search_mentors():
    """멘토 검색"""
    return {"message": "멘토 검색 기능이 구현될 예정입니다"}

@router.get("/{mentor_id}")
async def get_mentor_profile(mentor_id: int):
    """특정 멘토 프로필 조회"""
    return {"message": f"멘토 {mentor_id} 프로필 조회 기능이 구현될 예정입니다"}

@router.post("/profile")
async def create_mentor_profile():
    """멘토 프로필 생성"""
    return {"message": "멘토 프로필 생성 기능이 구현될 예정입니다"}

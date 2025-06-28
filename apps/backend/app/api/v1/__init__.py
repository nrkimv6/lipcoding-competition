"""
API v1 메인 라우터
"""
from fastapi import APIRouter
from app.api.v1 import auth, users, mentors, matches

api_router = APIRouter()

# 각 기능별 라우터 포함
api_router.include_router(auth.router, prefix="/auth", tags=["인증"])
api_router.include_router(users.router, prefix="/users", tags=["사용자"])
api_router.include_router(mentors.router, prefix="/mentors", tags=["멘토"])
api_router.include_router(matches.router, prefix="/matches", tags=["매칭"])

"""
인증 관련 API 엔드포인트
"""
from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from app.database import get_db

router = APIRouter()

@router.post("/login")
async def login():
    """사용자 로그인"""
    return {"message": "로그인 기능이 구현될 예정입니다"}

@router.post("/register")
async def register():
    """사용자 회원가입"""
    return {"message": "회원가입 기능이 구현될 예정입니다"}

@router.post("/logout")
async def logout():
    """사용자 로그아웃"""
    return {"message": "로그아웃 기능이 구현될 예정입니다"}

"""
사용자 관리 API 엔드포인트
"""
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from sqlalchemy import text
from app.database import get_db

router = APIRouter()

@router.get("/")
async def get_users():
    """사용자 목록 조회"""
    return {"users": [], "message": "사용자 목록을 조회합니다"}

@router.get("/profile")
async def get_profile():
    """현재 사용자 프로필 조회"""
    return {"message": "프로필 조회 기능이 구현될 예정입니다"}

@router.put("/profile")
async def update_profile():
    """사용자 프로필 업데이트"""
    return {"message": "프로필 업데이트 기능이 구현될 예정입니다"}

@router.get("/db-test")
async def test_database(db: Session = Depends(get_db)):
    """데이터베이스 연결 테스트 엔드포인트"""
    try:
        # 사용자 수 조회
        result = db.execute(text("SELECT COUNT(*) FROM users"))
        user_count = result.scalar()
        
        # 테이블 목록 조회
        result = db.execute(text("""
            SELECT table_name 
            FROM information_schema.tables 
            WHERE table_schema = 'public'
            ORDER BY table_name
        """))
        tables = [row[0] for row in result.fetchall()]
        
        return {
            "status": "success",
            "message": "데이터베이스 연결 성공",
            "user_count": user_count,
            "tables": tables
        }
    except Exception as e:
        return {
            "status": "error",
            "message": f"데이터베이스 연결 실패: {str(e)}"
        }

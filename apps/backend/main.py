from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from contextlib import asynccontextmanager

@asynccontextmanager
async def lifespan(app: FastAPI):
    # 애플리케이션 시작 시 실행
    print("Starting MM Matching API...")
    yield
    # 애플리케이션 종료 시 실행
    print("Shutting down MM Matching API...")

app = FastAPI(
    title="MM Matching API",
    description="멘토-멘티 매칭 서비스 API",
    version="1.0.0",
    lifespan=lifespan
)

# CORS 설정
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],  # Next.js 개발 서버
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
async def root():
    return {"message": "MM Matching API에 오신 것을 환영합니다!"}

@app.get("/health")
async def health_check():
    return {"status": "healthy", "service": "mm-matching-api"}

# API 라우터 그룹들
@app.get("/api/v1/mentors")
async def get_mentors():
    return {"mentors": [], "message": "멘토 목록을 조회합니다"}

@app.get("/api/v1/mentees")
async def get_mentees():
    return {"mentees": [], "message": "멘티 목록을 조회합니다"}

@app.post("/api/v1/matching")
async def create_matching():
    return {"message": "매칭이 생성되었습니다"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)

"""
간단한 테스트 서버 - 문제 파악용
"""
from fastapi import FastAPI
import uvicorn

app = FastAPI(title="Test Server")

@app.get("/")
async def root():
    return {"message": "Test server is running!"}

@app.post("/api/signup")
async def signup():
    return {"message": "Signup endpoint working"}

@app.post("/api/v1/auth/register")
async def register():
    return {"message": "Register endpoint working"}

if __name__ == "__main__":
    print("Starting simple test server...")
    uvicorn.run(app, host="0.0.0.0", port=8080)

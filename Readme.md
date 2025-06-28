# 앱 제출 자료 📋

**천하제일 입코딩대회: 멘토-멘티 매칭 앱 개발**

## 📋 앱 제출자 정보

### 제목
천하제일 입코딩대회: 멘토-멘티 매칭 앱 개발

### 참가자 이름
[여기에 참가자 이름 입력]

### GitHub 프로필 URL
[여기에 GitHub 프로필 URL 입력]
예: https://github.com/your-username

### GitHub 리포지토리 URL
[여기에 리포지토리 URL 입력]
예: https://github.com/your-username/mm-matching-app

### 스크린샷 URL
[여기에 앱 스크린샷 URL 입력]
예: https://github.com/your-username/mm-matching-app/blob/main/screenshot.png?raw=true

### 소개 동영상 URL
[여기에 소개 동영상 URL 입력]
예: https://www.youtube.com/watch?v=IUY0TJEwnGA

---

## 🎨 프론트엔드 앱 정보

### 프론트엔드 앱 기본 URL
✅ **프론트엔드 앱 기본 URL은 `http://localhost:3000`입니다.**

### 프론트엔드 앱 경로
```
./apps/frontend
```

### 프론트엔드 앱 실행 명령어
```bash
npm install && npm run dev &
```

**상세 실행 단계:**
```bash
# 1. 프론트엔드 디렉토리로 이동
cd apps/frontend

# 2. 의존성 설치
npm install

# 3. 개발 서버 실행 (백그라운드)
npm run dev &
```

---

## ⚙️ 백엔드 앱 정보

### 백엔드 앱 기본 URL
✅ **백엔드 앱 기본 URL은 `http://localhost:8080/api`입니다.**

### 백엔드 앱 경로
```
./apps/backend
```

### 백엔드 앱 실행 명령어
```bash
python -m venv venv && source venv/bin/activate && pip install -r requirements.txt && python -m uvicorn app.main:app --reload --host 0.0.0.0 --port 8080 &
```

**상세 실행 단계:**
```bash
# 1. 백엔드 디렉토리로 이동
cd apps/backend

# 2. 가상환경 생성 (Linux/MacOS)
python -m venv venv

# 3. 가상환경 활성화
source venv/bin/activate

# 4. 의존성 설치
pip install -r requirements.txt

# 5. 서버 실행 (백그라운드)
python -m uvicorn app.main:app --reload --host 0.0.0.0 --port 8080 &
```

### Swagger UI URL
```
http://localhost:8080/docs
```

### OpenAPI 문서 URL
```
http://localhost:8080/openapi.json
```

---

## 🛠️ 추가 설정 정보

### 환경 요구사항
- **Node.js**: 17+ 
- **Python**: 3.9+
- **PostgreSQL**: 14+ (또는 SQLite 사용 가능)

### 데이터베이스 설정
```bash
# PostgreSQL 사용 시
export PGPASSWORD="your_password"
psql -U postgres -c "CREATE DATABASE mm_matching;"

# 또는 SQLite 사용 (개발용)
# DATABASE_URL=sqlite:///./mm_matching.db
```

### 주요 API 엔드포인트
- **인증**: `/api/v1/auth/register`, `/api/v1/auth/login`
- **사용자**: `/api/v1/users/profile`
- **멘토**: `/api/v1/mentors/`
- **매칭**: `/api/v1/matches/request`

---

## 📸 스크린샷 가이드

앱 스크린샷에 포함되어야 할 화면들:

1. **메인 페이지** - 앱 소개 및 로그인 버튼
2. **회원가입 페이지** - 멘토/멘티 역할 선택
3. **로그인 페이지** - 이메일/비밀번호 입력
4. **대시보드** - 사용자별 맞춤 화면
5. **멘토 목록** - 기술 스택별 필터링
6. **매칭 요청** - 멘티가 멘토에게 요청
7. **Swagger UI** - API 문서 화면

---

## 🎥 소개 동영상 가이드

동영상에 포함할 내용:

1. **앱 개요 소개** (30초)
   - 멘토-멘티 매칭 서비스 설명
   - 주요 기능 소개

2. **사용자 등록 및 로그인** (1분)
   - 회원가입 과정 (멘토/멘티 선택)
   - 로그인 과정

3. **핵심 기능 시연** (2분)
   - 멘토 검색 및 필터링
   - 매칭 요청 생성
   - 멘토의 요청 수락/거절

4. **API 문서 확인** (30초)
   - Swagger UI 화면
   - 주요 엔드포인트 설명

**총 예상 시간**: 4분 내외

---

## ✅ 제출 전 체크리스트

- [ ] GitHub 리포지토리 public 설정
- [ ] README.md 파일 작성 (설치 및 실행 가이드)
- [ ] 스크린샷 파일 리포지토리에 업로드
- [ ] 소개 동영상 제작 및 업로드
- [ ] 프론트엔드/백엔드 정상 실행 확인
- [ ] API 문서 접근 가능 확인
- [ ] 데이터베이스 연결 및 초기 데이터 확인

---

## 🚨 중요 참고사항

1. **포트 설정**: 
   - 제출 템플릿과 동일하게 `8080` 포트 사용 ✅
   - API 경로: `/api/v1/` ✅

2. **백그라운드 실행**: 
   - 명령어 끝에 `&` 추가하여 백그라운드 실행

3. **환경 설정**: 
   - Linux/Unix 환경 기준 명령어
   - GitHub Actions에서 자동 테스트 실행

4. **데이터베이스**: 
   - PostgreSQL 권장, SQLite도 지원
   - `.env` 파일에서 DATABASE_URL 설정

5. **Python 가상환경**:
   - `python -m venv venv` (Linux/MacOS)
   - `source venv/bin/activate` (Linux/MacOS)

---

## 🔧 GitHub Actions 설정 예시

### 환경변수 (.env 파일)
```bash
# 데이터베이스 설정
DATABASE_URL=postgresql://postgres:password@localhost:5432/mm_matching

# JWT 설정  
SECRET_KEY=your-secret-key-here
ALGORITHM=HS256
ACCESS_TOKEN_EXPIRE_MINUTES=1440

# CORS 설정
ALLOWED_ORIGINS=["http://localhost:3000"]
```

### GitHub Actions Workflow
```yaml
name: Test MM Matching App

on: [push, pull_request]

jobs:
  test:
    runs-on: ubuntu-latest
    
    services:
      postgres:
        image: postgres:14
        env:
          POSTGRES_PASSWORD: password
          POSTGRES_DB: mm_matching
          POSTGRES_USER: postgres
        ports:
          - 5432:5432
        options: >-
          --health-cmd pg_isready
          --health-interval 10s
          --health-timeout 5s
          --health-retries 5

    steps:
    - uses: actions/checkout@v3
    
    - name: Setup Node.js
      uses: actions/setup-node@v3
      with:
        node-version: '18'
        
    - name: Setup Python
      uses: actions/setup-python@v4
      with:
        python-version: '3.9'
    
    - name: Wait for PostgreSQL
      run: |
        until pg_isready -h localhost -p 5432 -U postgres; do
          echo "Waiting for PostgreSQL..."
          sleep 2
        done
        
    - name: Create Database
      env:
        PGPASSWORD: password
      run: |
        psql -h localhost -U postgres -c "CREATE DATABASE mm_matching;" || true
    
    - name: Start Backend
      env:
        DATABASE_URL: postgresql://postgres:password@localhost:5432/mm_matching
        SECRET_KEY: test-secret-key-for-github-actions
        PYTHONPATH: /home/runner/work/lipcoding-competition/lipcoding-competition/apps/backend
        PORT: 8080
        HOST: 0.0.0.0
        DEBUG: false
      run: |
        cd apps/backend
        echo "Creating virtual environment..."
        python -m venv venv
        echo "Activating virtual environment..."
        source venv/bin/activate
        echo "Installing requirements..."
        pip install -r requirements.txt
        echo "Starting uvicorn server..."
        nohup python -m uvicorn app.main:app --host 0.0.0.0 --port 8080 --log-level info > server.log 2>&1 &
        echo "Waiting for server to start..."
        sleep 15
        echo "Server log:"
        cat server.log || echo "No log file found"
        
    - name: Check Backend Status
      run: |
        echo "Checking if backend is running..."
        for i in {1..30}; do
          if curl -f http://localhost:8080/ping; then
            echo "✅ Backend is running!"
            break
          else
            echo "⏳ Attempt $i: Backend not ready yet..."
            sleep 2
          fi
          if [ $i -eq 30 ]; then
            echo "❌ Backend failed to start"
            echo "=== Server Log ==="
            cat apps/backend/server.log || echo "No server log found"
            echo "=== Port Status ==="
            netstat -tlnp | grep :8080 || echo "Port 8080 not in use"
            echo "=== Process Status ==="
            ps aux | grep uvicorn || echo "No uvicorn process found"
            exit 1
          fi
        done
        
    - name: Start Frontend
      run: |
        cd apps/frontend && npm install && npm run dev &
        sleep 10
```

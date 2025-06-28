# MM Matching App 🎯

**멘토-멘티 매칭 서비스** - 멘토와 멘티를 효율적으로 연결해주는 웹 애플리케이션

## 📁 프로젝트 구조 (모노레포)

```
mm-matching-app/
├── apps/
│   ├── frontend/          # Next.js 14 + TypeScript + Tailwind CSS
│   └── backend/           # FastAPI + SQLAlchemy + PostgreSQL  
├── packages/              # 공통 코드 패키지 (TypeScript)
├── db/                    # 데이터베이스 스키마 및 마이그레이션
├── comp-rule/             # 대회 규정 및 기술 문서
└── docker-compose.yml     # 개발 환경 컨테이너 설정
```

## 🚀 주요 기능

### 🔐 인증 & 프로필 관리
- **회원가입/로그인**: JWT 기반 인증 시스템
- **역할 선택**: 멘토 또는 멘티로 가입
- **프로필 관리**: 개인정보, 기술 스택, 프로필 이미지 관리

### 🔍 멘토 찾기 & 매칭
- **멘토 검색**: 기술 스택별 필터링 및 정렬
- **매칭 요청**: 멘티가 멘토에게 요청 전송
- **요청 관리**: 멘토의 수락/거절 시스템
- **1:1 매칭**: 한 명의 멘토당 하나의 활성 매칭

### 📊 대시보드
- **요청 현황**: 보낸/받은 요청 상태 관리
- **매칭 상태**: 현재 매칭 진행 상황

## 🛠️ 기술 스택

### Frontend (Next.js)
- **Framework**: Next.js 14.2.30 (App Router)
- **Language**: TypeScript 5.x
- **Styling**: Tailwind CSS 3.4
- **Development**: ESLint + Prettier + TypeScript ESLint

### Backend (FastAPI)  
- **Framework**: FastAPI 0.104.1
- **Database**: PostgreSQL 17 + SQLAlchemy 2.0
- **Authentication**: JWT (python-jose)
- **Password**: bcrypt (passlib)
- **Testing**: pytest + httpx

### 공통 패키지
- **Type System**: Zod 스키마 검증
- **Testing**: Jest + TypeScript
- **Utils**: 공통 유틸리티 함수

### 인프라
- **Database**: PostgreSQL 17
- **Containerization**: Docker Compose
- **Cache**: Redis (선택사항)

## 📋 개발 진행 상황

### ✅ 완료된 작업
- [x] **프로젝트 구조 설정** - 모노레포 구조 및 워크스페이스 구성
- [x] **Frontend 환경 구축** - Next.js 14 + TypeScript + Tailwind CSS
- [x] **Backend 환경 구축** - FastAPI + SQLAlchemy + PostgreSQL 드라이버
- [x] **Backend 폴더 구조 개선** - FastAPI 모범 사례에 따른 모듈화 구조 🆕
- [x] **공통 패키지 설정** - TypeScript 타입 시스템 및 유틸리티
- [x] **데이터베이스 스키마** - 사용자, 멘토 프로필, 매칭 테이블 설계
- [x] **개발 도구 설정** - ESLint, Prettier, TypeScript 설정
- [x] **Docker 환경 설정** - PostgreSQL, Redis 컨테이너 구성
- [x] **Git 저장소 관리** - 초기 커밋 및 버전 관리 설정

### 🔄 진행 중인 작업
- [x] **데이터베이스 연결** - Backend와 PostgreSQL 연동 테스트 ✅ 완료
- [x] **Backend 구조 개선** - FastAPI 모범 사례 적용 및 모듈화 ✅ 완료
- [x] **Import 구문 검증** - 모든 모듈 정상 작동 및 서버 실행 확인 ✅ 완료
- [ ] **API 엔드포인트 구현** - 사용자 인증, 프로필, 매칭 API (기본 골격 완료 🆕)
- [ ] **Frontend UI 개발** - 로그인, 회원가입, 대시보드 페이지
- [ ] **이미지 업로드** - 프로필 이미지 업로드 기능

### 📝 향후 계획
- [ ] **API 문서화** - FastAPI 자동 문서 생성 설정
- [ ] **테스트 코드** - 단위 테스트 및 통합 테스트 작성  
- [ ] **배포 환경** - CI/CD 파이프라인 구성
- [ ] **성능 최적화** - 캐싱, 데이터베이스 인덱싱

## 🚦 빠른 시작

### 필수 요구사항
- **Node.js** 17+ ✅ 
- **Python** 3.9+ ✅
- **PostgreSQL** 17 ✅
- **Git** ✅

### 개발 환경 설정

1. **저장소 클론 및 의존성 설치**
```bash
# Frontend 의존성 설치
cd apps/frontend
npm install

# Backend 가상환경 및 의존성 설치  
cd ../backend
python -m venv venv
venv\Scripts\activate  # Windows
pip install -r requirements.txt
```

2. **데이터베이스 설정**
```sql
-- PostgreSQL에서 데이터베이스 생성
CREATE DATABASE mm_matching;
```

```bash
# 스키마 적용
cd ../../db
psql -U postgres -d mm_matching -f init.sql
psql -U postgres -d mm_matching -f seed.sql
```

3. **서비스 실행**
```bash
# Frontend (포트 3000)
cd apps/frontend
npm run dev

# Backend (포트 8000)  
cd apps/backend
venv\Scripts\activate
uvicorn main:app --reload
```

### 🔍 API 문서
Backend 실행 후 [http://localhost:8000/docs](http://localhost:8000/docs)에서 Swagger UI 확인

## 🛠️ 개발 참고사항 & 트러블슈팅

### 🐍 Python 가상환경 관리

#### 가상환경 활성화 확인
```bash
# 가상환경이 활성화되었는지 확인 (프롬프트에 (venv) 표시)
# Windows PowerShell
venv\Scripts\activate

# 활성화된 Python 경로 확인
where python
# 출력 예: D:\mm-matching-app\apps\backend\venv\Scripts\python.exe
```

#### pip 경로 명시 사용법
```bash
# 문제: 가상환경에서 pip 설치가 안 될 때
# 해결: 가상환경의 pip 경로를 직접 명시

# 방법 1: 상대경로 사용
venv\Scripts\pip install sqlalchemy psycopg2-binary python-dotenv

# 방법 2: 절대경로 사용 (확실한 방법)
D:\mm-matching-app\apps\backend\venv\Scripts\pip install -r requirements.txt

# 패키지 설치 확인
venv\Scripts\pip list
```

#### 패키지 설치 문제 해결
```bash
# 1. 개별 패키지 설치 (requirements.txt 실패 시)
venv\Scripts\pip install fastapi uvicorn sqlalchemy psycopg2-binary python-dotenv

# 2. 캐시 클리어 후 재설치
venv\Scripts\pip install --no-cache-dir -r requirements.txt

# 3. pip 업그레이드
venv\Scripts\pip install --upgrade pip
```

### 💾 PostgreSQL 연결 관리

#### 환경변수 설정 방법
```bash
# PowerShell에서 PostgreSQL 비밀번호 설정
$env:PGPASSWORD="102030"
$env:PGCLIENTENCODING="UTF8"

# 데이터베이스 연결 (비밀번호 입력 없이)
psql -U postgres -d mm_matching

# 한 줄로 실행
$env:PGPASSWORD="102030"; $env:PGCLIENTENCODING="UTF8"; psql -U postgres -d mm_matching
```

#### 데이터베이스 상태 확인
```bash
# 테이블 목록 확인
psql -U postgres -d mm_matching -c "\dt"

# 사용자 데이터 확인
psql -U postgres -d mm_matching -c "SELECT COUNT(*) FROM users;"

# 데이터베이스 재생성 (초기화)
$env:PGPASSWORD="102030"; psql -U postgres -c "DROP DATABASE IF EXISTS mm_matching;"
$env:PGPASSWORD="102030"; psql -U postgres -c "CREATE DATABASE mm_matching;"
```

### 🚀 서비스 실행 & 디버깅

#### Backend 실행 방법
```bash
# 방법 1: uvicorn 직접 실행
cd apps/backend
venv\Scripts\activate
uvicorn main:app --reload --host 0.0.0.0 --port 8000

# 방법 2: Python으로 실행
python main.py

# 방법 3: 디버그 모드 (상세한 로그)
uvicorn main:app --reload --log-level debug
```

#### API 테스트 엔드포인트
```bash
# 기본 연결 테스트
curl http://localhost:8000/

# 헬스체크
curl http://localhost:8000/health

# 데이터베이스 연결 테스트
curl http://localhost:8000/api/v1/db-test
```

### 📦 패키지 관리

#### requirements.txt 관리
```bash
# 현재 설치된 패키지 확인
venv\Scripts\pip list

# requirements.txt 업데이트
venv\Scripts\pip freeze > requirements.txt

# 특정 패키지 버전 확인
venv\Scripts\pip show sqlalchemy
```

#### 자주 사용하는 개발 패키지
```txt
# 필수 패키지
fastapi==0.104.1
uvicorn[standard]==0.24.0
sqlalchemy==2.0.23
psycopg2-binary==2.9.9
python-dotenv==1.0.0

# 개발 도구
pytest==7.4.3
black==23.11.0
isort==5.12.0
```

### 🔧 개발 환경 점검 체크리스트

```bash
# 1. Python 환경 확인
python --version  # Python 3.9+ 필요

# 2. 가상환경 활성화 확인
echo $env:VIRTUAL_ENV  # 가상환경 경로 출력되어야 함

# 3. PostgreSQL 서비스 확인
Get-Service postgresql*  # 서비스 실행 상태 확인

# 4. 포트 사용 확인
netstat -an | findstr :8000  # Backend 포트
netstat -an | findstr :3000  # Frontend 포트
netstat -an | findstr :5432  # PostgreSQL 포트
```

### ⚠️ 자주 발생하는 문제 & 해결책

| 문제 | 원인 | 해결책 |
|------|------|--------|
| `ModuleNotFoundError: No module named 'sqlalchemy'` | 가상환경에 패키지 미설치 | `venv\Scripts\pip install sqlalchemy` |
| `FATAL: password authentication failed` | PostgreSQL 비밀번호 오류 | `$env:PGPASSWORD="102030"` 설정 |
| `Port 8000 is already in use` | 포트 충돌 | 기존 프로세스 종료 또는 다른 포트 사용 |
| `Connection refused` | PostgreSQL 서비스 중단 | `Start-Service postgresql*` |
| pip 설치 실패 | 권한 또는 경로 문제 | 가상환경 pip 절대경로 사용 |

### 💡 개발 팁

1. **환경변수 자동 설정**: `.bashrc` 또는 PowerShell 프로필에 자주 사용하는 환경변수 등록
2. **자동 활성화**: VS Code에서 Python 인터프리터를 가상환경으로 설정하면 터미널에서 자동 활성화
3. **데이터베이스 백업**: 개발 중 데이터 손실 방지를 위한 정기적인 덤프 생성
4. **로그 모니터링**: `--log-level debug` 옵션으로 상세한 로그 확인

---

## 🗄️ 데이터베이스 스키마

### 주요 테이블
- **users**: 사용자 기본 정보 (이메일, 역할, 인증)
- **mentor_profiles**: 멘토 상세 정보 (경력, 전문 분야, 가용성)  
- **matches**: 매칭 요청 및 상태 관리
- **sessions**: 사용자 세션 관리

### ERD
```
users (1) ──→ (0..1) mentor_profiles
users (1) ──→ (0..n) matches (멘티 요청)
users (1) ──→ (0..n) matches (멘토 응답)
```

## � 환경 상태 (2025-06-28)

### ✅ 설치 완료
- **Node.js** v23.10.0, npm 10.9.2
- **Python** 3.13.5 (가상환경 구성됨)
- **PostgreSQL** 17 (서비스 실행 중)
- **Git** 저장소 초기화 완료

### 🏗️ 구축 완료
- **Frontend**: Next.js 14 + React 18 + TypeScript + Tailwind CSS
  - 패키지 의존성 386개 설치 완료
  - ESLint + Prettier 개발 도구 설정 완료
  - 개발 서버 정상 작동 (포트 3000)

- **Backend**: FastAPI + SQLAlchemy + PostgreSQL 드라이버
  - Python 가상환경 및 의존성 설치 완료
  - API 서버 정상 작동 (포트 8000)
  - JWT 인증, 비밀번호 암호화 설정

- **Database**: PostgreSQL 17 데이터베이스 설정 완료 ✅
  - `mm_matching` 데이터베이스 생성 완료
  - 4개 테이블 생성: users, mentor_profiles, mentee_profiles, matchings
  - 초기 데이터 삽입 완료 (사용자 5명)

## 📋 초기 세팅 진행 체크리스트

### ✅ 완료된 세팅
- [x] 1. `apps/frontend`에서 Next.js 프로젝트 생성
- [x] 2. `apps/backend`에서 FastAPI 프로젝트 생성  
- [x] 3. `db/`에 PostgreSQL 관련 스크립트 및 마이그레이션 관리
- [x] 4. `packages/`에 공통 코드 패키지 초기화
- [x] 5. 환경 설정 파일(.env) 생성
- [x] 6. Docker 설정 (docker-compose.yml)
- [x] 7. 개발 도구 설정 (ESLint, Prettier, pre-commit hooks)
- [ ] 8. API 문서화 설정
- [ ] 9. 테스트 환경 구축
- [ ] 10. CI/CD 파이프라인 구성

### ⚠️ 해결 필요 사항

#### 1. PowerShell 실행 정책 (우선순위: 높음)
- [x] PowerShell 실행 정책 RemoteSigned로 설정 완료

#### 2. Backend Python 환경 설정 (우선순위: 높음)  
- [x] Python 3.13.5 설치 확인
- [x] 가상환경 생성 및 활성화 완료
- [x] requirements.txt 의존성 설치 완료

#### 3. Git 저장소 관리
- [x] Git 저장소 초기화 완료
- [x] .gitignore 파일 설정 완료
- [x] 초기 커밋 생성 완료 (커밋 해시: ab3367a, 74afc7f)
- [ ] GitHub 원격 저장소 연결

#### 4. 서비스 실행 테스트 
- [x] Frontend: `npm run dev` (포트 3000) - 정상 작동 확인
- [x] Backend: `uvicorn main:app --reload` (포트 8000) - 정상 작동 확인
- [x] Database: PostgreSQL 연결 및 스키마 적용 완료

#### 5. 보안 취약점 해결
- [x] Frontend 보안 취약점 해결 완료 (`npm audit fix` 실행됨)

#### 6. Docker 환경 설정 (현재 미사용)
- ⚠️ **Docker Desktop 미설치**: Redis 컨테이너 실행 불가 (PostgreSQL은 로컬 설치 사용)
- **대안**: Redis 로컬 설치 또는 Docker Desktop 설치 필요
- 현재는 개발 환경에서 로컬 PostgreSQL 17 사용 (정상 작동)

#### 7. PostgreSQL 데이터베이스 설정 ✅ 완료
- [x] PostgreSQL 17 설치 완료
- [x] PostgreSQL 서비스 시작 완료 (postgresql-x64-17)
- [x] mm_matching 데이터베이스 생성 완료
- [x] init.sql 스크립트 실행 (테이블 생성) 완료
- [x] seed.sql 스크립트 실행 (초기 데이터 삽입) 완료
- [x] Backend에서 데이터베이스 연결 테스트 ✅ 완료

### 💡 다음 단계 권장사항 (Node.js 17, PostgreSQL 17 이미 설치된 환경)
1. [x] **Node.js 환경 확인** - 이미 설치 완료 (v23.10.0)
2. [x] **PostgreSQL 환경 확인** - 이미 설치 완료 (v17, 서비스 실행 중)
3. [x] **프론트엔드 의존성 설치** - `cd apps/frontend && npm install`
4. [x] **Python 가상환경 설정 및 의존성 설치** 완료
5. [x] **Git 저장소 초기화 및 초기 커밋** 완료
6. [ ] ~~GitHub 원격 저장소 연결~~ (보류)
7. [x] **PostgreSQL 데이터베이스 설정** - 완료 ✅
8. [x] **Backend 데이터베이스 연결 테스트** - 완료 ✅
9. [ ] **각 서비스 간 연동 테스트** (API 통신) ⬅️ **다음 우선순위**
10. [ ] **API 엔드포인트 구현** (사용자 인증, 프로필, 매칭)
11. [ ] **Frontend UI 개발** (로그인, 대시보드, 매칭 페이지)

### ✅ 해결 완료
- [x] **데이터베이스 초기화**: `mm_matching` DB 생성 및 스키마 적용 완료
- [x] **Backend 데이터베이스 연결**: SQLAlchemy 연결 및 테스트 완료
- [ ] **환경 변수 설정**: Backend DB 연결 정보 구성
- [ ] **Docker 환경**: Redis 컨테이너 설정 (선택사항)

## 🎯 개발 가이드

### 코드 스타일
```bash
# Frontend
npm run lint        # ESLint 검사
npm run format      # Prettier 포맷팅

# Backend  
python -m pytest   # 테스트 실행
```

### 브랜치 전략
- `main`: 프로덕션 브랜치
- `develop`: 개발 통합 브랜치  
- `feature/*`: 기능 개발 브랜치

### 커밋 컨벤션
```
feat: 새로운 기능 추가
fix: 버그 수정
docs: 문서 수정
style: 코드 포맷팅
refactor: 코드 리팩토링
test: 테스트 추가/수정
```

## 📚 참고 문서
- [요구사항 명세서](./comp-rule/mentor-mentee-app-requirements.md)
- [사용자 스토리](./comp-rule/mentor-mentee-app-user-stories.md)
- [API 스펙](./comp-rule/mentor-mentee-api-spec.md)
- [개발 규칙](./my-rule)

---

## 🛟 트러블슈팅

### 일반적인 문제
1. **포트 충돌**: 3000, 8000 포트가 사용 중인 경우
2. **PostgreSQL 연결 실패**: 서비스 상태 및 포트 확인
3. **Node.js 의존성 오류**: `npm ci` 또는 `npm install --force`

### 데이터베이스 재설정
```bash
# PostgreSQL 재설정
dropdb mm_matching
createdb mm_matching
psql -U postgres -d mm_matching -f db/init.sql
```

---

## 🧪 테스트 구조

### 📁 테스트 폴더 구조
```
tests/
├── backend/                  # 🐍 Backend 테스트
│   ├── conftest.py          # pytest 설정 및 픽스처
│   ├── unit/                # 단위 테스트
│   │   ├── test_api.py      # API 엔드포인트 테스트
│   │   └── test_models.py   # 데이터베이스 모델 테스트
│   ├── integration/         # 통합 테스트
│   │   ├── test_db_connection.py      # DB 연결 및 CRUD 테스트
│   │   └── test_api_integration.py    # API 워크플로우 테스트
│   └── utils/               # 테스트 유틸리티
│       ├── db_utils.py      # DB 테스트 헬퍼
│       └── fixtures.py      # 테스트 데이터
├── frontend/                # ⚛️ Frontend 테스트 (예정)
└── e2e/                     # 🔄 End-to-End 테스트 (예정)
```

### 🏃 테스트 실행 방법

#### Windows (PowerShell/CMD)
```bash
# 모든 테스트 실행
run_tests.bat all

# 단위 테스트만 실행
run_tests.bat unit

# 통합 테스트만 실행  
run_tests.bat integration

# 백엔드 전체 테스트
run_tests.bat backend

# 기존 테스트 (호환성)
run_tests.bat legacy

# 데이터베이스 연결만 체크
run_tests.bat db-check
```

#### 직접 pytest 실행
```bash
# 가상환경 활성화 필요
apps\backend\venv\Scripts\activate

# 전체 테스트
python -m pytest tests/ -v

# 특정 테스트 파일
python -m pytest tests/backend/unit/test_api.py -v

# 특정 테스트 함수
python -m pytest tests/backend/unit/test_api.py::test_health_check -v

# 마커별 테스트
python -m pytest -m "unit" -v          # 단위 테스트만
python -m pytest -m "integration" -v   # 통합 테스트만
python -m pytest -m "db" -v           # DB 관련 테스트만
```

### 📊 테스트 현황
- ✅ **pytest 환경 구성 완료** - conftest.py, pytest.ini 설정
- ✅ **기본 API 테스트** - health check, 기본 엔드포인트
- ✅ **데이터베이스 연결 테스트** - PostgreSQL 연결 및 CRUD 검증
- ✅ **테스트 유틸리티** - DB 헬퍼, 픽스처, 샘플 데이터
- 🔄 **API 통합 테스트** - 인증, 매칭 워크플로우 (예정)
- 🔄 **모델 단위 테스트** - SQLAlchemy 모델 검증 (예정)

---

## 🧹 폴더 정리 완료

#### ✅ 정리된 항목
- **폴더 구조 개선**: FastAPI 모범 사례에 따른 모듈화 구조 적용 🆕
- **API 라우터 분리**: 인증, 사용자, 멘토, 매칭별 라우터 분리 🆕
- **스키마 모듈화**: 도메인별 Pydantic 스키마 분리 🆕
- **설정 관리**: 중앙화된 설정 파일 구성 🆕
- **백업 폴더 정리**: .old 파일들을 backup 폴더로 이동 🆕
- **conf 폴더 생성**: 설정 관련 파일 분리 (.env.example) 🆕
- **Import 구문 검증**: 모든 모듈 import 정상 작동 확인 🆕
- **기존 테스트 파일 제거**: `apps/backend/test_*.py` 파일들을 새로운 구조로 마이그레이션
- **독립 스크립트 분리**: `scripts/db_check.py` - 스탠드얼론 DB 연결 테스트 도구
- **중복 제거**: 동일한 기능의 테스트 코드 통합 및 정리

#### 📂 현재 백엔드 폴더 구조
```
apps/backend/
├── app/                    # 메인 애플리케이션 패키지 🆕
│   ├── __init__.py        # 패키지 초기화
│   ├── main.py            # FastAPI 앱 인스턴스
│   ├── config.py          # 설정 관리 🆕
│   ├── database.py        # DB 연결 설정
│   ├── dependencies.py    # 공통 의존성 (예정)
│   ├── api/               # API 라우터 🆕
│   │   ├── __init__.py
│   │   └── v1/           # API 버전 1
│   │       ├── __init__.py
│   │       ├── auth.py   # 인증 관련 API 🆕
│   │       ├── users.py  # 사용자 관리 API 🆕
│   │       ├── mentors.py # 멘토 관리 API 🆕
│   │       └── matches.py # 매칭 관리 API 🆕
│   ├── models/            # SQLAlchemy 모델 (예정) 🆕
│   │   └── __init__.py
│   ├── schemas/           # Pydantic 스키마 🆕
│   │   ├── __init__.py
│   │   ├── common.py     # 공통 스키마 (Enum) 🆕
│   │   ├── user.py       # 사용자 스키마 🆕
│   │   ├── mentor.py     # 멘토 스키마 🆕
│   │   └── match.py      # 매칭 스키마 🆕
│   ├── services/          # 비즈니스 로직 (예정) 🆕
│   │   └── __init__.py
│   └── utils/            # 유틸리티 함수 (예정) 🆕
│       └── __init__.py
├── backup/               # 백업 파일 🆕
│   ├── database.py.old   # 기존 DB 설정 백업
│   └── schemas.py.old    # 기존 스키마 백업
├── conf/                 # 설정 파일 🆕
│   └── .env.example      # 환경변수 예제
├── scripts/              # 관리 스크립트 🆕
│   └── db_check.py      # DB 연결 테스트 도구
├── main.py              # 앱 실행 진입점
├── requirements.txt     # Python 의존성
├── .env                 # 환경변수
└── venv/               # 가상환경
```

#### 🧪 새로운 테스트 구조
```
tests/backend/
├── conftest.py         # pytest 설정
├── unit/              # 단위 테스트 (10개)
├── integration/       # 통합 테스트 (7개)
└── utils/             # 테스트 유틸리티
```

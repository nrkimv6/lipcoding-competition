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
- [x] **공통 패키지 설정** - TypeScript 타입 시스템 및 유틸리티
- [x] **데이터베이스 스키마** - 사용자, 멘토 프로필, 매칭 테이블 설계
- [x] **개발 도구 설정** - ESLint, Prettier, TypeScript 설정
- [x] **Docker 환경 설정** - PostgreSQL, Redis 컨테이너 구성
- [x] **Git 저장소 관리** - 초기 커밋 및 버전 관리 설정

### 🔄 진행 중인 작업
- [x] **데이터베이스 연결** - Backend와 PostgreSQL 연동 테스트 ✅ 완료
- [ ] **API 엔드포인트 구현** - 사용자 인증, 프로필, 매칭 API
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

### 💾 PostgreSQL 연결 방법
```bash
# Windows PowerShell에서 올바른 연결 방법
$env:PGPASSWORD="102030"; $env:PGCLIENTENCODING="UTF8"; psql -U postgres -d mm_matching

# 데이터베이스 재생성이 필요한 경우
$env:PGPASSWORD="102030"; psql -U postgres -c "DROP DATABASE IF EXISTS mm_matching;"
$env:PGPASSWORD="102030"; psql -U postgres -c "CREATE DATABASE mm_matching;"
$env:PGPASSWORD="102030"; $env:PGCLIENTENCODING="UTF8"; psql -U postgres -d mm_matching -f db/init.sql
$env:PGPASSWORD="102030"; $env:PGCLIENTENCODING="UTF8"; psql -U postgres -d mm_matching -f db/seed.sql
```

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

> 💡 **개발 환경 준비 완료!** 이제 API 구현과 UI 개발을 시작할 수 있습니다.

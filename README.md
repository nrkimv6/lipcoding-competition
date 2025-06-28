# MM Matching App 모노레포 구조

- `apps/frontend`: Next.js 프론트엔드
- `apps/backend`: FastAPI 백엔드
- `packages/`: 공통 코드(유틸, 타입 등)
- `db/`: 데이터베이스 마이그레이션 및 초기화 스크립트
- `comp-rule/`: 대회 규정 및 문서

---

## 초기 세팅 가이드

### 진행 체크리스트
- [x] 1. `apps/frontend`에서 Next.js 프로젝트 생성
- [x] 2. `apps/backend`에서 FastAPI 프로젝트 생성  
- [x] 3. `db/`에 PostgreSQL 관련 스크립트 및 마이그레이션 관리
- [x] 4. `packages/`에 공통 코드 패키지 초기화
- [x] 5. 환경 설정 파일(.env) 생성
- [x] 6. Docker 설정 (docker-compose.yml)
- [ ] 7. 개발 도구 설정 (ESLint, Prettier, pre-commit hooks)
- [ ] 8. API 문서화 설정
- [ ] 9. 테스트 환경 구축
- [ ] 10. CI/CD 파이프라인 구성

---

## 환경 검증 결과 (2025-06-28)

### ✅ 정상 동작 확인됨
- **Frontend (Next.js)**: 의존성 설치 완료, 빌드 시스템 정상
  - Node.js v23.10.0, npm 10.9.2
  - React 18, Next.js 14.2.17, TypeScript 5, Tailwind CSS 설치됨
  - 패키지 총 386개 설치 완료

- **Backend (FastAPI)**: 프로젝트 구조 및 설정 완료
  - main.py, schemas.py, requirements.txt 정상 설정
  - FastAPI, SQLAlchemy, PostgreSQL 드라이버 포함

- **공통 패키지**: TypeScript 환경 구성 완료
  - types, utils, constants 모듈 구조화
  - Jest 테스트 환경 설정

- **데이터베이스**: PostgreSQL 스키마 정의 완료
  - users, mentor_profiles, matches 등 테이블 스키마
  - Docker Compose PostgreSQL/Redis 서비스 설정

### ⚠️ 해결 필요 사항

#### 1. PowerShell 실행 정책 (우선순위: 높음)
```powershell
# 관리자 권한으로 실행 필요
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
```

#### 2. Backend Python 환경 설정 (우선순위: 높음)
```bash
# apps/backend 디렉토리에서
python -m venv venv
venv\Scripts\activate  # Windows
pip install -r requirements.txt
```

#### 3. 서비스 실행 테스트 
- [x] Frontend: `npm run dev` (포트 3000) - 정상 작동 확인
- [x] Backend: `uvicorn main:app --reload` (포트 8000) - 정상 작동 확인
- [ ] Database: Docker 미설치로 인해 스킵 (PostgreSQL 로컬 설치 필요)

#### 4. 보안 취약점 해결
- [x] Frontend 보안 취약점 해결 완료 (`npm audit fix` 실행됨)

#### 5. Docker 환경 설정 (현재 미사용)
- ⚠️ **Docker Desktop 미설치**: PostgreSQL 컨테이너 실행 불가
- **대안**: PostgreSQL 로컬 설치 또는 Docker Desktop 설치 필요
- 현재는 개발 환경에서 로컬 PostgreSQL 사용 권장

### 💡 다음 단계 권장사항
1. [x] Python 가상환경 설정 및 의존성 설치 완료
2. [ ] PostgreSQL 로컬 설치 또는 Docker Desktop 설치
3. [ ] 데이터베이스 연결 테스트
4. [ ] 각 서비스 간 연동 테스트 (API 통신)
5. [ ] 개발 도구 설정 진행 (체크리스트 7번)

> PostgreSQL 루트 계정 비밀번호: 102030 (my-rule 참고)

---

자세한 개발 규칙 및 기술 스택은 `my-rule`, `comp-rule` 참고

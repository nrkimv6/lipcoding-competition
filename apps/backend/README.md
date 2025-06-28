# FastAPI Backend

멘토-멘티 매칭 서비스의 백엔드 API 서버입니다.

## 기술 스택

- **FastAPI**: 고성능 웹 프레임워크
- **PostgreSQL**: 데이터베이스
- **SQLAlchemy**: ORM
- **Alembic**: 데이터베이스 마이그레이션
- **Pydantic**: 데이터 검증
- **JWT**: 인증

## 설치 및 실행

### 1. 가상환경 생성 및 활성화
```bash
python -m venv venv
venv\Scripts\activate  # Windows
# source venv/bin/activate  # macOS/Linux
```

### 2. 의존성 설치
```bash
pip install -r requirements.txt
```

### 3. 환경변수 설정
```bash
cp .env.example .env
# .env 파일을 편집하여 실제 값들로 수정
```

### 4. 데이터베이스 설정
```bash
# PostgreSQL이 실행 중인지 확인
# 데이터베이스 생성
createdb mm_matching
```

### 5. 서버 실행
```bash
uvicorn main:app --reload --host 0.0.0.0 --port 8000
```

## API 문서

서버 실행 후 다음 URL에서 API 문서를 확인할 수 있습니다:
- Swagger UI: http://localhost:8000/docs
- ReDoc: http://localhost:8000/redoc

## 테스트

```bash
pytest
```

## 프로젝트 구조

```
apps/backend/
├── main.py              # FastAPI 애플리케이션 진입점
├── schemas.py           # Pydantic 모델들
├── requirements.txt     # Python 의존성
├── .env.example        # 환경변수 예시
├── test_main.py        # 기본 테스트
└── README.md           # 이 파일
```

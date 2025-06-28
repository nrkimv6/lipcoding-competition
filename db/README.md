# Database Management

멘토-멘티 매칭 서비스의 PostgreSQL 데이터베이스 관리 디렉토리입니다.

## 파일 구조

```
db/
├── init.sql          # 데이터베이스 스키마 초기화
├── seed.sql          # 테스트 데이터 삽입
├── setup.sh          # 리눅스/맥용 설정 스크립트
├── setup.bat         # 윈도우용 설정 스크립트
└── README.md         # 이 파일
```

## 데이터베이스 설정

### 사전 요구사항

1. PostgreSQL 설치 및 실행
2. 사용자 계정: `postgres`
3. 비밀번호: `102030` (my-rule 참고)

### 자동 설정 (권장)

**Windows:**
```bash
setup.bat
```

**Linux/macOS:**
```bash
chmod +x setup.sh
./setup.sh
```

### 수동 설정

1. **데이터베이스 생성**
```sql
createdb mm_matching
```

2. **스키마 초기화**
```bash
psql -U postgres -d mm_matching -f init.sql
```

3. **테스트 데이터 삽입** (선택사항)
```bash
psql -U postgres -d mm_matching -f seed.sql
```

## 데이터베이스 스키마

### 주요 테이블

- **users**: 사용자 기본 정보 (멘토/멘티/관리자)
- **mentor_profiles**: 멘토 상세 프로필
- **mentee_profiles**: 멘티 상세 프로필  
- **matchings**: 멘토-멘티 매칭 정보

### 연결 정보

- **Host**: localhost
- **Port**: 5432
- **Database**: mm_matching
- **Username**: postgres
- **Password**: 102030

## 백엔드 연동

백엔드 애플리케이션에서 다음 환경변수를 설정하세요:

```env
DATABASE_URL=postgresql://postgres:102030@localhost:5432/mm_matching
```

## 유용한 명령어

### 데이터베이스 접속
```bash
psql -U postgres -d mm_matching
```

### 테이블 확인
```sql
\dt
```

### 사용자 목록 조회
```sql
SELECT * FROM users;
```

### 매칭 현황 조회
```sql
SELECT 
    u1.name as mentor_name,
    u2.name as mentee_name,
    m.status,
    m.created_at
FROM matchings m
JOIN users u1 ON m.mentor_id = u1.id
JOIN users u2 ON m.mentee_id = u2.id;
```

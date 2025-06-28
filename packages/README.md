# Shared Package

MM Matching App의 공통 코드 패키지입니다. 프론트엔드와 백엔드에서 공통으로 사용하는 타입, 유틸리티, 상수들을 관리합니다.

## 설치

```bash
npm install
```

## 개발

```bash
# TypeScript 컴파일 (watch 모드)
npm run dev

# 빌드
npm run build

# 테스트
npm test

# 린트
npm run lint
npm run lint:fix
```

## 구조

```
packages/
├── src/
│   ├── types/           # TypeScript 타입 정의
│   ├── utils/           # 유틸리티 함수들
│   ├── constants/       # 상수들
│   ├── __tests__/       # 테스트 파일들
│   └── index.ts         # 메인 export
├── dist/                # 컴파일된 파일들
├── package.json
├── tsconfig.json
├── jest.config.js
└── README.md
```

## 주요 Export

### Types
- `User`, `MentorProfile`, `MenteeProfile`, `Matching`
- `UserRole`, `MatchingStatus` enums
- Create/Update 타입들

### Utils
- `isValidEmail()` - 이메일 검증
- `isStrongPassword()` - 비밀번호 강도 검증
- `uniqueArray()` - 배열 중복 제거
- `slugify()` - URL 친화적 문자열 변환
- `formatDate()` - 날짜 포맷팅
- `timeAgo()` - 상대적 시간 표시
- `debounce()`, `throttle()` - 성능 최적화

### Constants
- `HTTP_STATUS` - HTTP 상태 코드
- `API_ENDPOINTS` - API 엔드포인트
- `COMMON_SKILLS` - 일반적인 기술 스택
- `INTEREST_CATEGORIES` - 관심 분야
- `EXPERIENCE_LEVELS` - 경험 레벨

## 사용 예시

### 프론트엔드에서 사용
```typescript
import { User, isValidEmail, API_ENDPOINTS } from '@mm-matching/shared';

const user: User = { /* ... */ };
const isValid = isValidEmail(user.email);
const endpoint = API_ENDPOINTS.USERS.DETAIL(user.id);
```

### 백엔드에서 사용
```python
# Python 백엔드에서는 타입 정의만 참고하고
# 유틸리티는 Python으로 별도 구현
```

## 빌드 및 배포

패키지가 변경되면 다른 앱에서 사용할 수 있도록 빌드해야 합니다:

```bash
npm run build
```

빌드된 파일들은 `dist/` 폴더에 생성되며, 이를 통해 다른 프로젝트에서 import할 수 있습니다.

/**
 * API 응답 관련 상수와 타입들
 */

// HTTP 상태 코드
export const HTTP_STATUS = {
  OK: 200,
  CREATED: 201,
  NO_CONTENT: 204,
  BAD_REQUEST: 400,
  UNAUTHORIZED: 401,
  FORBIDDEN: 403,
  NOT_FOUND: 404,
  CONFLICT: 409,
  INTERNAL_SERVER_ERROR: 500,
} as const;

// API 엔드포인트
export const API_ENDPOINTS = {
  AUTH: {
    LOGIN: '/auth/login',
    LOGOUT: '/auth/logout',
    REGISTER: '/auth/register',
    REFRESH: '/auth/refresh',
    PROFILE: '/auth/profile',
  },
  USERS: {
    LIST: '/users',
    DETAIL: (id: number) => `/users/${id}`,
    CREATE: '/users',
    UPDATE: (id: number) => `/users/${id}`,
    DELETE: (id: number) => `/users/${id}`,
  },
  MENTORS: {
    LIST: '/mentors',
    DETAIL: (id: number) => `/mentors/${id}`,
    PROFILE: (id: number) => `/mentors/${id}/profile`,
  },
  MENTEES: {
    LIST: '/mentees',
    DETAIL: (id: number) => `/mentees/${id}`,
    PROFILE: (id: number) => `/mentees/${id}/profile`,
  },
  MATCHINGS: {
    LIST: '/matchings',
    CREATE: '/matchings',
    DETAIL: (id: number) => `/matchings/${id}`,
    ACCEPT: (id: number) => `/matchings/${id}/accept`,
    REJECT: (id: number) => `/matchings/${id}/reject`,
    COMPLETE: (id: number) => `/matchings/${id}/complete`,
  },
} as const;

// API 응답 타입
export interface ApiResponse<T = unknown> {
  success: boolean;
  data?: T;
  message?: string;
  error?: string;
}

export interface PaginatedResponse<T> {
  data: T[];
  pagination: {
    page: number;
    limit: number;
    total: number;
    totalPages: number;
  };
}

// 에러 타입
export interface ApiError {
  code: string;
  message: string;
  details?: Record<string, unknown>;
}

// 검색 파라미터
export interface SearchParams {
  q?: string; // 검색어
  page?: number;
  limit?: number;
  sortBy?: string;
  sortOrder?: 'asc' | 'desc';
}

// 스킬 및 관심사 상수
export const COMMON_SKILLS = [
  'JavaScript',
  'TypeScript',
  'React',
  'Vue.js',
  'Angular',
  'Node.js',
  'Python',
  'Java',
  'C++',
  'Go',
  'Rust',
  'PHP',
  'Ruby',
  'Swift',
  'Kotlin',
  'SQL',
  'PostgreSQL',
  'MongoDB',
  'Redis',
  'Docker',
  'Kubernetes',
  'AWS',
  'GCP',
  'Azure',
  'Git',
  'Linux',
  'Machine Learning',
  'Data Science',
  'DevOps',
  'UI/UX Design',
] as const;

export const INTEREST_CATEGORIES = [
  '웹개발',
  '모바일개발',
  '백엔드개발',
  '프론트엔드개발',
  '풀스택개발',
  '데이터사이언스',
  '머신러닝',
  '인공지능',
  'DevOps',
  '클라우드',
  '게임개발',
  'UI/UX디자인',
  '블록체인',
  '사이버보안',
  '임베디드',
  'IoT',
] as const;

// 경험 레벨
export const EXPERIENCE_LEVELS = [
  '입문',
  '초급',
  '중급',
  '고급',
  '전문가',
] as const;

export type Skill = typeof COMMON_SKILLS[number];
export type InterestCategory = typeof INTEREST_CATEGORIES[number];
export type ExperienceLevel = typeof EXPERIENCE_LEVELS[number];

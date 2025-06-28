/**
 * 유틸리티 함수들
 */

/**
 * 이메일 형식 검증
 */
export function isValidEmail(email: string): boolean {
  const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
  return emailRegex.test(email);
}

/**
 * 비밀번호 강도 검증
 * 최소 8자, 대소문자, 숫자, 특수문자 포함
 */
export function isStrongPassword(password: string): boolean {
  const minLength = 8;
  const hasUpperCase = /[A-Z]/.test(password);
  const hasLowerCase = /[a-z]/.test(password);
  const hasNumbers = /\d/.test(password);
  const hasSpecialChar = /[!@#$%^&*(),.?":{}|<>]/.test(password);

  return (
    password.length >= minLength &&
    hasUpperCase &&
    hasLowerCase &&
    hasNumbers &&
    hasSpecialChar
  );
}

/**
 * 배열에서 중복 제거
 */
export function uniqueArray<T>(array: T[]): T[] {
  return [...new Set(array)];
}

/**
 * 문자열 슬러그화 (URL 친화적 문자열 변환)
 */
export function slugify(text: string): string {
  return text
    .toLowerCase()
    .trim()
    .replace(/[^\w\s-]/g, '') // 특수문자 제거
    .replace(/[\s_-]+/g, '-') // 공백과 언더스코어를 하이픈으로
    .replace(/^-+|-+$/g, ''); // 앞뒤 하이픈 제거
}

/**
 * 날짜 포맷팅 (YYYY-MM-DD)
 */
export function formatDate(date: Date): string {
  return date.toISOString().split('T')[0];
}

/**
 * 상대적 시간 표시 (예: "2시간 전", "3일 전")
 */
export function timeAgo(date: Date): string {
  const now = new Date();
  const diffInSeconds = Math.floor((now.getTime() - date.getTime()) / 1000);

  const units = [
    { name: '년', seconds: 365 * 24 * 60 * 60 },
    { name: '개월', seconds: 30 * 24 * 60 * 60 },
    { name: '일', seconds: 24 * 60 * 60 },
    { name: '시간', seconds: 60 * 60 },
    { name: '분', seconds: 60 },
    { name: '초', seconds: 1 },
  ];

  for (const unit of units) {
    const count = Math.floor(diffInSeconds / unit.seconds);
    if (count > 0) {
      return `${count}${unit.name} 전`;
    }
  }

  return '방금 전';
}

/**
 * 디바운스 함수
 */
export function debounce<T extends (...args: unknown[]) => void>(
  func: T,
  wait: number
): (...args: Parameters<T>) => void {
  let timeout: NodeJS.Timeout;
  
  return (...args: Parameters<T>) => {
    clearTimeout(timeout);
    timeout = setTimeout(() => func(...args), wait);
  };
}

/**
 * 스로틀 함수
 */
export function throttle<T extends (...args: unknown[]) => void>(
  func: T,
  limit: number
): (...args: Parameters<T>) => void {
  let inThrottle: boolean;
  
  return (...args: Parameters<T>) => {
    if (!inThrottle) {
      func(...args);
      inThrottle = true;
      setTimeout(() => (inThrottle = false), limit);
    }
  };
}

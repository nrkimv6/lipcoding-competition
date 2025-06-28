'use client';

import { useEffect } from 'react';
import { useRouter } from 'next/navigation';

export default function Home() {
  const router = useRouter();

  useEffect(() => {
    // 요구사항: "/" 페이지에서 인증 상태에 따른 자동 리다이렉트
    const token = localStorage.getItem('token');
    
    if (token) {
      // 인증된 사용자는 /profile 페이지로 리다이렉트
      router.push('/profile');
    } else {
      // 인증되지 않은 사용자는 /login 페이지로 리다이렉트
      router.push('/login');
    }
  }, [router]);

  // 리다이렉트 처리 중 로딩 화면
  return (
    <div className="min-h-screen flex items-center justify-center bg-gray-50">
      <div className="text-center">
        <h1 className="text-2xl font-bold text-gray-900 mb-4">MM Matching</h1>
        <p className="text-gray-600">로딩 중...</p>
      </div>
    </div>
  );
}

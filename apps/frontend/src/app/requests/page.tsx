'use client';

import { useState, useEffect } from 'react';
import { useRouter } from 'next/navigation';
import { matchAPI, authAPI } from '@/lib/api';
import type { User, MatchRequest } from '@/types';

export default function RequestsPage() {
  const router = useRouter();
  const [user, setUser] = useState<User | null>(null);
  const [requests, setRequests] = useState<MatchRequest[]>([]);
  const [isLoading, setIsLoading] = useState(false);
  const [error, setError] = useState('');

  // 사용자 인증 확인 및 요청 목록 로드
  useEffect(() => {
    const init = async () => {
      try {
        const token = localStorage.getItem('token');
        if (!token) {
          router.push('/login');
          return;
        }

        const userData = await authAPI.me();
        setUser(userData);

        // 매칭 요청 목록 로드
        const requestData = await matchAPI.getMatches();
        setRequests(requestData);
      } catch (err) {
        console.error('초기화 실패:', err);
        router.push('/login');
      }
    };

    init();
  }, [router]);

  const handleAcceptRequest = async (requestId: string) => {
    setIsLoading(true);
    try {
      await matchAPI.acceptRequest(requestId);
      
      // 요청 목록 새로고침
      const updatedRequests = await matchAPI.getMatches();
      setRequests(updatedRequests);
      
      alert('매칭 요청을 수락했습니다.');
    } catch (err: any) {
      setError(err.response?.data?.detail || '요청 수락에 실패했습니다');
    } finally {
      setIsLoading(false);
    }
  };

  const handleRejectRequest = async (requestId: string) => {
    setIsLoading(true);
    try {
      await matchAPI.rejectRequest(requestId);
      
      // 요청 목록 새로고침
      const updatedRequests = await matchAPI.getMatches();
      setRequests(updatedRequests);
      
      alert('매칭 요청을 거절했습니다.');
    } catch (err: any) {
      setError(err.response?.data?.detail || '요청 거절에 실패했습니다');
    } finally {
      setIsLoading(false);
    }
  };

  const handleCancelRequest = async (requestId: string) => {
    setIsLoading(true);
    try {
      await matchAPI.cancelRequest(requestId);
      
      // 요청 목록 새로고침
      const updatedRequests = await matchAPI.getMatches();
      setRequests(updatedRequests);
      
      alert('매칭 요청을 취소했습니다.');
    } catch (err: any) {
      setError(err.response?.data?.detail || '요청 취소에 실패했습니다');
    } finally {
      setIsLoading(false);
    }
  };

  const logout = () => {
    localStorage.removeItem('token');
    localStorage.removeItem('user');
    router.push('/login');
  };

  const getStatusText = (status: string) => {
    switch (status) {
      case 'pending': return '대기중';
      case 'accepted': return '수락';
      case 'rejected': return '거절';
      default: return status;
    }
  };

  const getStatusStyle = (status: string) => {
    switch (status) {
      case 'pending': return 'bg-yellow-100 text-yellow-800';
      case 'accepted': return 'bg-green-100 text-green-800';
      case 'rejected': return 'bg-red-100 text-red-800';
      default: return 'bg-gray-100 text-gray-800';
    }
  };

  if (!user) {
    return (
      <div className="min-h-screen flex items-center justify-center bg-gray-50">
        <div className="text-center">
          <p className="text-gray-600">로딩 중...</p>
        </div>
      </div>
    );
  }

  return (
    <div className="min-h-screen bg-gray-50">
      {/* 네비게이션 바 */}
      <nav className="bg-white shadow-sm mb-8">
        <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
          <div className="flex justify-between h-16">
            <div className="flex items-center">
              <h1 className="text-xl font-bold text-gray-900">MM Matching</h1>
            </div>
            <div className="flex items-center space-x-4">
              <a href="/profile" className="text-gray-600 hover:text-gray-900">프로필</a>
              {user.role === 'mentee' && (
                <a href="/mentors" className="text-gray-600 hover:text-gray-900">멘토 찾기</a>
              )}
              <a href="/requests" className="text-indigo-600 font-medium">요청 관리</a>
              <button
                onClick={logout}
                className="text-gray-600 hover:text-gray-900"
              >
                로그아웃
              </button>
            </div>
          </div>
        </div>
      </nav>

      <div className="max-w-4xl mx-auto px-4 sm:px-6 lg:px-8">
        <div className="mb-8">
          <h2 className="text-3xl font-bold text-gray-900">
            {user.role === 'mentor' ? '받은 매칭 요청' : '보낸 매칭 요청'}
          </h2>
          <p className="mt-2 text-gray-600">
            {user.role === 'mentor' 
              ? '멘티들로부터 받은 매칭 요청을 관리하세요.' 
              : '멘토에게 보낸 매칭 요청 상태를 확인하세요.'}
          </p>
        </div>

        {error && (
          <div className="mb-6 bg-red-50 border border-red-200 text-red-600 px-4 py-3 rounded-md">
            {error}
          </div>
        )}

        {/* 요청 목록 */}
        <div className="space-y-6">
          {requests.map((request) => (
            <div key={request.id} className="bg-white rounded-lg shadow-sm p-6">
              <div className="flex items-start justify-between">
                <div className="flex-1">
                  {/* 상대방 정보 */}
                  <div className="flex items-center mb-4">
                    <img
                      src={
                        user.role === 'mentor' 
                          ? (request.mentee?.profile_image || 'https://placehold.co/500x500.jpg?text=MENTEE')
                          : (request.mentor?.profile_image || 'https://placehold.co/500x500.jpg?text=MENTOR')
                      }
                      alt="프로필"
                      className="w-12 h-12 rounded-full object-cover border-2 border-gray-200"
                    />
                    <div className="ml-3">
                      <h3 className="text-lg font-semibold text-gray-900">
                        {user.role === 'mentor' ? request.mentee?.name : request.mentor?.name}
                      </h3>
                      <p className="text-sm text-gray-600">
                        {user.role === 'mentor' ? '멘티' : '멘토'}
                      </p>
                    </div>
                  </div>

                  {/* 요청 메시지 - 요구사항: class="request-message", mentee 속성 */}
                  <div 
                    className="request-message bg-gray-50 p-4 rounded-md mb-4"
                    data-mentee={user.role === 'mentor' ? request.mentee_id : undefined}
                  >
                    <p className="text-sm font-medium text-gray-700 mb-2">메시지:</p>
                    <p className="text-gray-900">{request.message}</p>
                  </div>

                  {/* 요청 정보 */}
                  <div className="flex items-center justify-between text-sm text-gray-500">
                    <span>
                      요청일: {new Date(request.created_at).toLocaleDateString('ko-KR')}
                    </span>
                    {/* 요청 상태 - 요구사항: id="request-status" */}
                    <span 
                      id="request-status"
                      className={`px-2 py-1 rounded-full text-xs font-medium ${getStatusStyle(request.status)}`}
                    >
                      {getStatusText(request.status)}
                    </span>
                  </div>
                </div>

                {/* 액션 버튼들 */}
                <div className="ml-4 flex flex-col gap-2">
                  {user.role === 'mentor' && request.status === 'pending' && (
                    <>
                      {/* 수락 버튼 - 요구사항: id="accept" */}
                      <button
                        id="accept"
                        onClick={() => handleAcceptRequest(request.id)}
                        disabled={isLoading}
                        className="px-4 py-2 bg-green-600 text-white text-sm rounded-md hover:bg-green-700 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-green-500 disabled:opacity-50"
                      >
                        수락
                      </button>
                      {/* 거절 버튼 - 요구사항: id="reject" */}
                      <button
                        id="reject"
                        onClick={() => handleRejectRequest(request.id)}
                        disabled={isLoading}
                        className="px-4 py-2 bg-red-600 text-white text-sm rounded-md hover:bg-red-700 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-red-500 disabled:opacity-50"
                      >
                        거절
                      </button>
                    </>
                  )}

                  {user.role === 'mentee' && request.status === 'pending' && (
                    <button
                      onClick={() => handleCancelRequest(request.id)}
                      disabled={isLoading}
                      className="px-4 py-2 bg-gray-600 text-white text-sm rounded-md hover:bg-gray-700 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-gray-500 disabled:opacity-50"
                    >
                      취소
                    </button>
                  )}
                </div>
              </div>
            </div>
          ))}
        </div>

        {/* 요청이 없는 경우 */}
        {requests.length === 0 && (
          <div className="text-center py-12">
            <p className="text-gray-500">
              {user.role === 'mentor' ? '받은 매칭 요청이 없습니다.' : '보낸 매칭 요청이 없습니다.'}
            </p>
            {user.role === 'mentee' && (
              <a 
                href="/mentors"
                className="mt-4 inline-block bg-indigo-600 text-white py-2 px-4 rounded-md hover:bg-indigo-700"
              >
                멘토 찾아보기
              </a>
            )}
          </div>
        )}
      </div>
    </div>
  );
}

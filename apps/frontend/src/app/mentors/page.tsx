'use client';

import { useState, useEffect } from 'react';
import { useRouter } from 'next/navigation';
import { mentorAPI, matchAPI, authAPI } from '@/lib/api';
import type { User, MentorProfile } from '@/types';

export default function MentorsPage() {
  const router = useRouter();
  const [user, setUser] = useState<User | null>(null);
  const [mentors, setMentors] = useState<MentorProfile[]>([]);
  const [filteredMentors, setFilteredMentors] = useState<MentorProfile[]>([]);
  const [searchTerm, setSearchTerm] = useState('');
  const [sortBy, setSortBy] = useState('name'); // 'name' 또는 'skill'
  const [isLoading, setIsLoading] = useState(false);
  const [error, setError] = useState('');
  const [requestMessages, setRequestMessages] = useState<{[key: string]: string}>({});

  // 사용자 인증 확인 및 멘토 목록 로드
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

        // 멘티만 접근 가능
        if (userData.role !== 'mentee') {
          router.push('/profile');
          return;
        }

        // 멘토 목록 로드
        const mentorData = await mentorAPI.getMentors();
        setMentors(mentorData);
        setFilteredMentors(mentorData);
      } catch (err) {
        console.error('초기화 실패:', err);
        router.push('/login');
      }
    };

    init();
  }, [router]);

  // 검색 및 정렬 처리
  useEffect(() => {
    let filtered = [...mentors];

    // 검색 필터링
    if (searchTerm) {
      filtered = filtered.filter(mentor => 
        mentor.user.name.toLowerCase().includes(searchTerm.toLowerCase()) ||
        mentor.skills.some(skill => 
          skill.toLowerCase().includes(searchTerm.toLowerCase())
        )
      );
    }

    // 정렬
    if (sortBy === 'name') {
      filtered.sort((a, b) => a.user.name.localeCompare(b.user.name));
    } else if (sortBy === 'skill') {
      filtered.sort((a, b) => a.skills.join(', ').localeCompare(b.skills.join(', ')));
    }

    setFilteredMentors(filtered);
  }, [mentors, searchTerm, sortBy]);

  const handleSendRequest = async (mentorId: string) => {
    const message = requestMessages[mentorId];
    if (!message?.trim()) {
      alert('메시지를 입력해주세요.');
      return;
    }

    setIsLoading(true);
    try {
      await matchAPI.createRequest({
        mentor_id: mentorId,
        message: message.trim(),
      });
      
      alert('매칭 요청이 전송되었습니다.');
      setRequestMessages(prev => ({ ...prev, [mentorId]: '' }));
    } catch (err: any) {
      setError(err.response?.data?.detail || '요청 전송에 실패했습니다');
    } finally {
      setIsLoading(false);
    }
  };

  const logout = () => {
    localStorage.removeItem('token');
    localStorage.removeItem('user');
    router.push('/login');
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
              <a href="/mentors" className="text-indigo-600 font-medium">멘토 찾기</a>
              <a href="/requests" className="text-gray-600 hover:text-gray-900">요청 관리</a>
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

      <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
        <div className="mb-8">
          <h2 className="text-3xl font-bold text-gray-900">멘토 찾기</h2>
          <p className="mt-2 text-gray-600">원하는 멘토를 찾아 매칭 요청을 보내보세요.</p>
        </div>

        {error && (
          <div className="mb-6 bg-red-50 border border-red-200 text-red-600 px-4 py-3 rounded-md">
            {error}
          </div>
        )}

        {/* 검색 및 정렬 */}
        <div className="mb-8 bg-white p-6 rounded-lg shadow-sm">
          <div className="grid grid-cols-1 md:grid-cols-3 gap-4">
            {/* 검색 - 요구사항: id="search" */}
            <div className="md:col-span-2">
              <label htmlFor="search" className="block text-sm font-medium text-gray-700 mb-1">
                기술 스택 검색
              </label>
              <input
                id="search"
                type="text"
                value={searchTerm}
                onChange={(e) => setSearchTerm(e.target.value)}
                className="w-full px-3 py-2 border border-gray-300 rounded-md focus:outline-none focus:ring-indigo-500 focus:border-indigo-500"
                placeholder="예: React, Python, Node.js"
              />
            </div>

            {/* 정렬 */}
            <div>
              <label className="block text-sm font-medium text-gray-700 mb-1">
                정렬 기준
              </label>
              <div className="flex gap-2">
                {/* 이름으로 정렬 - 요구사항: id="name" */}
                <button
                  id="name"
                  onClick={() => setSortBy('name')}
                  className={`px-3 py-2 text-sm rounded-md ${
                    sortBy === 'name'
                      ? 'bg-indigo-600 text-white'
                      : 'bg-gray-200 text-gray-700 hover:bg-gray-300'
                  }`}
                >
                  이름
                </button>
                {/* 스킬로 정렬 - 요구사항: id="skill" */}
                <button
                  id="skill"
                  onClick={() => setSortBy('skill')}
                  className={`px-3 py-2 text-sm rounded-md ${
                    sortBy === 'skill'
                      ? 'bg-indigo-600 text-white'
                      : 'bg-gray-200 text-gray-700 hover:bg-gray-300'
                  }`}
                >
                  스킬
                </button>
              </div>
            </div>
          </div>
        </div>

        {/* 멘토 목록 */}
        <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6">
          {filteredMentors.map((mentor) => (
            /* 개별 멘토 - 요구사항: class="mentor" */
            <div key={mentor.id} className="mentor bg-white rounded-lg shadow-sm p-6">
              {/* 멘토 프로필 */}
              <div className="text-center mb-4">
                <img
                  src={mentor.user.profile_image || 'https://placehold.co/500x500.jpg?text=MENTOR'}
                  alt={`${mentor.user.name} 프로필`}
                  className="w-20 h-20 rounded-full mx-auto object-cover border-2 border-gray-200"
                />
                <h3 className="mt-2 text-lg font-semibold text-gray-900">
                  {mentor.user.name}
                </h3>
                <p className="text-sm text-gray-600">
                  {mentor.years_of_experience}년 경력
                </p>
              </div>

              {/* 자기소개 */}
              <div className="mb-4">
                <p className="text-sm text-gray-700 line-clamp-3">
                  {mentor.bio || '자기소개가 없습니다.'}
                </p>
              </div>

              {/* 기술 스택 */}
              <div className="mb-4">
                <p className="text-xs font-medium text-gray-500 mb-2">기술 스택</p>
                <div className="flex flex-wrap gap-1">
                  {mentor.skills.map((skill, index) => (
                    <span
                      key={index}
                      className="px-2 py-1 bg-indigo-50 text-indigo-600 text-xs rounded-full"
                    >
                      {skill}
                    </span>
                  ))}
                </div>
              </div>

              {/* 매칭 요청 폼 */}
              <div className="border-t pt-4">
                {/* 요청 메시지 - 요구사항: id="message", data-mentor-id, data-testid */}
                <textarea
                  id="message"
                  data-mentor-id={mentor.id}
                  data-testid={`message-${mentor.id}`}
                  value={requestMessages[mentor.id] || ''}
                  onChange={(e) => setRequestMessages(prev => ({
                    ...prev,
                    [mentor.id]: e.target.value
                  }))}
                  className="w-full px-3 py-2 border border-gray-300 rounded-md text-sm focus:outline-none focus:ring-indigo-500 focus:border-indigo-500"
                  placeholder="멘토님께 보낼 메시지를 입력하세요..."
                  rows={3}
                />
                
                {/* 요청 버튼 - 요구사항: id="request" */}
                <button
                  id="request"
                  onClick={() => handleSendRequest(mentor.id)}
                  disabled={isLoading || !requestMessages[mentor.id]?.trim()}
                  className="mt-2 w-full bg-indigo-600 text-white py-2 px-4 rounded-md text-sm font-medium hover:bg-indigo-700 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-indigo-500 disabled:opacity-50 disabled:cursor-not-allowed"
                >
                  {isLoading ? '전송 중...' : '매칭 요청'}
                </button>
              </div>
            </div>
          ))}
        </div>

        {/* 멘토가 없는 경우 */}
        {filteredMentors.length === 0 && (
          <div className="text-center py-12">
            <p className="text-gray-500">
              {searchTerm ? '검색 조건에 맞는 멘토가 없습니다.' : '등록된 멘토가 없습니다.'}
            </p>
          </div>
        )}
      </div>
    </div>
  );
}

'use client';

import { useState, useEffect } from 'react';
import { useRouter } from 'next/navigation';
import { useForm } from 'react-hook-form';
import { zodResolver } from '@hookform/resolvers/zod';
import { z } from 'zod';
import { userAPI, authAPI } from '@/lib/api';
import type { User, ProfileForm } from '@/types';

const profileSchema = z.object({
  name: z.string().min(1, '이름을 입력해주세요'),
  bio: z.string().optional(),
  skills: z.string().optional(), // 임시로 문자열로 받아서 배열로 변환
});

type ProfileFormData = z.infer<typeof profileSchema>;

export default function ProfilePage() {
  const router = useRouter();
  const [user, setUser] = useState<User | null>(null);
  const [isLoading, setIsLoading] = useState(false);
  const [error, setError] = useState('');
  const [success, setSuccess] = useState('');

  const {
    register,
    handleSubmit,
    setValue,
    formState: { errors },
  } = useForm<ProfileFormData>({
    resolver: zodResolver(profileSchema),
  });

  // 사용자 정보 로드
  useEffect(() => {
    const loadUser = async () => {
      try {
        const token = localStorage.getItem('token');
        if (!token) {
          router.push('/login');
          return;
        }

        const userData = await authAPI.me();
        setUser(userData);
        
        // 폼에 기존 데이터 설정
        setValue('name', userData.name || '');
        setValue('bio', userData.bio || '');
        setValue('skills', userData.skills?.join(', ') || '');
      } catch (err) {
        console.error('사용자 정보 로드 실패:', err);
        router.push('/login');
      }
    };

    loadUser();
  }, [router, setValue]);

  const onSubmit = async (data: ProfileFormData) => {
    setIsLoading(true);
    setError('');
    setSuccess('');

    try {
      // 기술 스택을 배열로 변환
      const skills = data.skills 
        ? data.skills.split(',').map(skill => skill.trim()).filter(skill => skill)
        : [];

      const updateData = {
        name: data.name,
        bio: data.bio || '',
        skills,
      };

      const updatedUser = await userAPI.updateProfile(updateData);
      setUser(updatedUser);
      setSuccess('프로필이 성공적으로 업데이트되었습니다.');
    } catch (err: any) {
      setError(err.response?.data?.detail || '프로필 업데이트에 실패했습니다');
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
    <div className="min-h-screen bg-gray-50 py-12 px-4 sm:px-6 lg:px-8">
      {/* 네비게이션 바 - 요구사항에 따른 역할별 메뉴 */}
      <nav className="bg-white shadow-sm mb-8">
        <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
          <div className="flex justify-between h-16">
            <div className="flex items-center">
              <h1 className="text-xl font-bold text-gray-900">MM Matching</h1>
            </div>
            <div className="flex items-center space-x-4">
              <a href="/profile" className="text-gray-600 hover:text-gray-900">프로필</a>
              {user.role === 'mentee' && (
                <>
                  <a href="/mentors" className="text-gray-600 hover:text-gray-900">멘토 찾기</a>
                  <a href="/requests" className="text-gray-600 hover:text-gray-900">요청 관리</a>
                </>
              )}
              {user.role === 'mentor' && (
                <a href="/requests" className="text-gray-600 hover:text-gray-900">요청 관리</a>
              )}
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

      <div className="max-w-2xl mx-auto">
        <div className="bg-white shadow-sm rounded-lg p-6">
          <div className="mb-6">
            <h2 className="text-2xl font-bold text-gray-900">프로필 관리</h2>
            <p className="mt-1 text-sm text-gray-600">
              현재 역할: <span className="font-medium">{user.role === 'mentor' ? '멘토' : '멘티'}</span>
            </p>
          </div>

          {/* 프로필 이미지 - 요구사항: id="profile-photo" */}
          <div className="mb-6 text-center">
            <img
              id="profile-photo"
              src={user.profile_image || (user.role === 'mentor' 
                ? 'https://placehold.co/500x500.jpg?text=MENTOR'
                : 'https://placehold.co/500x500.jpg?text=MENTEE'
              )}
              alt="프로필 이미지"
              className="w-32 h-32 rounded-full mx-auto object-cover border-4 border-gray-200"
            />
            {/* 프로필 이미지 업로드 - 요구사항: id="profile" */}
            <input
              id="profile"
              type="file"
              accept=".jpg,.jpeg,.png"
              className="mt-4 block w-full text-sm text-gray-500
                file:mr-4 file:py-2 file:px-4
                file:rounded-full file:border-0
                file:text-sm file:font-semibold
                file:bg-indigo-50 file:text-indigo-700
                hover:file:bg-indigo-100"
            />
          </div>

          <form onSubmit={handleSubmit(onSubmit)} className="space-y-6">
            {error && (
              <div className="bg-red-50 border border-red-200 text-red-600 px-4 py-3 rounded-md">
                {error}
              </div>
            )}

            {success && (
              <div className="bg-green-50 border border-green-200 text-green-600 px-4 py-3 rounded-md">
                {success}
              </div>
            )}

            {/* 이름 - 요구사항: id="name" */}
            <div>
              <label htmlFor="name" className="block text-sm font-medium text-gray-700">
                이름
              </label>
              <input
                id="name"
                type="text"
                {...register('name')}
                className="mt-1 block w-full px-3 py-2 border border-gray-300 rounded-md shadow-sm focus:outline-none focus:ring-indigo-500 focus:border-indigo-500 sm:text-sm"
                placeholder="이름을 입력하세요"
              />
              {errors.name && (
                <p className="mt-1 text-sm text-red-600">{errors.name.message}</p>
              )}
            </div>

            {/* 자기소개 - 요구사항: id="bio" */}
            <div>
              <label htmlFor="bio" className="block text-sm font-medium text-gray-700">
                자기소개
              </label>
              <textarea
                id="bio"
                rows={4}
                {...register('bio')}
                className="mt-1 block w-full px-3 py-2 border border-gray-300 rounded-md shadow-sm focus:outline-none focus:ring-indigo-500 focus:border-indigo-500 sm:text-sm"
                placeholder="자기소개를 입력하세요"
              />
              {errors.bio && (
                <p className="mt-1 text-sm text-red-600">{errors.bio.message}</p>
              )}
            </div>

            {/* 기술 스택 - 요구사항: id="skillsets" (멘토만) */}
            {user.role === 'mentor' && (
              <div>
                <label htmlFor="skillsets" className="block text-sm font-medium text-gray-700">
                  기술 스택
                </label>
                <input
                  id="skillsets"
                  type="text"
                  {...register('skills')}
                  className="mt-1 block w-full px-3 py-2 border border-gray-300 rounded-md shadow-sm focus:outline-none focus:ring-indigo-500 focus:border-indigo-500 sm:text-sm"
                  placeholder="예: React, Node.js, Python (쉼표로 구분)"
                />
                <p className="mt-1 text-sm text-gray-500">
                  기술 스택을 쉼표(,)로 구분하여 입력하세요
                </p>
                {errors.skills && (
                  <p className="mt-1 text-sm text-red-600">{errors.skills.message}</p>
                )}
              </div>
            )}

            {/* 저장 버튼 - 요구사항: id="save" */}
            <div>
              <button
                id="save"
                type="submit"
                disabled={isLoading}
                className="w-full flex justify-center py-2 px-4 border border-transparent rounded-md shadow-sm text-sm font-medium text-white bg-indigo-600 hover:bg-indigo-700 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-indigo-500 disabled:opacity-50 disabled:cursor-not-allowed"
              >
                {isLoading ? '저장 중...' : '프로필 저장'}
              </button>
            </div>
          </form>
        </div>
      </div>
    </div>
  );
}

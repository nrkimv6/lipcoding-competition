import axios from 'axios';
import type { AuthResponse, LoginForm, SignupForm, User, MentorProfile, MatchRequest } from '@/types';

const API_URL = process.env.NEXT_PUBLIC_API_URL || 'http://localhost:8080';

// Axios 인스턴스 생성
const api = axios.create({
  baseURL: `${API_URL}/api/v1`,
  headers: {
    'Content-Type': 'application/json',
  },
});

// 요청 인터셉터 - JWT 토큰 추가
api.interceptors.request.use((config: any) => {
  const token = localStorage.getItem('token');
  if (token) {
    config.headers.Authorization = `Bearer ${token}`;
  }
  return config;
});

// 응답 인터셉터 - 에러 처리
api.interceptors.response.use(
  (response: any) => response,
  (error: any) => {
    if (error.response?.status === 401) {
      localStorage.removeItem('token');
      localStorage.removeItem('user');
      window.location.href = '/login';
    }
    return Promise.reject(error);
  }
);

// 인증 API
export const authAPI = {
  login: async (data: LoginForm): Promise<AuthResponse> => {
    const formData = new FormData();
    formData.append('username', data.email);
    formData.append('password', data.password);
    
    const response = await api.post('/auth/login', formData, {
      headers: {
        'Content-Type': 'application/x-www-form-urlencoded',
      },
    });
    return response.data;
  },

  register: async (data: SignupForm): Promise<AuthResponse> => {
    const response = await api.post('/auth/register', data);
    return response.data;
  },

  me: async (): Promise<User> => {
    const response = await api.get('/auth/me');
    return response.data;
  },
};

// 사용자 API
export const userAPI = {
  getProfile: async (): Promise<User> => {
    const response = await api.get('/users/profile');
    return response.data;
  },

  updateProfile: async (data: Partial<User>): Promise<User> => {
    const response = await api.put('/users/profile', data);
    return response.data;
  },

  getUser: async (userId: string): Promise<User> => {
    const response = await api.get(`/users/${userId}`);
    return response.data;
  },
};

// 멘토 API
export const mentorAPI = {
  getMentors: async (search?: string): Promise<MentorProfile[]> => {
    const params = search ? { search } : {};
    const response = await api.get('/mentors', { params });
    return response.data;
  },

  getMentor: async (mentorId: string): Promise<MentorProfile> => {
    const response = await api.get(`/mentors/${mentorId}`);
    return response.data;
  },

  createProfile: async (data: any): Promise<MentorProfile> => {
    const response = await api.post('/mentors/profile', data);
    return response.data;
  },

  getMyProfile: async (): Promise<MentorProfile> => {
    const response = await api.get('/mentors/profile');
    return response.data;
  },
};

// 매칭 API
export const matchAPI = {
  getMatches: async (): Promise<MatchRequest[]> => {
    const response = await api.get('/matches');
    return response.data;
  },

  createRequest: async (data: { mentor_id: string; message: string }): Promise<MatchRequest> => {
    const response = await api.post('/matches/request', data);
    return response.data;
  },

  acceptRequest: async (matchId: string): Promise<MatchRequest> => {
    const response = await api.put(`/matches/${matchId}/accept`);
    return response.data;
  },

  rejectRequest: async (matchId: string): Promise<MatchRequest> => {
    const response = await api.put(`/matches/${matchId}/reject`);
    return response.data;
  },

  cancelRequest: async (matchId: string): Promise<void> => {
    await api.delete(`/matches/${matchId}`);
  },
};

export default api;

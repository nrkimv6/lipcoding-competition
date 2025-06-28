// API 응답 타입들
export interface User {
  id: string;
  email: string;
  name: string;
  role: 'mentor' | 'mentee';
  bio?: string;
  profile_image?: string;
  skills?: string[];
}

export interface AuthResponse {
  access_token: string;
  token_type: string;
  user: User;
}

export interface MentorProfile {
  id: string;
  user_id: string;
  user: User;
  bio: string;
  skills: string[];
  years_of_experience: number;
  availability_status: string;
  profile_image?: string;
}

export interface MatchRequest {
  id: string;
  mentee_id: string;
  mentor_id: string;
  message: string;
  status: 'pending' | 'accepted' | 'rejected';
  created_at: string;
  updated_at: string;
  mentee?: User;
  mentor?: User;
}

// 폼 타입들
export interface LoginForm {
  email: string;
  password: string;
}

export interface SignupForm {
  email: string;
  password: string;
  name: string;
  role: 'mentor' | 'mentee';
}

export interface ProfileForm {
  name: string;
  bio: string;
  skills?: string[];
}

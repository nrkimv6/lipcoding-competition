import { z } from 'zod';

// 사용자 역할 enum
export enum UserRole {
  MENTOR = 'mentor',
  MENTEE = 'mentee',
  ADMIN = 'admin',
}

// 매칭 상태 enum
export enum MatchingStatus {
  PENDING = 'pending',
  ACCEPTED = 'accepted',
  REJECTED = 'rejected',
  COMPLETED = 'completed',
}

// 사용자 스키마
export const UserSchema = z.object({
  id: z.number(),
  email: z.string().email(),
  name: z.string().min(1),
  role: z.nativeEnum(UserRole),
  bio: z.string().optional(),
  skills: z.array(z.string()).default([]),
  interests: z.array(z.string()).default([]),
  isActive: z.boolean().default(true),
  createdAt: z.date(),
  updatedAt: z.date(),
});

// 멘토 프로필 스키마
export const MentorProfileSchema = z.object({
  id: z.number(),
  userId: z.number(),
  experienceYears: z.number().min(0),
  expertiseAreas: z.array(z.string()).default([]),
  availability: z.string(),
  maxMentees: z.number().min(1).default(3),
  createdAt: z.date(),
  updatedAt: z.date(),
});

// 멘티 프로필 스키마
export const MenteeProfileSchema = z.object({
  id: z.number(),
  userId: z.number(),
  learningGoals: z.array(z.string()).default([]),
  currentLevel: z.string(),
  preferredMentorType: z.string().optional(),
  createdAt: z.date(),
  updatedAt: z.date(),
});

// 매칭 스키마
export const MatchingSchema = z.object({
  id: z.number(),
  mentorId: z.number(),
  menteeId: z.number(),
  status: z.nativeEnum(MatchingStatus),
  message: z.string().optional(),
  createdAt: z.date(),
  updatedAt: z.date(),
});

// TypeScript 타입 추출
export type User = z.infer<typeof UserSchema>;
export type MentorProfile = z.infer<typeof MentorProfileSchema>;
export type MenteeProfile = z.infer<typeof MenteeProfileSchema>;
export type Matching = z.infer<typeof MatchingSchema>;

// 생성용 타입들 (ID와 타임스탬프 제외)
export type CreateUser = Omit<User, 'id' | 'createdAt' | 'updatedAt'>;
export type CreateMentorProfile = Omit<MentorProfile, 'id' | 'createdAt' | 'updatedAt'>;
export type CreateMenteeProfile = Omit<MenteeProfile, 'id' | 'createdAt' | 'updatedAt'>;
export type CreateMatching = Omit<Matching, 'id' | 'createdAt' | 'updatedAt'>;

// 업데이트용 타입들 (ID와 타임스탬프 제외, 모든 필드 optional)
export type UpdateUser = Partial<Omit<User, 'id' | 'createdAt' | 'updatedAt'>>;
export type UpdateMentorProfile = Partial<Omit<MentorProfile, 'id' | 'userId' | 'createdAt' | 'updatedAt'>>;
export type UpdateMenteeProfile = Partial<Omit<MenteeProfile, 'id' | 'userId' | 'createdAt' | 'updatedAt'>>;
export type UpdateMatching = Partial<Omit<Matching, 'id' | 'createdAt' | 'updatedAt'>>;

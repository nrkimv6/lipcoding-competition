-- MM Matching Database Schema
-- PostgreSQL 데이터베이스 초기화 스크립트

-- 데이터베이스 생성 (이미 존재할 경우 건너뜀)
-- CREATE DATABASE mm_matching;

-- 사용자 테이블
CREATE TABLE IF NOT EXISTS users (
    id SERIAL PRIMARY KEY,
    email VARCHAR(255) UNIQUE NOT NULL,
    name VARCHAR(100) NOT NULL,
    password_hash VARCHAR(255) NOT NULL,
    role VARCHAR(20) NOT NULL CHECK (role IN ('mentor', 'mentee', 'admin')),
    bio TEXT,
    skills TEXT[], -- PostgreSQL 배열 타입
    interests TEXT[],
    is_active BOOLEAN DEFAULT TRUE,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- 멘토 프로필 테이블
CREATE TABLE IF NOT EXISTS mentor_profiles (
    id SERIAL PRIMARY KEY,
    user_id INTEGER REFERENCES users(id) ON DELETE CASCADE,
    experience_years INTEGER NOT NULL DEFAULT 0,
    expertise_areas TEXT[],
    availability TEXT,
    max_mentees INTEGER DEFAULT 3,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- 멘티 프로필 테이블
CREATE TABLE IF NOT EXISTS mentee_profiles (
    id SERIAL PRIMARY KEY,
    user_id INTEGER REFERENCES users(id) ON DELETE CASCADE,
    learning_goals TEXT[],
    current_level VARCHAR(50),
    preferred_mentor_type VARCHAR(100),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- 매칭 테이블
CREATE TABLE IF NOT EXISTS matchings (
    id SERIAL PRIMARY KEY,
    mentor_id INTEGER REFERENCES users(id) ON DELETE CASCADE,
    mentee_id INTEGER REFERENCES users(id) ON DELETE CASCADE,
    status VARCHAR(20) NOT NULL CHECK (status IN ('pending', 'accepted', 'rejected', 'completed')),
    message TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    UNIQUE(mentor_id, mentee_id)
);

-- 인덱스 생성
CREATE INDEX IF NOT EXISTS idx_users_email ON users(email);
CREATE INDEX IF NOT EXISTS idx_users_role ON users(role);
CREATE INDEX IF NOT EXISTS idx_mentor_profiles_user_id ON mentor_profiles(user_id);
CREATE INDEX IF NOT EXISTS idx_mentee_profiles_user_id ON mentee_profiles(user_id);
CREATE INDEX IF NOT EXISTS idx_matchings_mentor_id ON matchings(mentor_id);
CREATE INDEX IF NOT EXISTS idx_matchings_mentee_id ON matchings(mentee_id);
CREATE INDEX IF NOT EXISTS idx_matchings_status ON matchings(status);

-- 업데이트 시간 자동 갱신 함수
CREATE OR REPLACE FUNCTION update_updated_at_column()
RETURNS TRIGGER AS $$
BEGIN
    NEW.updated_at = CURRENT_TIMESTAMP;
    RETURN NEW;
END;
$$ LANGUAGE 'plpgsql';

-- 트리거 생성
CREATE TRIGGER update_users_updated_at 
    BEFORE UPDATE ON users 
    FOR EACH ROW EXECUTE FUNCTION update_updated_at_column();

CREATE TRIGGER update_mentor_profiles_updated_at 
    BEFORE UPDATE ON mentor_profiles 
    FOR EACH ROW EXECUTE FUNCTION update_updated_at_column();

CREATE TRIGGER update_mentee_profiles_updated_at 
    BEFORE UPDATE ON mentee_profiles 
    FOR EACH ROW EXECUTE FUNCTION update_updated_at_column();

CREATE TRIGGER update_matchings_updated_at 
    BEFORE UPDATE ON matchings 
    FOR EACH ROW EXECUTE FUNCTION update_updated_at_column();

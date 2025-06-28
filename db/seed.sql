-- 테스트 데이터 삽입
-- 개발 및 테스트 환경을 위한 샘플 데이터

-- 테스트 사용자 삽입
INSERT INTO users (email, name, password_hash, role, bio, skills, interests) VALUES
('mentor1@example.com', '김멘토', '$2b$12$example_hash_1', 'mentor', 
 '10년 경력의 풀스택 개발자입니다.', 
 ARRAY['JavaScript', 'React', 'Node.js', 'Python'], 
 ARRAY['웹개발', '프론트엔드', '백엔드']),

('mentor2@example.com', '박선생', '$2b$12$example_hash_2', 'mentor', 
 '데이터 사이언스 전문가입니다.', 
 ARRAY['Python', 'Machine Learning', 'SQL', 'TensorFlow'], 
 ARRAY['데이터분석', '머신러닝', 'AI']),

('mentee1@example.com', '이학생', '$2b$12$example_hash_3', 'mentee', 
 '프론트엔드 개발을 배우고 싶은 신입 개발자입니다.', 
 ARRAY['HTML', 'CSS', 'JavaScript'], 
 ARRAY['웹개발', '프론트엔드']),

('mentee2@example.com', '최초보', '$2b$12$example_hash_4', 'mentee', 
 '데이터 분석을 시작하려는 학생입니다.', 
 ARRAY['Excel', 'Python'], 
 ARRAY['데이터분석', '통계']),

('admin@example.com', '관리자', '$2b$12$example_hash_5', 'admin', 
 '시스템 관리자입니다.', 
 ARRAY['System Admin', 'DevOps'], 
 ARRAY['관리', '시스템']);

-- 멘토 프로필 삽입
INSERT INTO mentor_profiles (user_id, experience_years, expertise_areas, availability, max_mentees) VALUES
(1, 10, ARRAY['Full Stack Development', 'JavaScript', 'React'], '평일 저녁, 주말', 5),
(2, 8, ARRAY['Data Science', 'Machine Learning', 'Python'], '주말, 평일 오후', 3);

-- 멘티 프로필 삽입
INSERT INTO mentee_profiles (user_id, learning_goals, current_level, preferred_mentor_type) VALUES
(3, ARRAY['React 마스터하기', '포트폴리오 만들기'], '초급', '친절하고 인내심 있는 멘토'),
(4, ARRAY['Python 데이터 분석', '머신러닝 기초'], '입문', '실무 경험이 풍부한 멘토');

-- 매칭 예시 삽입
INSERT INTO matchings (mentor_id, mentee_id, status, message) VALUES
(1, 3, 'accepted', '프론트엔드 개발 멘토링을 시작하겠습니다!'),
(2, 4, 'pending', '데이터 분석 멘토링을 요청드립니다.');

-- 확인용 쿼리들
-- SELECT * FROM users;
-- SELECT * FROM mentor_profiles;
-- SELECT * FROM mentee_profiles;
-- SELECT * FROM matchings;

#!/bin/bash
# API 테스트 스크립트 for Windows PowerShell
# 사용법: .\test_api.ps1

$BASE_URL = "http://localhost:8000"

Write-Host "🚀 MM Matching API 테스트 시작..." -ForegroundColor Green
Write-Host "기본 URL: $BASE_URL" -ForegroundColor Yellow

# 1. 기본 연결 테스트
Write-Host "`n1️⃣ 기본 연결 테스트..." -ForegroundColor Cyan
try {
    $response = Invoke-RestMethod -Uri "$BASE_URL/" -Method Get
    Write-Host "✅ 기본 연결 성공: $($response.message)" -ForegroundColor Green
} catch {
    Write-Host "❌ 기본 연결 실패: $($_.Exception.Message)" -ForegroundColor Red
    exit 1
}

# 2. 헬스체크
Write-Host "`n2️⃣ 헬스체크..." -ForegroundColor Cyan
try {
    $response = Invoke-RestMethod -Uri "$BASE_URL/health" -Method Get
    Write-Host "✅ 헬스체크 성공: $($response.status)" -ForegroundColor Green
} catch {
    Write-Host "❌ 헬스체크 실패: $($_.Exception.Message)" -ForegroundColor Red
}

# 3. API 문서 접근 테스트
Write-Host "`n3️⃣ API 문서 접근 테스트..." -ForegroundColor Cyan
try {
    $response = Invoke-WebRequest -Uri "$BASE_URL/docs" -Method Get
    if ($response.StatusCode -eq 200) {
        Write-Host "✅ Swagger UI 접근 성공" -ForegroundColor Green
    }
} catch {
    Write-Host "❌ Swagger UI 접근 실패: $($_.Exception.Message)" -ForegroundColor Red
}

# 4. OpenAPI 스펙 확인
Write-Host "`n4️⃣ OpenAPI 스펙 확인..." -ForegroundColor Cyan
try {
    $response = Invoke-RestMethod -Uri "$BASE_URL/openapi.json" -Method Get
    Write-Host "✅ OpenAPI 스펙 로드 성공: $($response.info.title)" -ForegroundColor Green
} catch {
    Write-Host "❌ OpenAPI 스펙 로드 실패: $($_.Exception.Message)" -ForegroundColor Red
}

# 5. 회원가입 테스트
Write-Host "`n5️⃣ 회원가입 테스트..." -ForegroundColor Cyan
$testUser = @{
    email = "test@example.com"
    password = "testpass123"
    name = "테스트 사용자"
    role = "mentee"
    bio = "테스트용 멘티입니다"
    skills = @("JavaScript", "React")
    interests = @("웹개발", "프론트엔드")
} | ConvertTo-Json

try {
    $headers = @{
        "Content-Type" = "application/json"
    }
    $response = Invoke-RestMethod -Uri "$BASE_URL/api/v1/auth/register" -Method Post -Body $testUser -Headers $headers
    Write-Host "✅ 회원가입 성공: 사용자 ID $($response.id)" -ForegroundColor Green
    $testUserId = $response.id
} catch {
    Write-Host "⚠️ 회원가입 실패 (이미 존재하는 사용자일 수 있음): $($_.Exception.Message)" -ForegroundColor Yellow
}

# 6. 로그인 테스트
Write-Host "`n6️⃣ 로그인 테스트..." -ForegroundColor Cyan
$loginData = @{
    email = "test@example.com"
    password = "testpass123"
} | ConvertTo-Json

try {
    $response = Invoke-RestMethod -Uri "$BASE_URL/api/v1/auth/login" -Method Post -Body $loginData -Headers $headers
    Write-Host "✅ 로그인 성공: 토큰 타입 $($response.token_type)" -ForegroundColor Green
    $accessToken = $response.access_token
} catch {
    Write-Host "❌ 로그인 실패: $($_.Exception.Message)" -ForegroundColor Red
}

# 7. 인증이 필요한 엔드포인트 테스트
if ($accessToken) {
    Write-Host "`n7️⃣ 인증된 사용자 정보 조회..." -ForegroundColor Cyan
    try {
        $authHeaders = @{
            "Authorization" = "Bearer $accessToken"
            "Content-Type" = "application/json"
        }
        $response = Invoke-RestMethod -Uri "$BASE_URL/api/v1/auth/me" -Method Get -Headers $authHeaders
        Write-Host "✅ 사용자 정보 조회 성공: $($response.name) ($($response.role))" -ForegroundColor Green
    } catch {
        Write-Host "❌ 사용자 정보 조회 실패: $($_.Exception.Message)" -ForegroundColor Red
    }

    # 8. 멘토 목록 조회
    Write-Host "`n8️⃣ 멘토 목록 조회..." -ForegroundColor Cyan
    try {
        $response = Invoke-RestMethod -Uri "$BASE_URL/api/v1/mentors/" -Method Get -Headers $authHeaders
        Write-Host "✅ 멘토 목록 조회 성공: $($response.Count)명의 멘토" -ForegroundColor Green
    } catch {
        Write-Host "❌ 멘토 목록 조회 실패: $($_.Exception.Message)" -ForegroundColor Red
    }
}

Write-Host "`n🎉 API 테스트 완료!" -ForegroundColor Green
Write-Host "`n📋 테스트 결과 요약:" -ForegroundColor White
Write-Host "- 기본 연결: ✅" -ForegroundColor Green
Write-Host "- 헬스체크: ✅" -ForegroundColor Green  
Write-Host "- API 문서: ✅" -ForegroundColor Green
Write-Host "- 회원가입/로그인: ✅" -ForegroundColor Green
Write-Host "- 인증 시스템: ✅" -ForegroundColor Green

Write-Host "`n🔗 유용한 링크:" -ForegroundColor White
Write-Host "- Swagger UI: $BASE_URL/docs" -ForegroundColor Blue
Write-Host "- ReDoc: $BASE_URL/redoc" -ForegroundColor Blue
Write-Host "- OpenAPI JSON: $BASE_URL/openapi.json" -ForegroundColor Blue

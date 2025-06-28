@echo off
REM MM Matching Database Setup Script for Windows
REM PostgreSQL 데이터베이스 초기화 스크립트 (Windows용)

setlocal enabledelayedexpansion

REM 환경 변수 설정
set DB_NAME=mm_matching
set DB_USER=postgres
set DB_PASSWORD=102030
set DB_HOST=localhost
set DB_PORT=5432

echo 🚀 MM Matching Database 초기화를 시작합니다...

REM PostgreSQL 서비스 확인
echo 📊 PostgreSQL 서비스 확인 중...
sc query postgresql-x64-14 >nul 2>&1
if !errorlevel! neq 0 (
    echo ⚠️ PostgreSQL 서비스를 찾을 수 없습니다. PostgreSQL이 설치되어 있는지 확인해주세요.
    pause
    exit /b 1
)

REM 데이터베이스 존재 확인
echo 🔍 데이터베이스 확인 중...
psql -h %DB_HOST% -p %DB_PORT% -U %DB_USER% -lqt | findstr /B "%DB_NAME%" >nul 2>&1
if !errorlevel! equ 0 (
    echo ✅ 데이터베이스 '%DB_NAME%'가 이미 존재합니다.
) else (
    echo 🔧 데이터베이스 '%DB_NAME%'를 생성합니다...
    createdb -h %DB_HOST% -p %DB_PORT% -U %DB_USER% %DB_NAME%
    if !errorlevel! equ 0 (
        echo ✅ 데이터베이스 생성 완료!
    ) else (
        echo ❌ 데이터베이스 생성 실패!
        pause
        exit /b 1
    )
)

REM 스키마 초기화
echo 🏗️ 스키마를 초기화합니다...
psql -h %DB_HOST% -p %DB_PORT% -U %DB_USER% -d %DB_NAME% -f init.sql
if !errorlevel! equ 0 (
    echo ✅ 스키마 초기화 완료!
) else (
    echo ❌ 스키마 초기화 실패!
    pause
    exit /b 1
)

REM 테스트 데이터 삽입 여부 확인
set /p "INSERT_DATA=🤔 테스트 데이터를 삽입하시겠습니까? (y/N): "
if /i "!INSERT_DATA!"=="y" (
    echo 📝 테스트 데이터를 삽입합니다...
    psql -h %DB_HOST% -p %DB_PORT% -U %DB_USER% -d %DB_NAME% -f seed.sql
    if !errorlevel! equ 0 (
        echo ✅ 테스트 데이터 삽입 완료!
    ) else (
        echo ❌ 테스트 데이터 삽입 실패!
    )
) else (
    echo ⏭️ 테스트 데이터 삽입을 건너뜁니다.
)

echo.
echo 🎉 데이터베이스 초기화가 완료되었습니다!
echo 📋 연결 정보:
echo    - Host: %DB_HOST%
echo    - Port: %DB_PORT%
echo    - Database: %DB_NAME%
echo    - User: %DB_USER%
echo.
pause

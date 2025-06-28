@echo off
REM Windows용 테스트 실행 스크립트

echo 🧪 MM Matching App 테스트 실행
echo ================================

REM 가상환경 활성화
call apps\backend\venv\Scripts\activate.bat

REM 인수에 따른 테스트 실행
if "%1"=="unit" (
    echo 단위 테스트 실행
    D:\mm-matching-app\apps\backend\venv\Scripts\python.exe -m pytest tests\backend\unit\ -v
) else if "%1"=="integration" (
    echo 통합 테스트 실행
    D:\mm-matching-app\apps\backend\venv\Scripts\python.exe -m pytest tests\backend\integration\ -v
) else if "%1"=="backend" (
    echo 백엔드 전체 테스트 실행
    D:\mm-matching-app\apps\backend\venv\Scripts\python.exe -m pytest tests\backend\ -v
) else if "%1"=="all" (
    echo 전체 테스트 실행
    D:\mm-matching-app\apps\backend\venv\Scripts\python.exe -m pytest tests\ -v
) else if "%1"=="legacy" (
    echo 기존 테스트 및 DB 체크 실행
    echo 🔍 데이터베이스 연결 테스트...
    D:\mm-matching-app\apps\backend\venv\Scripts\python.exe apps\backend\db_check.py
) else if "%1"=="db-check" (
    echo 데이터베이스 연결 체크
    D:\mm-matching-app\apps\backend\venv\Scripts\python.exe apps\backend\db_check.py
) else if "%1"=="" (
    echo 빠른 테스트 실행 ^(단위 테스트만^)
    D:\mm-matching-app\apps\backend\venv\Scripts\python.exe -m pytest tests\backend\unit\ -v
) else (
    echo 사용법: run_tests.bat [unit^|integration^|backend^|all^|legacy^|db-check]
    echo   unit        - 단위 테스트만 실행
    echo   integration - 통합 테스트만 실행
    echo   backend     - 백엔드 전체 테스트 실행
    echo   all         - 전체 테스트 실행
    echo   legacy      - 데이터베이스 연결 체크 (호환성)
    echo   db-check    - 데이터베이스 연결 상태 확인
    exit /b 1
)

echo.
echo ✅ 테스트 완료!

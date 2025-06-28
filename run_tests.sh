#!/bin/bash
# Unix/Linux용 테스트 실행 스크립트

echo "🧪 MM Matching App 테스트 실행"
echo "================================"

# Backend 디렉토리로 이동
cd apps/backend

# 가상환경 활성화 확인
if [[ "$VIRTUAL_ENV" != "" ]]
then
    echo "✅ 가상환경 활성화됨: $VIRTUAL_ENV"
else
    echo "⚠️  가상환경을 활성화해주세요: source venv/bin/activate"
    exit 1
fi

# pytest 설치 확인
if ! python -c "import pytest" 2>/dev/null; then
    echo "📦 pytest 설치 중..."
    pip install pytest pytest-asyncio httpx
fi

# 프로젝트 루트로 이동
cd ../../

echo ""
echo "🔍 테스트 시작..."

# 인수에 따른 테스트 실행
case "$1" in
    "unit")
        echo "단위 테스트 실행"
        python -m pytest tests/backend/unit/ -v
        ;;
    "integration") 
        echo "통합 테스트 실행"
        python -m pytest tests/backend/integration/ -v
        ;;
    "backend")
        echo "백엔드 전체 테스트 실행"
        python -m pytest tests/backend/ -v
        ;;
    "all")
        echo "전체 테스트 실행"
        python -m pytest tests/ -v
        ;;
    "")
        echo "빠른 테스트 실행 (단위 테스트만)"
        python -m pytest tests/backend/unit/ -v
        ;;
    *)
        echo "사용법: ./run_tests.sh [unit|integration|backend|all]"
        echo "  unit        - 단위 테스트만 실행"
        echo "  integration - 통합 테스트만 실행" 
        echo "  backend     - 백엔드 전체 테스트 실행"
        echo "  all         - 전체 테스트 실행"
        exit 1
        ;;
esac

echo ""
echo "✅ 테스트 완료!"

#!/bin/bash

# MM Matching Database Setup Script
# PostgreSQL 데이터베이스 초기화 스크립트

set -e  # 오류 발생 시 스크립트 중단

# 환경 변수 설정
DB_NAME="mm_matching"
DB_USER="postgres"
DB_PASSWORD="102030"
DB_HOST="localhost"
DB_PORT="5432"

echo "🚀 MM Matching Database 초기화를 시작합니다..."

# 데이터베이스 존재 확인 및 생성
echo "📊 데이터베이스 확인 중..."
if psql -h $DB_HOST -p $DB_PORT -U $DB_USER -lqt | cut -d \| -f 1 | grep -qw $DB_NAME; then
    echo "✅ 데이터베이스 '$DB_NAME'가 이미 존재합니다."
else
    echo "🔧 데이터베이스 '$DB_NAME'를 생성합니다..."
    createdb -h $DB_HOST -p $DB_PORT -U $DB_USER $DB_NAME
    echo "✅ 데이터베이스 생성 완료!"
fi

# 스키마 초기화
echo "🏗️ 스키마를 초기화합니다..."
psql -h $DB_HOST -p $DB_PORT -U $DB_USER -d $DB_NAME -f init.sql
echo "✅ 스키마 초기화 완료!"

# 테스트 데이터 삽입 (선택사항)
read -p "🤔 테스트 데이터를 삽입하시겠습니까? (y/N): " -n 1 -r
echo
if [[ $REPLY =~ ^[Yy]$ ]]; then
    echo "📝 테스트 데이터를 삽입합니다..."
    psql -h $DB_HOST -p $DB_PORT -U $DB_USER -d $DB_NAME -f seed.sql
    echo "✅ 테스트 데이터 삽입 완료!"
else
    echo "⏭️ 테스트 데이터 삽입을 건너뜁니다."
fi

echo "🎉 데이터베이스 초기화가 완료되었습니다!"
echo "📋 연결 정보:"
echo "   - Host: $DB_HOST"
echo "   - Port: $DB_PORT"
echo "   - Database: $DB_NAME"
echo "   - User: $DB_USER"

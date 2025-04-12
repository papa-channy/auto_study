#!/bin/bash

echo ""
echo "🎯 Git 설정 자동 적용 스크립트"
echo "──────────────────────────────"

# 1. 줄바꿈 경고 해결
echo "🔧 줄바꿈 설정: core.autocrlf = input"
git config --global core.autocrlf input

# 2. 한글 파일명 깨짐 방지
echo "🔧 한글 파일명 표시 설정: core.quotepath = false"
git config --global core.quotepath false

# 3. 사용자 정보 등록 여부 확인
name=$(git config --global user.name)
email=$(git config --global user.email)

if [ -z "$name" ] || [ -z "$email" ]; then
    echo ""
    echo "⚠️ Git 사용자 정보가 설정되어 있지 않아요!"
    read -p "👤 이름을 입력하세요: " input_name
    read -p "📧 이메일을 입력하세요: " input_email
    git config --global user.name "$input_name"
    git config --global user.email "$input_email"
    echo "✅ 사용자 정보가 설정되었습니다!"
else
    echo "✅ 사용자 정보: $name <$email>"
fi

echo ""
echo "🎉 Git 설정 완료! 이제 경고 없이 깔끔하게 사용할 수 있어요!"

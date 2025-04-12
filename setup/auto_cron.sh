#!/bin/bash

# 📁 setup/auto_cron.sh
# 크론탭에 run_all.py 자동 등록하는 설정 스크립트

# 프로젝트 및 파이썬 경로 설정
PROJECT_DIR="$HOME/Desktop/auto_study"
PYTHON_PATH="/c/Program Files/Python313/python.exe"
SCRIPT_PATH="$PROJECT_DIR/scripts/run_all.py"
LOG_PATH="$PROJECT_DIR/logs/cron.log"

# 크론에 추가할 명령어 구성
CRON_JOB="0 9 * * 1 cd \"$PROJECT_DIR\" && \"$PYTHON_PATH\" \"$SCRIPT_PATH\" >> \"$LOG_PATH\" 2>&1"

# 기존 중복 제거 후 등록
( crontab -l 2>/dev/null | grep -v "$SCRIPT_PATH" ; echo "$CRON_JOB" ) | crontab -

echo "✅ 크론 작업 등록 완료! (매주 월요일 09:00 자동 실행)"
crontab -l
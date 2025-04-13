# 📁 scripts/run_all.py
import subprocess
import os
import sys

# 🔧 PYTHONPATH 문제 해결을 위한 경로 강제 삽입
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

# 🔁 각 스크립트를 순서대로 실행하는 도우미 함수
def run_step(description, command):
    print(f"\n🔹 {description}")
    try:
        subprocess.run(command, check=True)
    except subprocess.CalledProcessError as e:
        print(f"❌ 실패: {description}\n↳ 오류: {e}")
        exit(1)

# 🚀 전체 자동화 파이프라인 시작!

run_step("[1] GPT 문제 생성 시작", ["python", "scripts/run_custom.py"])
run_step("[2] 프롬프트 템플릿 갱신", ["python", "-m", "gpt.prompt_generator"])
run_step("[3] 노션 업로드 실행", ["python", "-m", "notion.notion_uploader"])
run_step("[4] 문제 아카이브 및 초기화", ["python", "-m", "tools.archiver"])
run_step("[5] 노트북 자동 생성", ["python", "scripts/notebook_generator.py"])
run_step("[6] 실행 리포트 기록", ["python", "tools/log_reporter.py"])

print("\n✅ 모든 자동화 완료!")

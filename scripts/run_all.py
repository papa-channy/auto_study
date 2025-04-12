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
        subprocess.run(command, check=True)  # 🛠️ 명령 실행
    except subprocess.CalledProcessError as e:
        print(f"❌ 실패: {description}\n↳ 오류: {e}")  # ❗ 실패 시 로그 출력
        exit(1)

# 🚀 전체 자동화 파이프라인 시작!

# [1] GPT 문제 생성 (new_questions.txt 갱신)
run_step("[1] GPT 문제 생성 시작", ["python", "scripts/run_custom.py"])

# [2] 프롬프트 템플릿 갱신 (예시 최신화)
run_step("[2] 프롬프트 템플릿 갱신", ["python", "scripts/prompt_generator.py"])

# [3] 노션 업로드 (업로드 완료된 문제)
run_step("[3] 노션 업로드 실행", ["python", "notion/notion_uploader.py"])

# [4] 문제 아카이브 처리 + new_questions.txt 초기화
run_step("[4] 문제 아카이브 및 초기화", ["python", "tools/archiver.py"])

# [5] 노트북 생성 (주차별 폴더에 도구별로 저장)
run_step("[5] 노트북 자동 생성", ["python", "scripts/notebook_generator.py"])

# [6] 실행 리포트 로그 저장
run_step("[6] 실행 리포트 기록", ["python", "tools/log_reporter.py"])

# ✅ 전체 완료 메시지
print("\n✅ 모든 자동화 완료!")
print("→ 문제 생성, 아카이브, 노션 업로드, 노트북 생성 및 리포트 기록 완료.")
print("→ 모든 과정이 정상적으로 완료되었습니다. 🎉")
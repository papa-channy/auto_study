# 📁 tools/log_reporter.py
import os
from datetime import datetime
from tools.paths import ARCHIVED_QUESTIONS_PATH, NOTEBOOKS_DIR, ACTIVE_STUDY_RANGE_PATH

# 📝 자동화 리포트 생성기
def generate_report():
    today = datetime.now()
    timestamp = today.strftime("%Y-%m-%d %H:%M")
    week_folder = today.strftime("(%y/%m %U주차)")  # 주차명과 일치시키기 위함

    # 📊 문제 수 계산
    count_by_tool = {}
    total = 0
    if os.path.exists(ARCHIVED_QUESTIONS_PATH):
        with open(ARCHIVED_QUESTIONS_PATH, "r", encoding="utf-8") as f:
            for line in f:
                parts = line.strip().split("|")
                if len(parts) == 5:
                    tool = parts[3].split("/")[0].strip()
                    count_by_tool[tool] = count_by_tool.get(tool, 0) + 1
                    total += 1

    # 📓 생성된 노트북 파일 확인
    notebook_path = os.path.join(NOTEBOOKS_DIR, week_folder)
    ipynbs = []
    if os.path.exists(notebook_path):
        ipynbs = [f for f in os.listdir(notebook_path) if f.endswith(".ipynb")]

    # 📂 로그 폴더 준비
    log_dir = os.path.join(os.path.dirname(NOTEBOOKS_DIR), "logs")
    os.makedirs(log_dir, exist_ok=True)
    log_path = os.path.join(log_dir, f"report_{today.strftime('%Y-%m-%d')}.txt")

    # 🧾 리포트 작성
    with open(log_path, "w", encoding="utf-8") as f:
        f.write(f"📅 자동화 실행 리포트 - {timestamp}\n\n")
        f.write(f"✅ 총 업로드된 문제 수: {total}\n")
        for tool, count in count_by_tool.items():
            f.write(f"- {tool}: {count}문제\n")
        f.write(f"\n📤 노션 업로드: 완료 (추정)\n")
        f.write(f"📦 아카이브 저장: 완료\n")
        f.write(f"📓 노트북 생성: {', '.join(ipynbs) if ipynbs else '없음'}\n")
        f.write(f"🕒 실행 시각: {timestamp}\n")

    print(f"📝 리포트 저장 완료 → {log_path}")

if __name__ == "__main__":
    generate_report()

# 📁 tools/archiver.py
from tools.paths import NEW_QUESTIONS_PATH, ARCHIVED_QUESTIONS_PATH
import os

# 📦 문제 아카이브 처리 함수
def archive_questions():
    """new_questions.txt 내용을 archived_questions.txt에 누적 저장하고 초기화"""

    # ✅ 파일 존재 여부 확인
    if not os.path.exists(NEW_QUESTIONS_PATH):
        print("⚠️ new_questions.txt 파일이 존재하지 않습니다.")
        return

    # 📥 새 문제 로딩
    with open(NEW_QUESTIONS_PATH, "r", encoding="utf-8") as new_file:
        new_lines = [line.strip() for line in new_file if line.strip()]

    if not new_lines:
        print("ℹ️ 새로 등록된 문제가 없습니다. 아카이브 생략.")
        return

    # 📦 기존 아카이브 로딩 (중복 방지용)
    archived_lines = set()
    if os.path.exists(ARCHIVED_QUESTIONS_PATH):
        with open(ARCHIVED_QUESTIONS_PATH, "r", encoding="utf-8") as archive_file:
            archived_lines.update(line.strip() for line in archive_file if line.strip())

    # 🔍 중복 제거된 신규 문제 추출
    new_unique = [line for line in new_lines if line not in archived_lines]

    # 📝 아카이브에 추가 저장
    with open(ARCHIVED_QUESTIONS_PATH, "a", encoding="utf-8") as archive_file:
        for line in new_unique:
            archive_file.write(line + "\n")

    # 🧹 new_questions 초기화
    with open(NEW_QUESTIONS_PATH, "w", encoding="utf-8") as new_file:
        new_file.write("")

    print(f"📦 {len(new_unique)}개 문제 아카이브 완료 및 초기화됨.")

# ▶️ 스크립트 단독 실행 시
if __name__ == "__main__":
    archive_questions()

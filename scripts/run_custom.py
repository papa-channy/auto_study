# 📁 scripts/run_custom.py
import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))  # ✅ 루트 경로 강제 포함

from gpt.generator import generate_questions, save_questions
from tools.paths import (
    ACTIVE_STUDY_RANGE_PATH,  # 📂 사용할 도구 리스트 (pds/sql/viz)
    DATASET_LIST_PATH,        # 📂 사용할 데이터셋 리스트
    DIFFICULTY_MAP_PATH       # 📂 도구별 난이도 설정
)

# 📥 설정 파일 불러오기 함수들
def load_list(path):
    with open(path, "r", encoding="utf-8") as f:
        return [line.strip() for line in f if line.strip() and not line.startswith("#")]

def load_dataset_list():
    return load_list(DATASET_LIST_PATH)

def load_active_tools():
    return load_list(ACTIVE_STUDY_RANGE_PATH)

def load_difficulty_map():
    difficulty_map = {}
    with open(DIFFICULTY_MAP_PATH, "r", encoding="utf-8") as f:
        for line in f:
            if ":" in line:
                tool, levels = line.strip().split(":", 1)
                difficulty_map[tool.strip()] = [lvl.strip() for lvl in levels.split(",")]
    return difficulty_map

# 🚀 메인 실행 로직
def run():
    tools = load_active_tools()         # ✅ 학습할 도구 리스트 (예: ["pds", "sql"])
    datasets = load_dataset_list()      # ✅ 사용할 데이터셋 리스트
    difficulty_map = load_difficulty_map()  # ✅ 도구별 난이도 매핑

    for tool in tools:
        if tool not in difficulty_map:
            print(f"⚠️ 난이도 설정이 없는 도구: {tool} → 건너뜀")
            continue

        for dataset in datasets:
            try:
                print(f"\n📘 생성 중: {tool} × {dataset}")
                result = generate_questions(dataset, tool)  # 🧠 GPT 문제 생성
                save_questions(result)                      # 💾 결과 저장
            except Exception as e:
                print(f"❌ 오류 발생: {tool} × {dataset} → {e}")

    print("\n✅ 모든 문제 생성 완료!")

# ▶️ 스크립트 실행 시작
if __name__ == "__main__":
    run()

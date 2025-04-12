# 📁 scripts/custom_setting.py
from tools.paths import (
    ACTIVE_STUDY_RANGE_PATH,
    DATASET_LIST_PATH,
    DIFFICULTY_MAP_PATH
)

MAX_CALLS = 10  # ✅ 호출 횟수 상한선

# 📄 기본 리스트 파일 로딩/저장 함수들
def load_list(path):
    with open(path, "r", encoding="utf-8") as f:
        return [line.strip() for line in f if line.strip() and not line.startswith("#")]

def save_list(path, items):
    with open(path, "w", encoding="utf-8") as f:
        for item in items:
            f.write(item + "\n")

# 🔧 사용자에게 리스트 수정 옵션 제공 (1. 그대로 / 2. 추가 / 3. 삭제)
def edit_list(name, path):
    while True:
        items = load_list(path)
        print(f"\n📘 현재 {name}: {', '.join(items)}")
        print("1. ✅ 그대로 사용\n2. ➕ 추가\n3. ❌ 삭제")
        choice = input("> ").strip()

        if choice == "1":
            return items
        elif choice == "2":
            new_item = input("추가할 항목 입력: ").strip()
            if new_item and new_item not in items:
                items.append(new_item)
                save_list(path, items)
        elif choice == "3":
            for i, item in enumerate(items):
                print(f"{i+1}. {item}")
            idx = input("삭제할 번호 입력: ").strip()
            if idx.isdigit():
                idx = int(idx)
                if 1 <= idx <= len(items):
                    del items[idx - 1]
                    save_list(path, items)
        else:
            print("❗ 1~3 중에서 선택해 주세요.")

# 📊 난이도 매핑 수정

def edit_difficulty(path):
    difficulties = {}
    if os.path.exists(path):
        with open(path, "r", encoding="utf-8") as f:
            for line in f:
                if ":" in line:
                    k, v = line.strip().split(":")
                    difficulties[k.strip()] = [s.strip() for s in v.split(",")]

    while True:
        print("\n📚 현재 난이도 설정:")
        for k, v in difficulties.items():
            print(f"- {k}: {', '.join(v)}")

        print("1. ✅ 그대로 사용\n2. ✏️ 수정")
        choice = input("> ").strip()
        if choice == "1":
            return difficulties
        elif choice == "2":
            tool = input("대상 도구 입력: ").strip()
            current = difficulties.get(tool, [])
            print(f"현재: {', '.join(current) if current else '(없음)'}")
            while True:
                print("1. 그대로 2. 추가 3. 삭제")
                action = input("선택 > ").strip()
                if action == "1":
                    break
                elif action == "2":
                    new = input("추가할 난이도: ").strip()
                    if new and new not in current:
                        current.append(new)
                elif action == "3":
                    for i, val in enumerate(current):
                        print(f"{i+1}. {val}")
                    idx = input("삭제할 번호: ").strip()
                    if idx.isdigit():
                        idx = int(idx)
                        if 1 <= idx <= len(current):
                            del current[idx - 1]
                difficulties[tool] = current
                print(f"→ 현재: {', '.join(current)}")
            with open(path, "w", encoding="utf-8") as f:
                for k, v in difficulties.items():
                    f.write(f"{k}: {', '.join(v)}\n")
            return difficulties

# 🔢 GPT 호출 횟수 설정 (최대 10)
def edit_gpt_calls():
    while True:
        print("\n📶 현재 GPT 호출 횟수는 도구별 문제수 계산에 사용됩니다.")
        calls = input("사용할 호출 횟수 입력 (1~10): ").strip()
        if calls.isdigit():
            calls = int(calls)
            if 1 <= calls <= MAX_CALLS:
                return calls
        print("❗ 1~10 사이 자연수를 입력해 주세요.")

# 📊 최종 설정 요약 출력
def show_summary(tools, datasets, difficulty_map, gpt_calls):
    print("\n🧾 최종 설정 요약")
    total = 0
    for tool in tools:
        levels = difficulty_map.get(tool, [])
        count = len(levels) * gpt_calls
        total += count
        print(f"- {tool}: {len(levels)}단계 × {gpt_calls}회 = {count}문제")
    print(f"총 예상 문제 수: {total}")
    print(f"사용할 데이터셋: {', '.join(datasets)}")

# ▶️ 실행 엔트리 포인트
if __name__ == "__main__":
    while True:
        tools = edit_list("도구", ACTIVE_STUDY_RANGE_PATH)
        datasets = edit_list("데이터셋", DATASET_LIST_PATH)
        difficulty_map = edit_difficulty(DIFFICULTY_MAP_PATH)
        gpt_calls = edit_gpt_calls()

        show_summary(tools, datasets, difficulty_map, gpt_calls)

        again = input("\n다시 수정하시겠어요? (y/n): ").strip().lower()
        if again != "y":
            print("🎉 설정 완료!")
            break

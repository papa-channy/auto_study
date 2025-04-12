# 📁 scripts/prompt_generator.py
import os
from tools.paths import GPT_DIR  # 📂 프롬프트 및 예시 파일 경로가 저장된 디렉토리

# 📄 예시 파일 경로 매핑 (도구 약어 → 최근 예시 파일 경로)
EXAMPLE_PATHS = {
    "pds": os.path.join(GPT_DIR, "recent_examples_pandas.txt"),
    "sql": os.path.join(GPT_DIR, "recent_examples_sql.txt"),
    "viz": os.path.join(GPT_DIR, "recent_examples_viz.txt"),
}

# 📄 프롬프트 파일 경로 매핑 (도구 약어 → 출력 프롬프트 파일 경로)
OUTPUT_PATHS = {
    "pds": os.path.join(GPT_DIR, "prompt_pandas.txt"),
    "sql": os.path.join(GPT_DIR, "prompt_sql.txt"),
    "viz": os.path.join(GPT_DIR, "prompt_viz.txt"),
}

# 📝 프롬프트 헤더 템플릿 (도구별 고정 프롬프트 서두)
HEADER = {
    "pds": "아래 조건에 맞는 Pandas 문제를 생성해줘.\n\n🟡 요청 조건:\n- 데이터셋: {dataset}  ← 예: tips, titanic, iris\n- 문제 개수: 3문제\n- 난이도는 중 → 상 → 최상 순으로 구성\n\n🟢 출력 형식:\n번호|난이도|dataset|분류|문제 내용\n\n📝 출력 예시:",
    "sql": "아래 조건에 맞는 SQL 문제를 생성해줘.\n\n🟡 요청 조건:\n- 데이터셋: {dataset} ← 예: tips, titanic, iris\n- 문제 개수: 3문제\n- 난이도는 하 → 중하 → 중상 순으로 구성\n\n🟢 출력 형식:\n번호|난이도|dataset|분류|문제 내용\n\n📝 출력 예시:",
    "viz": "아래 조건에 맞는 시각화 문제를 생성해줘.\n\n🟡 요청 조건:\n- 데이터셋: {dataset} ← 예: titanic, tips, iris\n- 문제 개수: 3문제\n- 난이도는 하 → 중하 → 중상 순으로 구성\n\n🟢 출력 형식:\n번호|난이도|dataset|분류|문제 내용\n\n📝 출력 예시:",
}

# 🛠️ 프롬프트 파일 자동 생성 함수
def generate_prompt(tool):
    tool = tool.lower()  # ✅ 도구명 소문자로 통일
    example_path = EXAMPLE_PATHS[tool]  # 📂 예시 파일 경로
    output_path = OUTPUT_PATHS[tool]    # 📁 출력 프롬프트 파일 경로
    header = HEADER[tool]               # 📝 프롬프트 서두 내용

    # 📥 예시 불러오기
    with open(example_path, "r", encoding="utf-8") as f:
        examples = f.read().strip()

    # 💾 프롬프트 파일 생성 및 저장
    with open(output_path, "w", encoding="utf-8") as f:
        f.write(header + "\n" + examples + "\n\n❗주의사항:\n")
        if tool == "pds":
            f.write("- 문제 내용에 데이터셋 이름은 언급하지 마세요.\n")
            f.write("- 실제 분석에서 자주 쓰이는 문제로 구성해 주세요.\n")
        elif tool == "sql":
            f.write("- SQL 키워드는 직접 넣지 말고 설명 중심으로 구성해 주세요.\n")
        elif tool == "viz":
            f.write("- 시각화 도구 이름은 문제에 포함하지 마세요.\n")
            f.write("- 시각적으로 비교하거나 인사이트를 도출할 수 있는 주제로 구성해 주세요.\n")

    print(f"✅ {tool} 프롬프트 생성 완료 → {output_path}")  # 🎉 완료 메시지 출력

# ▶️ 테스트 실행용: 모든 도구에 대해 생성 함수 실행
if __name__ == "__main__":
    tools = ["pds", "sql", "viz"]
    for tool in tools:
        generate_prompt(tool)

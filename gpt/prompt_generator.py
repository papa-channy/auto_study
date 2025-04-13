# 📁 gpt/prompt_generator.py (✅ 프롬프트 한글화 + 양식 엄격화 버전)
import sys, os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from tools.paths import GPT_DIR

# 📄 예시 파일 경로 매핑
EXAMPLE_PATHS = {
    "pds": os.path.join(GPT_DIR, "recent_examples_pandas.txt"),
    "sql": os.path.join(GPT_DIR, "recent_examples_sql.txt"),
    "viz": os.path.join(GPT_DIR, "recent_examples_viz.txt"),
}

# 📄 프롬프트 파일 저장 경로
OUTPUT_PATHS = {
    "pds": os.path.join(GPT_DIR, "prompt_pandas.txt"),
    "sql": os.path.join(GPT_DIR, "prompt_sql.txt"),
    "viz": os.path.join(GPT_DIR, "prompt_viz.txt"),
}

# 📝 프롬프트 헤더 (한글 버전 + 형식 강조)
HEADER = {
    "pds": "아래 조건에 따라 Pandas 문제를 생성해 주세요.\n\n🟡 조건:\n- 데이터셋: {dataset} (예: tips, titanic 등)\n- 문제 수: 3문제\n- 난이도: 중 → 상 → 최상\n- 문제는 반드시 한국어로 작성하세요.\n\n❗ 출력 형식은 아래 양식을 정확히 따르세요 (다른 문장/설명/힌트 추가 금지):\n1|중|tips|데이터 전처리|결측값을 제거하라\n2|상|tips|요약 통계|성별별 평균 팁 금액을 구하라\n3|최상|tips|시각화|요일별 생존율을 그래프로 나타내라",

    "sql": "아래 조건에 따라 SQL 문제를 생성해 주세요.\n\n🟡 조건:\n- 데이터셋: {dataset} (예: tips, titanic 등)\n- 문제 수: 3문제\n- 난이도: 하 → 중하 → 중상\n- 문제는 반드시 한국어로 작성하세요.\n\n❗ 출력 형식은 아래 양식을 정확히 따르세요 (다른 문장/설명/힌트 추가 금지):\n1|하|tips|Filtering|팁이 10달러 이상인 행을 찾으세요.\n2|중하|tips|Aggregation|요일별 총 지출 금액을 구하세요.\n3|중상|tips|Join|음료 정보와 함께 고객 정보를 조인하여 출력하세요.",

    "viz": "아래 조건에 따라 시각화 문제를 생성해 주세요.\n\n🟡 조건:\n- 데이터셋: {dataset} (예: tips, titanic 등)\n- 문제 수: 3문제\n- 난이도: 하 → 중하 → 중상\n- 문제는 반드시 한국어로 작성하세요.\n\n❗ 출력 형식은 아래 양식을 정확히 따르세요 (다른 문장/설명/힌트 추가 금지):\n1|하|tips|기초 시각화|요일별 팁 금액 분포를 막대그래프로 나타내라\n2|중하|tips|비교 분석|식사 인원수에 따른 팁 금액을 박스플롯으로 비교하라\n3|중상|tips|시계열|시간대별 평균 팁 금액을 선그래프로 나타내라",
}

# 📌 프롬프트 생성 함수
def generate_prompt(tool):
    tool = tool.lower()
    example_path = EXAMPLE_PATHS[tool]
    output_path = OUTPUT_PATHS[tool]
    header = HEADER[tool]

    with open(example_path, "r", encoding="utf-8") as f:
        examples = f.read().strip()

    with open(output_path, "w", encoding="utf-8") as f:
        f.write(header + "\n\n📝 예시:\n" + examples)

    print(f"✅ {tool} 프롬프트 생성 완료 → {output_path}")

# ▶️ 진입점
if __name__ == "__main__":
    for tool in ["pds", "sql", "viz"]:
        generate_prompt(tool)

# 📁 gpt/generator.py (✅ 문제 정제 필터링 + 랜덤 데이터셋 선택 구조 지원)
import sys, os, random
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from openai import OpenAI
from dotenv import load_dotenv
from tools.paths import (
    PROMPT_PATHS,
    NEW_QUESTIONS_PATH,
    ENV_PATH,
)

# 🔧 직접 경로 지정 (ACTIVE_DATASETS_PATH 미정의 시 오류 방지)
ACTIVE_DATASETS_PATH = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "config", "active_dataset.txt")

# 🔐 환경변수 로드 및 Groq API 설정
load_dotenv(dotenv_path=ENV_PATH)
client = OpenAI(
    api_key=os.getenv("GROQ_API_KEY"),
    base_url="https://api.groq.com/openai/v1"
)

# 📥 템플릿 로드 함수
def load_prompt_template(tool):
    path = PROMPT_PATHS[tool]
    with open(path, "r", encoding="utf-8") as f:
        return f.read()

# ✂️ GPT 응답 정제 함수
def clean_gpt_response(text):
    lines = text.strip().split("\n")
    valid = [
        line.strip() for line in lines
        if line.count("|") >= 4 and line.strip()[0].isdigit() and any("가" <= ch <= "힣" for ch in line)
    ]
    return "\n".join(valid)

# 🎲 랜덤 데이터셋 1개 선택 함수
def choose_random_dataset():
    with open(ACTIVE_DATASETS_PATH, "r", encoding="utf-8") as f:
        datasets = [line.strip() for line in f if line.strip()]
    selected = random.choice(datasets)
    print(f"🎯 이번 실행에 선택된 데이터셋: {selected}")
    return selected

# 🧠 문제 생성 함수 (Groq 기반)
def generate_questions(dataset, tool, model="llama3-8b-8192"):
    prompt = load_prompt_template(tool).format(dataset=dataset)

    response = client.chat.completions.create(
        model=model,
        messages=[
            {"role": "system", "content": "너는 데이터 분석 문제를 만드는 AI야."},
            {"role": "user", "content": prompt}
        ],
        temperature=0.7,
        max_tokens=1000
    )

    raw_output = response.choices[0].message.content
    return clean_gpt_response(raw_output)

# 💾 정제된 문제 저장 함수
def save_questions(text):
    filtered = clean_gpt_response(text)
    with open(NEW_QUESTIONS_PATH, "a", encoding="utf-8") as f:
        f.write(filtered.strip() + "\n")

# ▶️ 테스트 실행
if __name__ == "__main__":
    dataset = choose_random_dataset()
    for tool in ["pds", "sql", "viz"]:
        result = generate_questions(dataset, tool)
        print(f"\n📘 생성된 문제 ({tool}):")
        print(result)
        save_questions(result)

# ✅ run_all.py와 연동 시: 매 실행마다 하나의 데이터셋만 무작위 선택되어 문제 생성됨

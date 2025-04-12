# 📁 gpt/generator.py (openai >= 1.0.0 대응 버전)
import openai
import os
from dotenv import load_dotenv
from tools.paths import (
    PROMPT_PATHS,            # 📂 도구별 프롬프트 템플릿 경로
    NEW_QUESTIONS_PATH,      # 📄 생성된 문제 저장 위치
    ENV_PATH                 # 🔐 환경 변수 (.env) 파일 경로
)

# 🔐 .env 파일에서 API 키 불러오기
load_dotenv(dotenv_path=ENV_PATH)
client = openai.OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

# 📥 템플릿 파일 로드 함수
def load_prompt_template(tool):
    """도구에 맞는 프롬프트 템플릿을 불러옵니다."""
    path = PROMPT_PATHS[tool]
    with open(path, "r", encoding="utf-8") as f:
        return f.read()

# 🚀 GPT에게 문제 생성 요청 함수 (openai>=1.0.0 버전)
def generate_questions(dataset, tool, model="gpt-3.5-turbo"):
    """GPT에게 문제를 요청하고 응답을 받아 반환합니다."""
    prompt = load_prompt_template(tool).format(dataset=dataset)

    response = client.chat.completions.create(
        model=model,
        messages=[
            {"role": "system", "content": "당신은 데이터 분석 문제를 만드는 AI입니다."},
            {"role": "user", "content": prompt}
        ],
        temperature=0.7,
        max_tokens=1000
    )

    return response.choices[0].message.content  # 🧠 응답 텍스트 추출

# 💾 생성된 문제를 파일에 저장하는 함수
def save_questions(text):
    with open(NEW_QUESTIONS_PATH, "a", encoding="utf-8") as f:
        f.write(text.strip() + "\n")

# 🧪 테스트 실행용: 문제 생성 후 저장까지
if __name__ == "__main__":
    dataset = "titanic"
    tool = "pds"
    result = generate_questions(dataset, tool)
    print("\n📘 생성된 문제:")
    print(result)
    save_questions(result)

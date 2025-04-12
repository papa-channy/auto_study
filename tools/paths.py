# 📁 tools/paths.py
import os

# 🧭 BASE_DIR: 프로젝트 루트 디렉토리 경로
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# 📂 주요 하위 디렉토리 경로
CONFIG_DIR = os.path.join(BASE_DIR, "config")
DATA_DIR = os.path.join(BASE_DIR, "data")
GPT_DIR = os.path.join(BASE_DIR, "gpt")
NOTION_DIR = os.path.join(BASE_DIR, "notion")
TOOLS_DIR = os.path.join(BASE_DIR, "tools")
SCRIPTS_DIR = os.path.join(BASE_DIR, "scripts")
NOTEBOOKS_DIR = os.path.join(BASE_DIR, "notebooks")  # 📓 노트북 저장 경로

# 📄 설정 관련 경로들
KEYWORDS_PATH = os.path.join(CONFIG_DIR, "keywords.json")
SETTINGS_PATH = os.path.join(CONFIG_DIR, "settings.json")
ACTIVE_STUDY_RANGE_PATH = os.path.join(CONFIG_DIR, "active_study_range.txt")
DATASET_LIST_PATH = os.path.join(CONFIG_DIR, "dataset_list.txt")
DIFFICULTY_MAP_PATH = os.path.join(CONFIG_DIR, "difficulty_map.txt")

# 📄 데이터 저장 파일 경로
NEW_QUESTIONS_PATH = os.path.join(DATA_DIR, "new_questions.txt")
ARCHIVED_QUESTIONS_PATH = os.path.join(DATA_DIR, "archived_questions.txt")

# 📄 도구별 최신 예시 파일 경로
RECENT_EXAMPLES = {
    "pds": os.path.join(GPT_DIR, "recent_examples_pandas.txt"),
    "sql": os.path.join(GPT_DIR, "recent_examples_sql.txt"),
    "viz": os.path.join(GPT_DIR, "recent_examples_viz.txt")
}

# 📄 프롬프트 템플릿 경로
PROMPT_PATHS = {
    "pds": os.path.join(GPT_DIR, "prompt_pandas.txt"),
    "sql": os.path.join(GPT_DIR, "prompt_sql.txt"),
    "viz": os.path.join(GPT_DIR, "prompt_viz.txt")
}

# 🔐 환경변수 파일 (.env)
ENV_PATH = os.path.join(BASE_DIR, ".env")

# 📦 requirements.txt 경로
REQUIREMENTS_PATH = os.path.join(BASE_DIR, "requirements.txt")
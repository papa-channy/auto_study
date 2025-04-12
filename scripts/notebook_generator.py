# 📁 scripts/notebook_generator.py
import os
import nbformat
from nbformat.v4 import new_notebook, new_markdown_cell, new_code_cell
from datetime import datetime
from tools.paths import NEW_QUESTIONS_PATH, NOTEBOOKS_DIR, ACTIVE_STUDY_RANGE_PATH, DIFFICULTY_MAP_PATH

# 📅 현재 날짜 기준 (YY/MM n주차) 폴더 이름 생성 함수
def get_week_folder():
    today = datetime.now()
    year_short = today.strftime("%y")
    month = today.strftime("%m")
    week_num = (today.day + today.replace(day=1).weekday() - 1) // 7 + 1
    return f"({year_short}/{month} {week_num}주차)"

# 🔧 도구별 첫 코드 셀: 라이브러리 import 템플릿
LIBRARY_IMPORTS = {
    "pds": "import pandas as pd\nimport seaborn as sns",
    "sql": "# SQL 환경 설정은 별도 노트 참고",
    "viz": "import matplotlib.pyplot as plt\nimport seaborn as sns"
}

# 📥 설정 파일 로딩 함수

def load_list(path):
    with open(path, "r", encoding="utf-8") as f:
        return [line.strip() for line in f if line.strip() and not line.startswith("#")]

def load_difficulty_map():
    difficulty_map = {}
    with open(DIFFICULTY_MAP_PATH, "r", encoding="utf-8") as f:
        for line in f:
            if ":" in line:
                tool, levels = line.strip().split(":", 1)
                difficulty_map[tool.strip()] = [lvl.strip() for lvl in levels.split(",")]
    return difficulty_map

# 📄 문제 불러오기
def load_questions():
    with open(NEW_QUESTIONS_PATH, "r", encoding="utf-8") as f:
        return [line.strip() for line in f if line.strip() and "|" in line]

# 📓 노트북 자동 생성 함수
def generate_notebooks():
    questions = load_questions()
    tools = load_list(ACTIVE_STUDY_RANGE_PATH)
    difficulty_map = load_difficulty_map()
    week_folder = get_week_folder()

    # 📁 주차별 폴더 생성
    folder_path = os.path.join(NOTEBOOKS_DIR, week_folder)
    os.makedirs(folder_path, exist_ok=True)

    # 📊 도구별 문제 묶기
    by_tool = {tool: [] for tool in tools}
    for q in questions:
        parts = q.split("|")
        if len(parts) != 5:
            continue
        tool_tag = parts[3].split("/")[0].strip().lower()
        if tool_tag in by_tool:
            by_tool[tool_tag].append(q)

    # 📓 도구별 ipynb 생성
    for tool in tools:
        nb = new_notebook()
        cells = []

        # 🧱 셀 1: 라이브러리 불러오기 코드
        lib_code = LIBRARY_IMPORTS.get(tool, "")
        if lib_code:
            cells.append(new_code_cell(lib_code))

        # 🔢 문제별 셀 구성
        for idx, line in enumerate(by_tool.get(tool, []), start=1):
            _, level, dataset, _, question = [p.strip() for p in line.split("|", 4)]
            markdown = f"## {idx}. {level}\n{question}"
            code = f"# {dataset} 데이터셋 로딩 예시\ndf = sns.load_dataset(\"{dataset}\")\ndf.head()"
            cells.append(new_markdown_cell(markdown))
            cells.append(new_code_cell(code))
            cells.append(new_markdown_cell("---"))  # 셀 구분선

        nb.cells = cells

        # 💾 노트북 저장
        file_path = os.path.join(folder_path, f"{tool}.ipynb")
        with open(file_path, "w", encoding="utf-8") as f:
            nbformat.write(nb, f)
        print(f"✅ {tool}.ipynb 생성 완료 → {file_path}")

# ▶️ 실행 엔트리 포인트
if __name__ == "__main__":
    generate_notebooks()
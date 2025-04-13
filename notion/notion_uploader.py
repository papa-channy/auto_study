# 📁 notion/notion_uploader.py (✅ 로깅/검사 추가 버전 + 한글 필터 강화 + 프롬프트 개선 예정)
import sys, os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import json
from dotenv import load_dotenv
from notion_client import Client
from datetime import datetime
from tools.paths import KEYWORDS_PATH, NEW_QUESTIONS_PATH, ENV_PATH

class NotionUploader:
    def __init__(self):
        self.question_file = NEW_QUESTIONS_PATH
        self.keyword_map = self.load_keyword_map(KEYWORDS_PATH)

        load_dotenv(dotenv_path=ENV_PATH)
        self.api_key = os.getenv("NOTION_API_KEY")
        self.database_id = os.getenv("NOTION_DATABASE_ID")

        print(f"🔐 NOTION_API_KEY 시작: {self.api_key[:10]}...")
        print(f"📘 NOTION_DATABASE_ID: {self.database_id}")

        self.notion = Client(auth=self.api_key)

    def load_keyword_map(self, path):
        with open(path, "r", encoding="utf-8") as f:
            return json.load(f)

    def classify(self, text):
        categories = []
        for category, keywords in self.keyword_map.items():
            if any(k in text for k in keywords):
                categories.append(category)
        return list(set(categories))

    def upload(self):
        with open(self.question_file, "r", encoding="utf-8") as f:
            lines = [
                line for line in f.readlines()
                if (line.strip().startswith("1|") or line.strip().startswith("2|") or line.strip().startswith("3|"))
                and any("가" <= ch <= "힣" for ch in line)  # 한글 포함 여부 체크
            ]

        for line in lines:
            if line.count("|") < 4:
                print(f"❌ 잘못된 형식: {line.strip()}")
                continue

            try:
                번호, 난이도, 데이터셋, 분류명, 질문 = [part.strip() for part in line.strip().split("|", 4)]
            except ValueError:
                print(f"❌ 파싱 실패: {line.strip()}")
                continue

            분류_목록 = [분류명] if 분류명 else self.classify(질문)

            try:
                today = datetime.now().strftime("%m/%d")
                self.notion.pages.create(
                    parent={"database_id": self.database_id},
                    properties={
                        "날짜": {"rich_text": [{"text": {"content": today}}]},
                        "dataset": {"select": {"name": 데이터셋}},
                        "문제": {"rich_text": [{"text": {"content": 질문}}]},
                        "분류": {"multi_select": [{"name": tag} for tag in 분류_목록]} if 분류_목록 else {},
                        "난이도": {"select": {"name": 난이도}},
                        "상태": {"select": {"name": "미풀이"}},
                    }
                )
                print(f"✅ {번호} 업로드 성공 | 분류: {', '.join(분류_목록) if 분류_목록 else '없음'}")
            except Exception as e:
                print(f"❌ {번호} 업로드 실패: {e}")

if __name__ == "__main__":
    uploader = NotionUploader()
    uploader.upload()

# 💬 다음 단계: GPT 프롬프트를 한글로 엄격하게 지시하는 방식으로 개선 예정!

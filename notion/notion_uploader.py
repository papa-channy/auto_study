# 📁 notion/notion_uploader.py
import os
import json
from dotenv import load_dotenv
from notion_client import Client
from datetime import datetime
from tools.paths import KEYWORDS_PATH, NEW_QUESTIONS_PATH, ENV_PATH

class NotionUploader:
    def __init__(self):
        self.question_file = NEW_QUESTIONS_PATH  # 📄 문제 파일 경로
        self.keyword_map = self.load_keyword_map(KEYWORDS_PATH)  # 🧠 자동 분류 키워드 로딩

        load_dotenv(dotenv_path=ENV_PATH)  # 🔐 API 키 로드
        self.notion = Client(auth=os.getenv("NOTION_API_KEY"))
        self.database_id = os.getenv("NOTION_DATABASE_ID")

    def load_keyword_map(self, path):
        """JSON 파일에서 분류 키워드 불러오기"""
        with open(path, "r", encoding="utf-8") as f:
            return json.load(f)

    def classify(self, text):
        """문제 내용 기반 자동 분류 수행"""
        categories = []
        for category, keywords in self.keyword_map.items():
            if any(k in text for k in keywords):
                categories.append(category)
        return list(set(categories))  # 중복 제거 후 반환

    def upload(self):
        """문제 파일을 읽어 노션에 한 줄씩 업로드"""
        with open(self.question_file, "r", encoding="utf-8") as f:
            lines = f.readlines()

        for line in lines:
            if line.count("|") < 4:
                print(f"❌ 잘못된 형식: {line.strip()}")
                continue

            try:
                번호, 난이도, 데이터셋, 분류명, 질문 = [part.strip() for part in line.strip().split("|", 5)]
                분류_목록 = [분류명] if 분류명 else self.classify(질문)

                today = datetime.now().strftime("%m/%d")
                self.notion.pages.create(
                    parent={"database_id": self.database_id},
                    properties={
                        "날짜": {"rich_text": [{"text": {"content": today}}]},
                        "dataset": {"select": {"name": 데이터셋}},
                        "문제": {"rich_text": [{"text": {"content": 질문}}]},
                        "분류": {"multi_select": [{"name": tag} for tag in 분류_목록]} if 분류_목록 else {},
                        "난이도": {"select": {"name": 난이도}},
                        "상태": {"select": {"name": "미풀이"}},  # ✅ 기본 상태 설정
                    }
                )
                print(f"✅ {번호} 업로드 성공 | 분류: {', '.join(분류_목록) if 분류_목록 else '없음'}")
            except Exception as e:
                print(f"❌ {번호} 업로드 실패: {e}")
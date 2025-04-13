# 📊 Notion 기반 데이터 분석 문제 자동화 시스템 (Groq 기반 버전)

> GPT 문제 생성 → Notion 업로드 → .ipynb 자동 생성 → 리포트 저장까지! ✨
> **한 큐에 학습을 자동화하는 통합형 CLI 도구**

---

## 📌 프로젝트 소개

- GPT를 활용해 Pandas / SQL / 시각화 문제를 자동 생성하고,
- Notion에 자동 업로드 + 주차별 `.ipynb` 학습 노트북도 자동 생성!
- 문제 백업, 자동 리포트 저장, 크론 자동 실행까지 지원합니다.

이제는 OpenAI가 아닌 **Groq 기반 무료 LLM**을 사용하여 실행 비용 없이 전자동화 가능!

---

## 📂 폴더 구조

```bash
auto_study/
├── config/                # 설정 파일 (도구, 난이도, 키워드 등)
├── data/                  # 문제 저장 및 아카이브 파일
├── gpt/                   # 프롬프트 템플릿 & GPT 호출기
├── notion/                # Notion 업로더
├── scripts/               # 실행 스크립트 및 자동화 컨트롤러
├── tools/                 # 경로 관리, 아카이브, 리포트 등 유틸
├── notebooks/             # 매주 생성된 ipynb 노트북
├── logs/                  # 자동 생성된 리포트
├── .env                   # 🔐 API 키 및 노션 DB ID
└── requirements.txt       # 필요한 라이브러리 목록
```

---

## ⚙️ 설정 방법

### 1️⃣ 환경 변수 설정 (`.env`)
```env
GROQ_API_KEY=gsk-xxxxxxxxxxxxxxxxxxx
NOTION_API_KEY=secret_xxxxxxxxxxxxx
NOTION_DATABASE_ID=xxxxxxxxxxxxxxxxx
```

### 2️⃣ 필수 패키지 설치
```bash
pip install -r requirements.txt
```

### 3️⃣ Notion 데이터베이스 필드 구조
```
속성명    | 타입
-----------|------------
날짜       | 텍스트
문제       | 텍스트
dataset    | Select
난이도     | Select
분류       | Multi-select
상태       | Select
```

> 🔐 필드명은 코드에 하드코딩되어 있으므로 띄어쓰기와 대소문자까지 동일하게 설정해야 합니다.

---

## 🚀 실행 방법

### 수동 실행
```bash
python scripts/custom_setting.py  # 설정 커스터마이징 (도구/데이터셋/난이도 등)
python scripts/run_all.py         # 전체 자동화 한 번에 실행
```

### 크론 자동화 등록
```bash
chmod +x setup/auto_cron.sh     # 실행 권한 부여 (최초 1회)
./setup/auto_cron.sh            # 매주 월요일 오전 9시 자동 실행 등록
```

---

## 📦 자동화 흐름 요약

1. `scripts/run_all.py` 실행 시 다음이 순차적으로 실행됩니다:
   - ✅ GPT 문제 생성 (Groq 기반 llama3 모델 사용)
   - ✅ 프롬프트 템플릿 갱신
   - ✅ Notion 업로드
   - ✅ 문제 아카이브 및 초기화
   - ✅ `.ipynb` 노트북 자동 생성
   - ✅ 리포트 파일 자동 저장 (`logs/`)

---

## 📑 문제 생성 양식 예시

```
1 | 중 | tips | pds/데이터 전처리 | 결측치를 제거하세요.
2 | 상 | titanic | pds/시각화 | 생존자 수를 막대 그래프로 시각화하세요.
```

---

## 🙋‍♀️ 제작자
- 만든 사람: **찬이** 🩵
- 시스템 설계 & 확장 도우미: **ChatGPT + Groq + Notion API**

---

## 💬 다음 계획
- 📦 문제 유형별 정답 예시 연동
- 📘 문제 추천 로그 분석 기능
- 🧠 학습 진척도 기반 추천 알고리즘 연동

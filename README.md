# 📊 Notion 기반 데이터 분석 문제 자동화 시스템

> GPT 문제 생성 → Notion 업로드 → .ipynb 자동 생성 → 리포트 저장까지! ✨
> **한 큐에 학습을 자동화하는 통합형 CLI 도구**

---

## 📌 프로젝트 소개

- GPT를 활용해 Pandas / SQL / 시각화 문제를 자동 생성하고,
- Notion에 자동 업로드 + 주차별 `.ipynb` 학습 노트북도 자동 생성!
- 문제 백업, 자동 리포트 저장, 크론 자동 실행까지 지원합니다.

처음에는 수작업으로 문제를 정리했지만, 
학습 루틴을 자동화하고자 GPT와 실시간으로 구조를 설계하고, 
지금의 자동화 파이프라인으로 발전시켰습니다. 🛠️

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
OPENAI_API_KEY=sk-...
NOTION_API_KEY=secret_...
NOTION_DATABASE_ID=xxxxxxxx...
```

### 2️⃣ 필수 패키지 설치
```bash
pip install -r requirements.txt
```

### 3️⃣ Notion 데이터베이스 필드 구조
날짜	텍스트
문제	텍스트      
dataset	Select          
난이도	Select
분류	Multi-select
상태    Select

> 🔐 필드명은 코드에 하드코딩되어 있으므로 띄어쓰기와 대소문자까지 동일하게 설정해야 합니다.

---

## 🚀 실행 방법

### 기본 실행 (수동 실행)
```bash
python scripts/custom_setting.py  # 설정 커스터마이징 (도구/데이터셋/난이도 등)
python scripts/run_all.py         # 전체 자동화 한 번에 실행
```

### 크론 자동화 실행 등록
```bash
chmod +x setup/auto_cron.sh     # 실행 권한 부여 (최초 1회)
./setup/auto_cron.sh            # 크론 등록
```

> 매주 월요일 오전 9시 자동으로 `run_all.py`가 실행됩니다.
> 결과는 `logs/report_YYYY-MM-DD.txt`에 자동 저장됩니다.

---

## 📦 자동화 흐름 요약

1. `scripts/run_all.py` 실행 시 다음 과정이 순차적으로 처리됩니다:
   - GPT 문제 생성
   - 프롬프트 템플릿 갱신
   - Notion 업로드
   - 문제 아카이브 및 초기화
   - 노트북(.ipynb) 생성
   - 실행 리포트 저장

---

## 📑 문제 생성 양식

```
번호 | 난이도 | 데이터셋 | 분류 | 문제 내용
예: 1 | 중 | tips | pds/데이터 전처리 | 결측치를 제거하세요.
```

---

## 🙋‍♀️ 제작자
- 만든 사람: 찬
- GPT와 실시간 협업으로 설계한 완전 자동화 시스템

---

## 💬 다음 계획
- ✅ OpenAI → 무료 LLM(OpenRouter 등) 우회 적용 예정
- ✅ zip 자동 백업 기능 예정
- ✅ 문제 추천 기록 기반으로 학습 분석 기능 추가?

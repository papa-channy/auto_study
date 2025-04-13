# 📘 weekly_settings.py
# ------------------------------
# ✅ 자동화 전체 흐름을 제어하는 통합 설정 파일
# ------------------------------
# 이 파일은 custom_setting.py 및 모든 자동화 스크립트가 참조하는
# "최종 설정값 요약 버전"으로, 자동으로 작성되거나 사용자가 직접 수정할 수 있습니다.
#
# 📌 실제 자동 실행 대상은 아님 (자동화 컨트롤러 역할)
#
# 설정 항목:
# - ACTIVE_STUDY_RANGES: 도구 약어 리스트 (예: pds, sql, viz)
# - DATASETS: 사용할 데이터셋 리스트
# - DIFFICULTY_MAP: 도구별 난이도 설정 (난이도 개수 × 호출 횟수 = 문제 수)
# - TOTAL_WEEKLY_PROBLEMS: 주당 총 문제 목표 수
# - PROBLEMS_PER_BATCH: GPT에게 한 번에 요청할 문제 수
# - NUM_BATCHES_PER_WEEK: 주당 GPT 호출 횟수
# - START_DATE: 기준 주차 계산용 시작일

ACTIVE_STUDY_RANGES = ["pds"]

DATASETS = [
    "titanic", "tips", "iris", "penguins",
    "flights", "diamonds", "mpg", "car_crashes"
]

DIFFICULTY_MAP = {
    "pds": ["중", "상", "최상"],
    

    # TOTAL_WEEKLY_PROBLEMS = 9
    # PROBLEMS_PER_BATCH = 3
    # NUM_BATCHES_PER_WEEK = 1
    # START_DATE = "2024-01-01"    오류 수정하기기
}
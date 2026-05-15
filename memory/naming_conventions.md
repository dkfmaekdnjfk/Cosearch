---
name: 명명 규칙
description: Obsidian 파일명 접두사, 코드 파일 명명 규칙, 결과물 폴더 구조, legacy 정의
type: reference
---

# 명명 규칙

## Obsidian 파일명 접두사

| 접두사 | 폴더 | 용도 | 예시 |
|--------|------|------|------|
| `EXP` | `50_Experiments/` | 분석/실험 세션 노트 | `EXP 260417 세션주제.md` |
| `MTG` | `50_Experiments/` | 미팅/발표 노트 | `MTG 260417 lab meeting.md` |
| `DR` | `70_Reviews/` | 딥리서치 결과 원본 | `DR 260416 주제.md` |
| `REV` | `70_Reviews/` | 코드/분석 리뷰 | `REV 260416 Analysis.md` |

`99_Assets/`는 이미지·PDF 등 바이너리 파일 전용 — `.md` 파일 금지.

---

## 코드 파일 명명 규칙

| 종류 | 위치 | 명명 | 예시 |
|------|------|------|------|
| 분석 실행 스크립트 (.py) | `code/scripts/` | `topic_YYMMDD.py` | `pca_quiet_trajectory_260515.py` |
| 탐색적 노트북 (.ipynb) | `code/notebooks/` | `topic_YYMMDD.ipynb` | `exploratory_pca_260515.ipynb` |
| 패키지·유틸리티 | `code/<package_name>/` | snake_case, 날짜 없음 | `trial_seg/loader.py` |

**날짜는 topic 뒤에**: 파일은 주제로 검색하고, 날짜는 버전 식별용.
EXP 노트와 스크립트 날짜가 대응되어야 한다 (`EXP 260515 ...` ↔ `*_260515.py`).

---

## 결과물 폴더 구조

```
results/runs/
  YYMM/                    ← 월 단위 그룹
    YYMMDD_topic/          ← 날짜_주제 (날짜 먼저)
      figures/
      *.csv
      *.pkl
```

예: `results/runs/2605/260515_pca_quiet_traj/`

| 폴더 | 용도 | Git |
|------|------|-----|
| `results/runs/` | 신규 스크립트 출력 | ❌ 로컬 전용 |
| `results/final/` | 논문·발표용 최종 선별 figure | ✅ 추적 |
| `results/legacy/` | 이전 구조 아카이브 (읽기 전용) | ❌ 로컬 전용 |

---

## 설정 파일

공유 입력 파일(세션 설정, 파라미터 JSON 등)은 `config/`에 저장 (git 추적).

```
config/
  sessions/    ← 세션 설정 JSON
  params/      ← 분석 파라미터
```

---

## Legacy 폴더 정의

`code/legacy/`, `results/legacy/`, `data/legacy/`는 **이전 구조의 파일을 일괄 이동한 것**.
"사용하지 않는다"는 의미가 아님 — 현재도 참조·실행 가능한 코드/데이터 포함.
Legacy 스크립트를 재사용하려면 `code/scripts/`에 날짜 포함 이름으로 복사 후 정식 등록.

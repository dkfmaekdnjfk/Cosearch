---
name: 명명 규칙
description: Obsidian 파일명 접두사 및 코드 파일 명명 규칙
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

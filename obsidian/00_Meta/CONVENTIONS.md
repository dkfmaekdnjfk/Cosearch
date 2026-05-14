---
title: "CONVENTIONS"
tags:
  - meta
  - conventions
date-modified: YYYY-MM-DD
---

# Obsidian Vault 규칙

## 파일명 접두사

| 접두사 | 폴더 | 용도 | 예시 |
|--------|------|------|------|
| `EXP` | `50_Experiments/` | 분석/실험 세션 노트 | `EXP 260417 세션주제.md` |
| `MTG` | `50_Experiments/` | 미팅/발표 노트 | `MTG 260417 lab meeting.md` |
| `DR` | `70_Reviews/` | 딥리서치 결과 원본 | `DR 260416 주제.md` |
| `REV` | `70_Reviews/` | 코드/분석 리뷰 | `REV 260416 Analysis.md` |

`99_Assets/`는 이미지·PDF 등 바이너리 파일 전용 — `.md` 파일 금지.

---

## EXP 노트 frontmatter

```yaml
---
title: "EXP YYMMDD 세션주제"
tags:
  - experiment
  - [관련 태그]
status: complete
date-experiment: YYYY-MM-DD
date-created: YYYY-MM-DD
date-modified: YYYY-MM-DD
---
```

---

## 폴더 용도

| 폴더 | 용도 |
|------|------|
| `00_Meta/` | 프로젝트 현황 (PROJECT_STATUS.md), 규칙 (CONVENTIONS.md) |
| `10_Literature/` | 논문 노트 (citekey 기반, `저자연도_키워드.md`) |
| `20_Concepts/` | 이론·개념 노트 |
| `30_Methodology/` | 분석 방법론 문서 (best practice, 파이프라인 기준) |
| `40_Projects/` | 진행 중 분석 파이프라인 노트 |
| `50_Experiments/` | EXP·MTG 노트 (날짜 기반) |
| `60_Plans/` | 계획, 로드맵, 다음 단계 |
| `70_Reviews/` | DR·REV 파일 |
| `99_Assets/` | 이미지, PDF (바이너리 전용) |

---

## 코드·데이터·결과물 구조

```text
code/
  cosearch/       Cosearch 프레임워크 패키지 (경로 관리, 유틸리티)
  scripts/        실행 스크립트 (run_*.py, preprocess_*.py 등)
  pipelines/      파이프라인 설정 파일 (*.yaml)
  notebooks/      탐색적 분석용 Jupyter 노트북
  tests/          테스트 코드

data/
  examples/       Git 추적 가능한 소형 예시 데이터
  raw/            원본 데이터 (Git 제외, 로컬 전용)
  processed/      전처리 결과 (Git 제외, 로컬 전용)

results/
  final/          최종 결과물 (Git 추적 가능 — 논문/보고서용 그림·표)
  logs/           실행 로그 (Git 제외)
  tmp/            임시 출력 (Git 제외)
```

### Tracking policy

Git tracks: `code/`, `obsidian/`, `data/examples/`, `results/final/`, configs, small samples.

Git does NOT track: `data/raw/`, `data/processed/`, `results/logs/`, `results/tmp/`, large binaries, caches, secrets.

Every untracked artifact that matters must be referenced from the relevant EXP note with path, command, source, and checksum when possible.

---

## EXP 노트 코드 실행 섹션

코드를 실행한 세션의 EXP 노트에는 다음 섹션을 추가한다.

```markdown
## Code
- `code/scripts/run_example.py`

## Input
- `data/raw/dataset.csv` *(local only)*

## Command
```bash
python code/scripts/run_example.py --config code/pipelines/example.yaml
```

## Output
- Tracked: `results/final/summary.csv`
- Local only: `results/logs/run_260514.log`

## Result
주요 결과 요약.

## Next
다음 단계.
```

---

## 코드·데이터·결과물 추적 규칙

### Git 추적 대상

| 종류 | 경로 |
|------|------|
| 분석 코드 | `code/` (`legacy/` 제외) |
| Obsidian 노트 | `obsidian/` |
| 폴더 설명 문서 | `code/README.md`, `data/README.md`, `results/README.md` |
| 대용량 파일 목록 | `artifacts/manifest.yaml` |
| 최종 결과물 | `results/final/` |
| 예시 데이터 | `data/examples/` |

### Git 제외 대상 (로컬 전용)

| 종류 | 경로 |
|------|------|
| 원본 데이터 | `data/raw/` |
| 전처리 데이터 | `data/processed/` |
| 중간·임시 결과물 | `results/logs/`, `results/tmp/` |

### 새 대용량 파일이 생길 때 할 일

1. **`artifacts/manifest.yaml`에 항목 추가** — `local_path`, `note`, `created_by` 기록
2. **관련 EXP 노트에 경로 기록** — Output/Command 섹션에 명시
3. `results/final/`에 넣을 최종본만 Git에 추가

---

## EXP 노트 코드 실행 섹션

코드를 실행한 세션의 EXP 노트에 추가:

```markdown
## Code
- `code/scripts/run_example.py`

## Input
- `data/processed/...` *(local only)*

## Command
```bash
PYTHONPATH=code python code/scripts/run_example.py --config ...
```

## Output
- Tracked: `results/final/summary.png`
- Local only: `results/tmp/YYMMDD_topic/`

## Result
주요 결과 요약.

## Next
다음 단계.
```

---

## Literature 노트 frontmatter

```yaml
---
title: "논문 제목"
tags: [literature, 주제태그]
citekey: 저자연도_키워드
authors: "저자1, 저자2"
year: YYYY
journal: "저널명"
doi: "10.xxxx/xxxxx"
pmid: "XXXXXXXX"
status: unread
importance: 3   # 1~5
date-created: YYYY-MM-DD
date-modified: YYYY-MM-DD
---
```

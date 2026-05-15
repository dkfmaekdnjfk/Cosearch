# [Project Name] — Claude Instructions

## 프로젝트 개요

[프로젝트 설명을 여기에 작성]

분석 현황: `memory/project_experiment_status.md` | 명명 규칙: `memory/naming_conventions.md`

> **온보딩 확인** — 세션 시작 시 `obsidian/00_Meta/START_HERE.md`의 `onboarded` 필드를 확인할 것.
> `false`이면 파일을 읽고 사용자에게 세팅 순서를 안내한 뒤, 완료 시 `onboarded: true`로 업데이트한다.
> `true`이면 이 과정을 건너뛴다.

> **Cosearch 동기화 확인** — 세션 시작 시 `.claude/skills/sync-from-cosearch/last_sync.txt`를 확인할 것.
> 파일이 없거나 마지막 동기화로부터 14일 이상 지났으면 사용자에게 안내:
> "Cosearch 템플릿 업데이트 확인이 14일 이상 지났습니다. `/sync-from-cosearch`를 실행해보세요."

---

## 핵심 경로

### 코드

| 역할 | 경로 |
|------|------|
| 분석 스크립트 | `code/scripts/` |
| 파이프라인 설정 | `code/pipelines/` |
| 노트북 | `code/notebooks/` |
| Cosearch 패키지 | `code/cosearch/` |
| 테스트 | `code/tests/` |
| 기존 코드 (legacy) | `code/legacy/` |

### 데이터

| 역할 | 경로 |
|------|------|
| 예시 데이터 | `data/examples/` |
| 원본 데이터 | `data/raw/` (로컬) |
| 전처리 데이터 | `data/processed/` (로컬) |

### 결과물

| 역할 | 경로 |
|------|------|
| 신규 스크립트 출력 | `results/runs/YYMM/YYMMDD_topic/` (로컬) |
| 최종 결과물 (git 추적) | `results/final/` |
| cosearch 이전 아카이브 | `results/legacy/` (로컬) |
| 실행 로그 | `results/logs/` (로컬) |
| 임시 출력 | `results/tmp/` (로컬) |

### 설정

| 역할 | 경로 |
|------|------|
| 세션 설정 | `config/sessions/` |
| 분석 파라미터 | `config/params/` |

### 기타

| 역할 | 경로 |
|------|------|
| Obsidian vault | `obsidian/` |
| 메모리 | `~/.claude/projects/[인코딩된-경로]/memory/` |

---

## ⚠️ 작업 진행 방식

- **작업 전 반드시 확인** — 무엇을 할지 먼저 설명하고 승인받은 후 진행. "continue" 같은 말만으로 임의 판단해서 실행하지 말 것

- **코드 파일 이동·재구조화 시** — `obsidian/00_Meta/START_HERE.md` > "코드 재구조화 안전 절차" 섹션을 반드시 따를 것

---

## ⚠️ 필수 원칙

- **의도 불명확 시 되물을 것** — 세션/케이스/비교 기준이 애매하면 임의 판단 말고 먼저 확인
- **결론**: 단일 지표로 결론 내리지 말 것
- **파일 탐색**: 재귀 `ls -R` 금지. 파일 크기 먼저 확인 후 필요한 부분만 읽기

---

## Obsidian 구조

`00_Meta/` 현황·규칙 | `10_Literature/` | `20_Concepts/` | `30_Methodology/` | `40_Projects/`
`50_Experiments/` EXP·MTG | `60_Plans/` | `70_Reviews/` DR·REV | `99_Assets/` 이미지·PDF 전용

---

## 스킬

| 스킬 | 위치 | 용도 |
|------|------|------|
| `session-wrap` | `.claude/skills/` | 세션 마무리 — EXP 노트 + 메모리 업데이트 |
| `organize-deepresearch` | `.claude/skills/` | DR 파일 → Obsidian 흡수 |
| `write-critical-review` | `.agents/skills/` | 프로젝트 파일을 읽고 peer review 수준의 비판적 리뷰 작성 |

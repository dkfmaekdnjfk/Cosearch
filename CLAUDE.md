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

## 근거와 해석 기록

- 수치·판정에는 원문 근거 위치(`파일:줄`, 표 번호·행·열)를 함께 기록한다.
- 메모리·현황 요약은 탐색 시작점이다. 주장에 사용하기 전에 원문 근거를 직접 연다.
- 분석을 설명할 때 계산 절차와 함께 연구질문에서 무엇을 구별하고 어떤 실제 현상을
  이해하게 하는지 적는다. 계산 결과와 기전 해석·추론을 구별한다.
- 결과·그림 해설의 논리 연결은 `research-interpretation-review` 스킬로 점검한다.
  실제 비교 대상과 기준, 그림에서 판단할 부분, 해석이 성립하는 조건을 연결한다.
  설명 점검 요청을 추가 분석·그림 제작·검사 파일 작성으로 확대하지 않는다.
- 주장을 철회하거나 수정할 때 관련 문서를 검색하여 같은 전제에 의존하는 곳을 확인한다.
- 코드의 핵심 로직을 재사용하면 원본을 복사한 뒤 변경 부분만 수정한다.
  주제만 비슷하고 본체가 다르면 새로 작성하되 참조한 스캐폴딩의 출처를 기록한다.
- 용어는 원문과 표준 정의를 확인한다. 용어집과 운영 절차의 정본은
  `obsidian/00_Meta/GLOSSARY.md`다. 새 명칭은 사용 전 충돌 점검과 정의 등재를 마친다.
  금지어는 대체하고 감시어는 정의를 대조한다. 윤문에는 `korean-copy` 스킬과 용어집을 함께 적용한다.

## 답변·작성 전 검증

- 답변 전 `obsidian/00_Meta/ANSWER_GATES.md`, Obsidian 작성 전 `WRITE_GATES.md`를 적용한다.
- Claude 훅은 질문을 컨텍스트에 주입한다. 다른 환경에서는 해당 노트를 직접 읽는다.
- 질문은 검증 절차이며 작업 승인이나 권한을 새로 부여하지 않는다.

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
| `scientific-figure` | `.claude/skills/` | 기존 Nature 디자인 시스템과 연계한 figure 설계·제작·자료 및 최종 출력 검수 |
| `full-methods` | `.claude/skills/` | 실제 코드·원문 대조와 입력·산출물·재현 근거를 연결한 HTML 연구 보고서 작성 |
| `korean-copy` | `.claude/skills/` | 한국어 문구 규칙·점검, 전문 용어 영문 원문 우선 |
| `research-interpretation-review` | `.claude/skills/` | 연구질문·비교 기준·figure 표현·실제 현상의 해석 연결 점검 |
| `session-wrap` | `.claude/skills/` | 세션 마무리 — EXP 노트 + 메모리 업데이트 |
| `organize-deepresearch` | `.claude/skills/` | DR 파일 → Obsidian 흡수 |
| `write-critical-review` | `.agents/skills/` | 프로젝트 파일을 읽고 peer review 수준의 비판적 리뷰 작성 |

# [Project Name] — Claude Instructions

## 프로젝트 개요

[프로젝트 설명을 여기에 작성]

분석 현황: `memory/project_experiment_status.md` | Vault 규칙: `obsidian/00_Meta/CONVENTIONS.md`

> **온보딩 확인** — 세션 시작 시 `obsidian/00_Meta/START_HERE.md`의 `onboarded` 필드를 확인할 것.
> `false`이면 파일을 읽고 사용자에게 세팅 순서를 안내한 뒤, 완료 시 `onboarded: true`로 업데이트한다.
> `true`이면 이 과정을 건너뛴다.

---

## 핵심 경로

| 역할 | 경로 |
|------|------|
| 에이전트 스크립트 | `agent/` |
| 결과물 | `results/` |
| Obsidian vault | `obsidian/` |
| 메모리 | `~/.claude/projects/[인코딩된-경로]/memory/` |

---

## ⚠️ 작업 진행 방식

- **작업 전 반드시 확인** — 무엇을 할지 먼저 설명하고 승인받은 후 진행. "continue" 같은 말만으로 임의 판단해서 실행하지 말 것

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

| 스킬 | 용도 |
|------|------|
| `session-wrap` | 세션 마무리 — EXP 노트 + 메모리 업데이트 |
| `organize-deepresearch` | DR 파일 → Obsidian 흡수 |

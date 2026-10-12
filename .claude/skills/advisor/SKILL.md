---
name: advisor
description: |
  연구 방향 독립 진단 스킬. 격리된 에이전트를 소환하여 ADVISOR.md 원칙에 따라
  연구의 필요성·증거 적합성·반론을 검토하고 결과를 70_Reviews/에 저장한다.
  "advisor 실행", "연구 방향 검토", "advisor 돌려줘", "방향 진단해줘",
  "advisor 써줘" 등의 말이 나오면 이 스킬을 사용할 것.
---

# Advisor 스킬

격리된 에이전트를 소환하여 현재 연구 방향을 독립적으로 진단한다.
에이전트는 이 대화의 맥락을 모르는 상태에서 파일만 보고 판단한다.

---

## Step 1: 핵심 파일 위치 확인

아래 파일들이 존재하는지 확인한다:

| 파일 | 역할 |
|------|------|
| `ADVISOR.md` (프로젝트 루트) | advisor 행동 원칙 |
| `obsidian/00_Meta/PROJECT_STATUS.md` | 논문 Claim + 현재 병목 + 실험 현황 |

사용자가 지정한 추가 파일과 현황에서 연결한 원문 근거를 포함한다. 진단 범위를
결정하는 정보가 빠졌을 때만 사용자에게 묻는다. 모델은 사용자 지정이 있으면 따르고,
없으면 실행 환경의 기본 모델을 사용한다.

---

## Step 2: 에이전트 소환

아래 프롬프트로 에이전트를 소환한다.
`[PROJECT_ROOT]`는 실제 프로젝트 루트 경로로 치환한다.

```
당신은 연구 advisor입니다. 아래 파일들을 순서대로 읽고 분석을 수행하세요.

**읽을 파일 (필수):**
1. [PROJECT_ROOT]/ADVISOR.md — 당신이 따라야 할 행동 원칙
2. [PROJECT_ROOT]/obsidian/00_Meta/PROJECT_STATUS.md — 논문 Claim, 현재 병목, 실험 현황

**읽을 파일 (선택, 있으면):**
[추가 파일 목록]

**수행할 작업:**
ADVISOR.md의 세 층위를 사고 도구로 사용해 진단하세요. 출력은 층위별 칸을
채우기보다 큰 목표 대비 현재 위치, 밀어붙일 방향과 근거, 다음 행동을 설명하세요.
이전 advisor 리뷰를 읽지 말고, 현황에서 지목한 코드·원자료·본문 근거를 직접 확인하세요.

주의:
- 칭찬이나 격려로 시작하지 않는다
- 층위 1 질문에 명확한 답이 없으면 없다고 말한다
- 필요하면 현재 방향 전체를 갈아엎으라고 말할 수 있다
- 분석 후 [PROJECT_ROOT]/obsidian/70_Reviews/REV YYMMDD advisor [주제].md에 직접 저장한다
- frontmatter: title, tags: [review, advisor], date-created, status: complete
- 저장한 파일 경로를 반환한다
```

---

## Step 3: 결과 저장

에이전트가 저장한 파일을 다시 읽어 내용과 저장 위치를 확인한다. 저장 도구를 사용할 수
없는 환경에서는 메인 에이전트가 반환된 분석을 원문 그대로 저장한다.

- 저장 경로: `obsidian/70_Reviews/`
- 파일명: `REV YYMMDD advisor [주제].md` (오늘 날짜 + 진단 주제 한 줄)
- frontmatter:
```yaml
---
title: "REV YYMMDD advisor [주제]"
tags: [advisor, review]
date-created: YYYY-MM-DD
status: complete
---
```

저장 완료 후 사용자에게 파일 경로를 알려준다.

---
title: "START HERE"
tags:
  - meta
  - onboarding
onboarded: false
date-created: YYYY-MM-DD
---

# 이 시스템은 무엇인가

AI와 연구를 하면서 생기는 근본적인 문제가 있다: **AI는 세션이 끊기면 맥락을 전부 잃는다.**

이 프로젝트는 그 문제를 해결하기 위해 Obsidian을 **AI의 외부 기억 저장소**로 쓴다. 사람이 읽는 노트이기도 하지만, 본질적인 목적은 다음 세션의 AI가 이 폴더를 읽고 "지금 이 프로젝트가 어디쯤 있고, 무엇을 알고, 무엇을 모르는지"를 복원할 수 있도록 구조화된 기록을 쌓는 것이다.

## 시스템의 세 축

| 축 | 역할 |
|----|------|
| **Obsidian** (`obsidian/`) | AI + 사람이 함께 읽는 전체 기억 저장소. 논문, 방법론, 실험 기록, 개념 정리 |
| **Claude 메모리** (`~/.claude/.../memory/`) | Claude 전용 압축 스냅샷. 세션 시작 시 빠르게 현재 상태 파악 |
| **스킬 + 훅** (`.claude/`) | 두 축을 자동으로 연결하고 유지 (`/session-wrap`, `/organize-deepresearch`) |

세션이 끝날 때마다 기록을 남기는 것이 이 시스템의 핵심이다. 기록이 쌓일수록 AI가 더 깊은 맥락으로 작업할 수 있다.

---

# 처음 세팅 (1회)

## 1. CLAUDE.md 채우기

프로젝트 루트의 `CLAUDE.md`를 열어 플레이스홀더를 교체한다:

- `[Project Name]` → 실제 프로젝트명
- `[프로젝트 설명을 여기에 작성]` → 한두 줄 요약
- 경로 테이블 → 실제 폴더 구조에 맞게 수정

## 2. Obsidian vault 열기

Obsidian에서 `obsidian/` 폴더를 새 vault로 연다.
(Obsidian → Open folder as vault → 이 프로젝트의 `obsidian/` 선택)

## 3. 이 vault의 폴더 구조 파악

`00_Meta/CONVENTIONS.md`를 읽는다. 어떤 폴더에 어떤 노트가 들어가는지, 파일명 규칙이 뭔지 5분이면 파악된다.

## 4. 프로젝트 현황 초안 작성

`00_Meta/PROJECT_STATUS.md`를 열어 현재 상태를 채운다:
- 지금 어느 단계인가
- 당장 해결해야 할 것이 무엇인가
- 다음에 할 일이 무엇인가

## 5. 이해도 체크리스트 채우기

`00_Meta/Understanding_Checklist.md`를 열어 이 프로젝트에서 이해해야 할 핵심 개념들을 `❓`로 채운다. 이해가 생길 때마다 `⚠️` → `✅`로 업데이트한다.

AI가 이 파일을 보면 "사용자가 무엇을 알고 모르는지"를 파악해 설명 수준을 조정한다.

---

# 매 세션 루틴

## 세션 시작

Claude Code를 열고 이렇게 말하면 된다:

> "오늘 뭐하지?" 또는 "현황 파악해줘"

Claude가 메모리 파일과 PROJECT_STATUS를 읽고 현재 상태를 요약해준다.

## 세션 중

- 논문을 읽고 정리할 결과가 생기면 → `/organize-deepresearch`
- 분석이나 코드 작업은 평소대로

## 세션 끝

> "/session-wrap" 또는 "마무리하자"

Claude가 자동으로:
1. 오늘 작업을 `50_Experiments/EXP YYMMDD.md`로 기록
2. `00_Meta/PROJECT_STATUS.md` 업데이트
3. Claude 메모리 스냅샷 갱신
4. 오늘 교정 사례 있으면 `HUMAN_CORRECTIONS.md` 업데이트

---

# 핵심 원칙 하나

**세션 마무리를 건너뛰지 말 것.** 기록이 끊기면 다음 세션의 AI는 다시 처음부터 파악해야 한다. 5분짜리 `/session-wrap`이 다음 세션의 30분을 아껴준다.

---

> **Claude에게:** 위 세팅을 모두 완료했으면 이 파일 상단 frontmatter의 `onboarded: false`를 `onboarded: true`로 업데이트할 것.

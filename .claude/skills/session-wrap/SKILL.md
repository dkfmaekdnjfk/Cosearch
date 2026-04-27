---
name: session-wrap
description: |
  세션 마무리 스킬. 오늘 한 작업을 Obsidian EXP 노트로 기록하고,
  project_experiment_status.md를 현재 상태로 업데이트한다.
  "세션 마무리", "끝내자", "오늘 정리", "wrap up", "마무리하자",
  "메모리 업데이트", "정리하고 끝내자" 등의 말이 나오면 반드시 이 스킬을 사용할 것.
  사용자가 명시적으로 요청하지 않아도, 긴 작업 세션 후 "끝", "수고", "다음에" 같은
  마무리 신호가 보이면 이 스킬을 먼저 제안할 것.
---

# 세션 마무리 스킬

세션 종료 전에 두 가지를 반드시 완료한다:
1. **EXP 노트** — 오늘 한 작업의 상세 기록 (Obsidian 50_Experiments/)
2. **Status 업데이트** — 현재 상태 스냅샷 갱신 (memory/project_experiment_status.md)

---

## Step 1: 오늘 EXP 노트 확인

`obsidian/50_Experiments/`에서 오늘 날짜 파일 확인:
- 파일명 형식: `EXP YYMMDD 세션주제.md` (예: `EXP 260416 데이터 전처리.md`)
- 이미 있으면 → 내용 보완
- 없으면 → 새로 생성

### EXP 노트 frontmatter
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

### EXP 노트 본문 구조
```markdown
# EXP YYMMDD — 세션 주제

## 작업 목표
[이 세션에서 하려 했던 것]

## 완료한 작업
[실제로 완료한 것들, 구체적으로]

## 주요 결론/발견
[중요한 깨달음, 수치, 결정사항]

## 수정/변경사항
[파일 이동, 코드 수정, 재분류 등]

## 미완료 / 다음 세션으로
[못 끝낸 것, 다음에 해야 할 것]
```

---

## Step 2: PROJECT_STATUS.md 업데이트 (Obsidian)

파일 경로: `obsidian/00_Meta/PROJECT_STATUS.md`

이 파일은 **사람이 읽는 상세 현황**이다. Obsidian wikilink, 테이블, 실험 계보 등 포함 가능.
길이 제한 없음. 단, 오래된 세션 요약은 3개 이내로 유지하고 오래된 것은 삭제.

파일이 없으면 새로 생성한다.

업데이트할 섹션:
- **현재 단계** 한 줄 (상단)
- **최근 세션 요약** 블록에 오늘 세션 추가 (맨 위에 삽입, 오래된 것 삭제)
- **실험 계보 테이블** — 새 실험이 있으면 행 추가
- **다음 우선순위** — 현재 상태 반영

---

## Step 3: project_experiment_status.md 업데이트 (Claude 메모리)

**메모리 파일 경로 계산 방법:**
`~/.claude/projects/[인코딩된-프로젝트-경로]/memory/project_experiment_status.md`

인코딩 규칙: 경로의 각 문자를 ASCII 영숫자·`.`·`-`·`_`는 그대로, 나머지(`:`, `\`, `/`, 공백, 비ASCII)는 모두 `-`로 변환.

예) `C:\Users\foo\Desktop\my project` → `C--Users-foo-Desktop-my-project`

이 파일은 **Claude 컨텍스트용 스냅샷**이다. Claude가 세션 시작 시 로드.

### 핵심 원칙
- **현재 상태만** — 이력, 검증 기록, 테이블 없음
- **최대 50줄** — 넘으면 줄여야 함
- **다음 세션의 Claude가 2분 안에 파악** 가능해야 함

### 고정 구조 (이 순서, 이 항목만)
```markdown
# 프로젝트 현황 (업데이트: YYMMDD)

[한 줄 요약]

## 미해결 블로커 (우선순위순)
1. [가장 시급한 것] (최대 5개)

## 다음 세션 첫 번째 할 일
> [딱 하나, 구체적으로]

## 핵심 파일 위치
| 역할 | 경로 |

## 마지막 세션 요약 (1~3줄)
[날짜] — [한 것] — [결론]
```

### 업데이트 방법
1. 현재 파일 Read
2. 각 섹션을 현재 상태로 **교체** (추가 아님)
3. 50줄 초과 시 → 테이블 압축 또는 요약 1줄로 줄임

---

## Step 4: HUMAN_CORRECTIONS.md 업데이트 (해당 시)

파일 경로: `obsidian/00_Meta/HUMAN_CORRECTIONS.md`

이 세션에서 사용자가 Claude의 판단/해석/방향을 교정한 사례가 있었다면 기록한다.

**기록 기준** (이 조건을 하나라도 충족하면 기록):
- Claude가 잘못된 코드 수정이나 파일 변경을 했고, 사용자가 revert/교정을 요청한 경우
- Claude의 해석이 틀려서 사용자가 방향을 바꿔준 경우
- 사용자의 도메인 지식이 Claude의 판단을 뒤집은 경우

**기록하지 않는 것**: 단순 오타 수정, 수치 업데이트, 사용자 기호 반영

**형식**:
```markdown
### [YYMMDD] 교정 제목

**상황**: Claude가 뭘 했는가
**교정**: 사용자가 어떻게 교정했는가
**패턴**: 재발 방지를 위한 한 줄 규칙
```

패턴 요약 테이블도 함께 업데이트.

---

## Step 5: 코드 변경 시 git commit & push

세션 중 코드 또는 스킬 파일을 수정했다면 반드시 커밋 후 push.

```bash
git add <수정된 파일들>
git commit -m "커밋 메시지"
git push
```

- temp 파일 (`temp_*.py`, `*_tmp.*` 등)은 스테이징 제외
- obsidian 노트 변경도 함께 커밋 가능

---

## Step 6: 완료 확인

사용자에게 다음을 보고:
- ✅ EXP 노트: `50_Experiments/EXP YYMMDD XXX.md` 생성/업데이트
- ✅ Obsidian STATUS: `00_Meta/PROJECT_STATUS.md` 업데이트
- ✅ Claude 메모리: `project_experiment_status.md` XX줄로 업데이트
- ✅ HUMAN_CORRECTIONS: 교정 사례 있으면 `00_Meta/HUMAN_CORRECTIONS.md` 업데이트
- ✅ Git push: 코드/스킬 변경 시 완료 여부
- 다음 세션 첫 번째 할 일: [내용]

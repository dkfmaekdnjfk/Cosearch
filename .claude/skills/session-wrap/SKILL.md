---
name: session-wrap
description: |
  세션 마무리 스킬. 오늘 한 작업을 Obsidian EXP 노트로 기록하고,
  `obsidian/00_Meta/PROJECT_STATUS.md`와 공유 Claude 메모리 스냅샷을 현재 상태로 업데이트한다.
  "세션 마무리", "끝내자", "오늘 정리", "wrap up", "마무리하자",
  "메모리 업데이트", "정리하고 끝내자" 등의 말이 나오면 반드시 이 스킬을 사용할 것.
  사용자가 명시적으로 요청하지 않아도, 긴 작업 세션 후 "끝", "수고", "다음에" 같은
  마무리 신호가 보이면 이 스킬을 먼저 제안할 것.
---

# 세션 마무리 스킬

세션 종료 전에 다음을 반드시 완료한다:
1. **EXP 노트** — 이번 세션의 상세 기록 (`obsidian/50_Experiments/`)
2. **Status 업데이트** — 사람이 읽는 상세 현황과 에이전트가 읽는 현재 상태 스냅샷 갱신
3. **교정·산출물 기록** — 해당하는 경우 교정 이력과 대용량 산출물 목록 갱신

---

## Step 0: 현재 시각 확인

사용자의 시간대를 기준으로 현재 날짜·시각을 확인한다. 앱이 제공한 시간대를 우선하고,
터미널 날짜를 사용할 때에는 그 시간대와 일치하는지 확인한다. 시각을 추측하지 않는다.

```bash
date "+%Y-%m-%d %H:%M (%a)"
```

앞 세션을 가리킬 때 `어제`, `지난주`, `며칠 전` 같은 상대 시점 표현을 쓰지 않는다.
세션 식별자(`260831b`)나 절대 날짜와 시각을 사용한다. 상대 시점 표현이 꼭 필요하면
현재 시각과 대상 노트의 `date-experiment`를 확인하여 실제 차이를 계산한다.

---

## Step 1: 이번 세션의 EXP 노트 생성

`obsidian/50_Experiments/`에서 오늘 날짜로 시작하는 파일을 확인한다.
- 파일명 형식: `EXP YYMMDD 세션주제.md` (예: `EXP 260416 데이터 전처리.md`)
- 같은 날짜의 노트가 없으면 접미어 없이 새로 생성한다.
- 같은 날짜의 노트가 있으면 날짜 뒤에 알파벳 접미어를 붙여 새 노트를 만든다.
  둘째 세션은 `EXP 260831b …`, 셋째 세션은 `EXP 260831c …`처럼 기록한다.
- 접미어는 해당 세션의 식별자다. Status 세션 요약, 교정 번호, 커밋 메시지에도 같은
  식별자를 사용한다.

앞 세션의 작업을 이어서 끝냈고 문제의식도 같을 때만 기존 노트를 보완한다. 이 경우
`## 미완료 / 다음 세션으로`를 해소하고 본문을 갱신한다.

### EXP 노트 frontmatter
```yaml
---
title: "EXP YYMMDD 세션주제"
tags:
  - experiment
  - [관련 태그]
status: complete
date-experiment: YYYY-MM-DD
session-start: "HH:MM"
session-end: "HH:MM"
date-created: YYYY-MM-DD
date-modified: YYYY-MM-DD
---
```

`session-start`를 모르면 첫 커밋이나 첫 파일의 수정 시각으로 근사하고, 근사했음을 밝힌다.

### EXP 노트 본문 구조
```markdown
# EXP YYMMDD[접미어] — 세션 주제

> `YYYY-MM-DD HH:MM–HH:MM` · 앞 세션: `[식별자 또는 「없음」]`

## 문제의식 / 배경
[왜 이 세션을 시작했는지. 확실하지 않으면 사용자에게 먼저 묻고 추측하지 않는다.]

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

### 코드를 실행한 세션이라면 아래 섹션도 추가

````markdown
## Code
- `code/scripts/run_example.py`

## Input
- `data/processed/...` *(local only)*

## Command
```bash
PYTHONPATH=code python code/scripts/run_example.py
```

## Output
- Tracked: `results/final/summary.png`
- Local only: `results/runs/YYMM/YYMMDD_topic/`

## Result
[주요 수치, 그래프 해석, 결론]
````

---

## Step 2: PROJECT_STATUS.md 업데이트 (Obsidian)

파일 경로: `obsidian/00_Meta/PROJECT_STATUS.md`

이 파일은 **사람이 읽는 상세 현황**이다. Obsidian wikilink, 테이블, 실험 계보 등 포함 가능.
길이 제한 없음. 단, 오래된 세션 요약은 3개 이내로 유지하고 오래된 것은 삭제.

업데이트할 섹션:
- **현재 단계** 한 줄 (상단)
- **최근 세션 요약** 블록에 이번 세션을 맨 위에 추가한다.
  제목은 `### YYYY-MM-DD[접미어] (HH:MM–HH:MM)` 형식으로 쓰고 3개만 유지한다.
- **실험 계보 테이블** — 새 실험이 있으면 행 추가
- **다음 우선순위** — 현재 상태 반영
- **논문 Claim** — 이 논문이 한 문장으로 주장하는 것. 연구 방향이 바뀌면 반드시 업데이트.
- **현재 병목** — 지금 막힌 지점 또는 해결해야 할 핵심 질문. 매 세션 업데이트.

---

## Step 3: project_experiment_status.md 업데이트 (공유 메모리)

프로젝트 지침이 지정한 공유 메모리 파일을 사용한다. 별도 Codex 정본을 만들지 않는다.
기본 위치: `~/.claude/projects/[인코딩된-프로젝트-경로]/memory/project_experiment_status.md`.
기존 MEMORY.md와 실제 폴더를 확인해 경로를 결정한다.

이 파일은 Claude와 Codex가 함께 읽는 **현재 상태 스냅샷**이다.

### 핵심 원칙
- **현재 상태만** — 이력, 검증 기록, 테이블 없음
- **최대 50줄이면서 2,000자 이하** — 두 조건을 모두 만족해야 한다.
- **다음 세션의 에이전트가 2분 안에 파악**할 수 있어야 한다.

### 고정 구조 (이 순서, 이 항목만)
```markdown
# 프로젝트 현황 (업데이트: YYMMDD[접미어] HH:MM)

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
1. 현재 파일을 읽는다.
2. 각 섹션을 현재 상태로 **교체**한다. 이전 상태를 뒤에 누적하지 않는다.
3. 저장 후 Python으로 줄 수와 유니코드 문자 수를 모두 측정한다.

   ```bash
   python3 -c "from pathlib import Path; s=Path('실제 메모리 파일 경로').expanduser().read_text(encoding='utf-8'); print(f'{len(s.splitlines())}줄 / {len(s)}자')"
   ```

   `wc -m`과 `awk length`는 로케일에 따라 한글 바이트 수를 셀 수 있으므로 사용하지 않는다.
4. 50줄 또는 2,000자를 넘으면 오래된 블로커와 완료 항목을 먼저 삭제하고, 서술 문단과
   테이블을 압축한다. 개행만 없애 줄 수를 맞추는 방식은 사용하지 않는다.
5. 완료 보고에 줄 수와 문자 수를 함께 적는다.

---

## Step 4: HUMAN_CORRECTIONS.md 업데이트 (해당 시)

파일 경로: `obsidian/00_Meta/HUMAN_CORRECTIONS.md`

이 세션에서 사용자가 에이전트의 판단·해석·방향을 교정한 사례가 있었다면 기록한다.

**기록 기준** (이 조건을 하나라도 충족하면 기록):
- 에이전트가 잘못된 코드 수정이나 파일 변경을 했고, 사용자가 복원이나 교정을 요청한 경우
- 에이전트의 해석이 틀려서 사용자가 방향을 바꿔준 경우
- 사용자의 분야 지식이 에이전트의 판단을 뒤집은 경우

**기록하지 않는 것**: 단순 오타 수정, 수치 업데이트, 사용자 기호 반영

**형식**:
```markdown
### [YYMMDD] 교정 제목

**상황**: 에이전트가 무엇을 했는가
**교정**: 사용자가 어떻게 교정했는가
**패턴**: 재발 방지를 위한 한 줄 규칙
```

해당 사례가 없으면 건너뛴다.

---

## Step 5: 대용량 파일 생성 시 manifest 업데이트

이 세션에서 `data/processed/`, `results/runs/` 등 Git 밖 대용량 파일·폴더가 새로 생겼다면:

1. `artifacts/manifest.yaml`에 항목 추가
   - `local_path`, `note`, `created_by` 기록
2. EXP 노트 Output 섹션에 경로 명시 (이미 위에서 작성)

파일이 없으면 건너뜀.

---

## Step 6: Claude 훅과 같은 검증 수행

Codex에서는 Claude의 Stop 훅이 자동으로 실행되지 않으므로 존재하는 검사 프로그램을 직접 실행한다. 아래 예시는 파일이 있을 때만 실행한다.

```bash
python3 .claude/hooks/check_memory_update.py </dev/null
```

- 프로젝트에 추가 검증 훅이 있다면 해당 지침에 따라 함께 실행한다.
- 메모리·Status·EXP 노트 경고가 나오면 누락 여부를 확인하고 필요한 갱신을 마친다.
- 외부 검토 원문처럼 수정해서는 안 되는 사료는 검사 결과만을 이유로 고치지 않는다.

---

## Step 7: 변경사항 git commit, 요청 시 push

세션 중 코드·스킬·문서 등 Git 관리 대상 파일을 수정했다면 세션 래핑 과정에서 커밋한다.
`git push`는 사용자가 명시적으로 요청한 경우에만 진행한다.

```bash
git add <이번 세션에서 실제로 수정한 경로들>
git diff --cached --name-status
git commit -m "커밋 메시지"
# 사용자가 push를 명시적으로 요청한 경우에만:
git push
```

- `git add .`를 사용하지 않는다. 이번 세션에서 실제로 수정한 경로만 명시한다.
- 커밋 전 `git status`와 diff를 확인하고, 이번 세션에서 의도적으로 만든 변경만 스테이징한다.
- 다른 작업이나 사용자의 기존 변경이 섞여 있으면 임의로 포함하지 않는다. 안전하게 분리할 수 없는 경우에는 커밋하지 않고 그 이유를 보고한다.
- temp 파일 (`temp_*.py`, `*_tmp.*` 등)은 스테이징 제외
- obsidian 노트 변경도 함께 커밋 가능

---

## Step 8: 완료 확인

사용자에게 다음을 보고:
- ✅ EXP 노트: `50_Experiments/EXP YYMMDD[접미어] XXX.md` 생성/업데이트
- ✅ Obsidian STATUS: `00_Meta/PROJECT_STATUS.md` 업데이트
- ✅ 공유 메모리: `project_experiment_status.md` XX줄 / X,XXX자로 업데이트
- ✅ HUMAN_CORRECTIONS: 교정 사례가 있으면 `00_Meta/HUMAN_CORRECTIONS.md` 업데이트
- ✅ Manifest: 대용량 파일 생겼으면 `artifacts/manifest.yaml` 업데이트
- ✅ Git commit: 변경사항 커밋 완료 여부와 commit hash
- ✅ Git push: 사용자가 요청했을 때만 완료 여부
- 다음 세션 첫 번째 할 일: [내용]

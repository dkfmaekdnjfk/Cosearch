---
name: sync-from-cosearch
description: |
  Cosearch 템플릿 레포에서 스킬 업데이트를 가져오는 스킬.
  "코서치 업데이트 확인해줘", "스킬 동기화해줘", "sync-from-cosearch" 등의 말이 나오면 이 스킬을 사용할 것.
  마지막 동기화 날짜를 last_sync.txt에 기록하며, CLAUDE.md 지시에 따라 2주 이상 지나면
  세션 시작 시 알림이 표시된다.
---

# Cosearch 동기화 스킬

Cosearch 템플릿 레포(https://github.com/dkfmaekdnjfk/Cosearch)의 `.claude/skills/`와
현재 프로젝트를 비교해 새 스킬·변경사항을 선택적으로 가져온다.

---

## Step 1: 마지막 동기화 날짜 확인

파일: `.claude/skills/sync-from-cosearch/last_sync.txt`

- 있으면 → 날짜를 읽어 사용자에게 표시: "마지막 동기화: YYYY-MM-DD"
- 없으면 → "동기화 이력 없음"으로 진행

---

## Step 2: Cosearch 레포 fetch

```bash
# 기존 temp 폴더 정리 후 shallow clone (skills 폴더만)
rm -rf /tmp/cosearch_sync
git clone --depth 1 --filter=blob:none --sparse \
  https://github.com/dkfmaekdnjfk/Cosearch.git /tmp/cosearch_sync
cd /tmp/cosearch_sync && git sparse-checkout set .claude/skills ADVISOR.md
```

---

## Step 3: diff 비교 및 보고

현재 프로젝트의 `.claude/skills/`와 비교:

| 구분 | 처리 |
|------|------|
| **새 스킬** (Cosearch에만 있음) | 파일명 목록으로 보고 |
| **변경된 스킬** (양쪽에 있지만 내용 다름) | 파일명 + diff 핵심만 요약 |
| **현재 프로젝트에만 있는 스킬** | 건드리지 않음 (프로젝트 고유) |

루트의 `ADVISOR.md`도 비교 대상에 포함한다.

사용자에게 보고 후 확인:
```
새 스킬: [목록]
변경된 스킬: [목록]

어떤 것을 가져올까요? (전체 / 선택 / 건너뜀)
```

---

## Step 4: 선택적 적용

사용자가 선택한 항목만 복사:

```bash
# 스킬 파일
cp /tmp/cosearch_sync/.claude/skills/[스킬명]/SKILL.md \
   .claude/skills/[스킬명]/SKILL.md

# ADVISOR.md (선택 시)
cp /tmp/cosearch_sync/ADVISOR.md ./ADVISOR.md
```

프로젝트 고유 설정(경로, 태그 등)이 있는 스킬은 덮어쓰기 전 사용자에게 확인한다.

---

## Step 5: 정리 및 날짜 기록

```bash
rm -rf /tmp/cosearch_sync
echo "YYYY-MM-DD" > .claude/skills/sync-from-cosearch/last_sync.txt
```

완료 보고:
```
✅ 동기화 완료 (YYYY-MM-DD)
가져온 것: [목록]
건너뛴 것: [목록]
다음 알림: 14일 후
```

---
name: write-review-prompt
description: 외부 AI에 전달할 코드·방법론·논문 리뷰 프롬프트를 파일로 작성한다. 리뷰 프롬프트나 외부 검토 요청문 작성 시 사용하며, 리뷰 자체는 실행하지 않는다.
---

# 리뷰 프롬프트 작성 스킬

외부 AI(Gemini 등 Antigravity 접근 가능한 도구)에게 코드/방법론 리뷰를
요청하는 프롬프트를 작성하고 저장한다.

---

## 절대 금지

- 서브에이전트로 리뷰 직접 실행 ❌
- 채팅창에 프롬프트 전문 출력 ❌

---

## Step 1: 프롬프트 구성

사용자가 제공한 내용을 바탕으로 프롬프트를 작성한다.
모든 리뷰 프롬프트에 반드시 포함할 것:

1. **배경**: 외부 AI가 컨텍스트 없이도 이해할 수 있도록 충분히
2. **읽어야 할 파일 목록**: 레포 루트 기준 경로, 읽는 순서 명시
3. **리뷰 항목**: 구체적인 질문 형태로
4. **출력 형식**: 종합 판정 / 문제 / 권고 구조 권장
5. **`write-critical-review` 스킬 사용 지시**:
   반드시 프롬프트 마지막에 명시 —
   > "리뷰 수행 시 `write-critical-review` 스킬을 사용하여 작성하고,
   > 결과를 `obsidian/70_Reviews/REV YYMMDD [주제].md`에 저장해주세요."

---

## Step 2: 저장

- 저장 위치: `obsidian/60_Plans/PLAN YYMMDD review prompt [주제].md`
- frontmatter 형식:
  ```yaml
  ---
  title: "Review Prompt — [주제]"
  tags:
    - review
    - prompt
  status: ready
  date-created: YYYY-MM-DD
  result-file: ""
  ---
  ```

---

## Step 3: 결과 수신 시

결과 파일(`70_Reviews/REV YYMMDD [주제].md`)이 생성되면:
- 프롬프트 파일 `status: done`으로 변경
- `result-file` 필드에 결과 파일명 기입

---

## Step 4: 보고

채팅 출력: 파일 경로만

```
✅ 저장: obsidian/60_Plans/PLAN YYMMDD review prompt XXX.md
```

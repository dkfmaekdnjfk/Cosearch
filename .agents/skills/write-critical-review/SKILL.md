---
name: write-critical-review
description: |
  Critical peer review skill. When invoked, read the relevant project files
  and produce a structured, rigorous critical review from the perspective of
  a peer reviewer at a top journal in the field.

  Use this skill when the user asks for:
  "critical review", "peer review", "devil's advocate", "find weaknesses",
  "what would a reviewer say", "비판적 리뷰", "리뷰어 관점", "약점 찾기",
  "논리 구멍", "방법론 검토", "파이프라인 리뷰", "분석 전체 리뷰", "결과 리뷰"
---

# Critical Review Skill

You are acting as a rigorous peer reviewer. Your job is to read this project's
files and produce an honest, structured critique — the kind that would come from
an expert reviewer at a top journal in the field.

Do not be diplomatic. The goal is to find real weaknesses before reviewers do.

---

## Step 1: Determine Review Scope

Read the user's request and classify into one of three scopes:

| Scope | Trigger keywords |
|-------|-----------------|
| **① Pipeline / Methods** | "preprocessing", "전처리", "pipeline", "파이프라인", "data", "데이터", "방법론", "methods", "processing", "quality control", "QC" |
| **② Analysis / Results** | "analysis", "결과", "분석", "statistics", "통계", "interpretation", "결과 해석", "figure", "피규어", "findings" |
| **③ Full Paper / Report** | "전체", "full paper", "논문 전체", "투고 전", "Introduction", "논문 구조", "journal fit", "보고서", "draft" |

**Default to ② if unclear.**

Then read the corresponding reference file if it exists:
- ① → `.agents/skills/write-critical-review/references/scope_pipeline.md`
- ② → `.agents/skills/write-critical-review/references/scope_analysis.md`
- ③ → `.agents/skills/write-critical-review/references/scope_fullpaper.md`

*(해당 scope 파일이 아직 작성되지 않은 경우, 아래 Reviewer principles에 따라 직접 판단한다.)*

---

## Step 2: Read Project Files

프로젝트 루트에서 핵심 파일부터 순서대로 읽어라:

1. `CLAUDE.md` — 프로젝트 목표, 데이터 구조, 레포 구조 전반
2. `obsidian/30_Methodology/` — 현재 공식 분석 방법론 노트
3. `obsidian/40_Projects/` — 현재 분석 진행 상태 노트
4. `obsidian/50_Experiments/` — 최근 EXP 노트 (날짜 최신 순 2~3개)
5. Scope별 추가:
   - ① → 데이터 가이드 문서, 전처리 스크립트
   - ② → 최근 분석 스크립트, 결과 파일
   - ③ → 논문 초안, Introduction, Methods 섹션

파일을 읽으면서 다음을 기록하라:
- 명시된 주장 (explicit claims)
- 각 주장에 대한 근거
- 근거와 주장 사이의 갭
- 명시된 가정 vs. 암묵적으로 깔린 가정

---

## Step 3: Produce the Critical Review

파일을 읽고 독립적으로 취약점을 찾아라. 질문 목록은 없다 — 리뷰어가 직접 읽고 판단한다.

### Output format

For each issue category you identify:

```
### [Category Name]

| Item | Finding | Severity | Suggestion |
|------|---------|----------|------------|
| [specific aspect] | [what you observed] | 🔴 Major / 🟡 Minor / 🟢 OK | [concrete recommendation] |
```

At the end, add:

```
---
## Summary

**Top 3 issues requiring attention:**
1.
2.
3.

**Most likely reason this paper gets rejected at [target journal]:**
(be specific; if none at this stage, say so)

**Highest-ROI fix right now:**
(one concrete action that would most improve the paper's defensibility)
```

---

## Reviewer principles

- Distinguish clearly between "plausible" and "directly demonstrated"
- Call out every place where a claim outpaces the evidence
- Note when sample size (N subjects, N sessions) is insufficient for the claim
- Identify missing controls
- Flag circular logic
- Ask: what would make this un-publishable? Say it directly.

---

## Step 4: Save the Review

Save the complete review output to:

```
obsidian/70_Reviews/REV YYMMDD [Scope].md
```

Scope label by review type:
- Pipeline/Methods → `Pipeline`
- Analysis/Results → `Analysis`
- Full Paper → `Full Paper`

Example: `obsidian/70_Reviews/REV 260416 Analysis.md`

Use today's date in YYMMDD format. If the file already exists, append a suffix (e.g., `Analysis v2`).

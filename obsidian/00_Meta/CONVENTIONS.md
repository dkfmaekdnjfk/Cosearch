---
title: "CONVENTIONS"
tags:
  - meta
  - conventions
date-modified: YYYY-MM-DD
---

# Obsidian Vault 규칙

## 파일명 접두사

| 접두사 | 폴더 | 용도 | 예시 |
|--------|------|------|------|
| `EXP` | `50_Experiments/` | 분석/실험 세션 노트 | `EXP 260417 세션주제.md` |
| `MTG` | `50_Experiments/` | 미팅/발표 노트 | `MTG 260417 lab meeting.md` |
| `DR` | `70_Reviews/` | 딥리서치 결과 원본 | `DR 260416 주제.md` |
| `REV` | `70_Reviews/` | 코드/분석 리뷰 | `REV 260416 Analysis.md` |

`99_Assets/`는 이미지·PDF 등 바이너리 파일 전용 — `.md` 파일 금지.

---

## EXP 노트 frontmatter

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

---

## 폴더 용도

| 폴더 | 용도 |
|------|------|
| `00_Meta/` | 프로젝트 현황 (PROJECT_STATUS.md), 규칙 (CONVENTIONS.md) |
| `10_Literature/` | 논문 노트 (citekey 기반, `저자연도_키워드.md`) |
| `20_Concepts/` | 이론·개념 노트 |
| `30_Methodology/` | 분석 방법론 문서 (best practice, 파이프라인 기준) |
| `40_Projects/` | 진행 중 분석 파이프라인 노트 |
| `50_Experiments/` | EXP·MTG 노트 (날짜 기반) |
| `60_Plans/` | 계획, 로드맵, 다음 단계 |
| `70_Reviews/` | DR·REV 파일 |
| `99_Assets/` | 이미지, PDF (바이너리 전용) |

---

## Literature 노트 frontmatter

```yaml
---
title: "논문 제목"
tags: [literature, 주제태그]
citekey: 저자연도_키워드
authors: "저자1, 저자2"
year: YYYY
journal: "저널명"
doi: "10.xxxx/xxxxx"
pmid: "XXXXXXXX"
status: unread
importance: 3   # 1~5
date-created: YYYY-MM-DD
date-modified: YYYY-MM-DD
---
```

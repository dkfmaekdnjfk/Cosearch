---
title: "Literature Dashboard"
tags:
  - meta
  - dashboard
date-modified: YYYY-MM-DD
---

# 논문 현황 대시보드

## ❌ 파일 없음 — 수동 다운로드 필요

```dataview
TABLE paper_file, journal, year
FROM "10_Literature"
WHERE paper_status = "missing"
SORT year ASC
```

## ⚠️ 요약본만 있음 (전문 필요 시 수동 다운로드)

```dataview
TABLE paper_file, journal, year
FROM "10_Literature"
WHERE paper_status = "stub"
SORT year ASC
```

## ✅ 전문 보유

```dataview
TABLE paper_file, journal, year
FROM "10_Literature"
WHERE paper_status = "full"
SORT year ASC
```

## 🚫 할루시네이션 (논문 없음)

```dataview
TABLE paper_file, journal, year
FROM "10_Literature"
WHERE paper_status = "hallucinated"
```

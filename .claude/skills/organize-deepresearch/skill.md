---
name: organize-deepresearch
description: |
  딥리서치 결과 파일(.md)을 Obsidian 노트 체계로 흡수·정리하는 워크플로우.
  사용자가 딥리서치 파일을 @멘션하거나 "정리해줘", "흡수해줘", "옵시디언에 반영해줘",
  "딥리서치 결과 정리", "리뷰 결과 정리" 등을 말할 때 반드시 이 스킬을 사용할 것.
  별도 요약 문서를 만드는 게 아니라, 기존 노트 체계(10_Literature/ 등)에 결과를 흡수하는 것이 핵심.
---

# 딥리서치 결과 정리 스킬

딥리서치 파일은 **소비하고 소화하는 것**이다. 결과물을 별도 정리 문서로 만들지 말고,
기존 Obsidian 노트 체계에 흡수시키는 것이 목표다.

---

## Step 1: 파싱 — 딥리서치에서 무엇이 나왔나?

딥리서치 파일을 읽고 다음 세 가지로 분류한다.

| 종류 | 처리 방향 |
|------|-----------|
| **새로 등장한 논문** | → `obsidian/10_Literature/`에 개별 literature 노트 생성 |
| **방법론/분석 접근법에 영향** | → `obsidian/30_Methodology/` 또는 `obsidian/20_Concepts/` 노트 업데이트 |
| **진행 중인 분석/프로젝트에 영향** | → `obsidian/40_Projects/` 관련 노트 업데이트 |
| **팩트 수정** (저자명·수치·방법 오류 등) | → 해당 노트 직접 수정 |

딥리서치 파일 자체는 건드리지 않는다. `obsidian/70_Reviews/`에 원본 그대로 보관.

---

## Step 2: 새 논문 → 개별 literature 노트 생성

각 논문마다 하나의 `.md` 파일을 생성한다. 파일명 형식: `저자연도 주제키워드.md`

### PubMed 조회 (병렬 처리)
여러 논문이 있을 경우 PubMed MCP tool을 병렬로 호출해 저자·저널·DOI·PMID를 한 번에 확인한다.
- PMID 있으면 `get_article_metadata` 직접 사용
- DOI만 있으면 `search_articles`에 `DOI[doi]`로 검색
- 저자/제목만 있으면 `search_articles`로 검색

### 표준 frontmatter
```yaml
---
title: "논문 제목"
tags:
  - literature
  - [주제 태그들]
  - [방법론 태그: 예) population-coding / pca / time-series 등]
citekey: 저자연도_키워드
authors: "저자1, 저자2, ..."
year: YYYY
journal: "저널명"
doi: "10.xxxx/xxxxx"
pmid: "XXXXXXXX"
pmcid: "PMCXXXXXXXX"   # 있을 경우만
url: "https://..."
status: unread
importance: 3          # 1~5
aliases:
  - 저자연도
date-created: YYYY-MM-DD
date-modified: YYYY-MM-DD
---
```

### 노트 본문 구조
```markdown
# 저자 연도 — 한국어 제목 요약

---

## 한 줄 요약
[논문의 핵심을 한 문장으로]

---

## 핵심 내용
[논문이 실제로 보여주는 것: 실험 조건, 결과 수치, 방법론]

---

## 우리 연구와의 관계

- **적용 맥락**: [우리 분석의 어떤 부분을 지지/반박/보완하는가]
- **근거 수준**: (A) 직접 확인 / (B) 문헌상 추론 / (C) 가설
- **한계**: [이 논문만으로 주장할 수 없는 것]

---

## 관련 노트
- [[관련 방법론 노트]] — 설명
- [[관련 논문]] — 관련 내용
```

### 미확인 사항 처리
저자·저널·수치 등이 확인되지 않으면 `[!warning]` callout으로 명시하고 진행한다.
확인 후에는 callout을 제거한다.

---

## Step 2.5: 새 논문 → 메타데이터 기록 + 원문 다운로드 (`99_Assets/papers/`)

### ⚠️ 핵심 원칙: 메타데이터 즉시 기록

**PubMed 조회로 PMID/PMCID를 찾는 순간, 노트 frontmatter에 즉시 기록한다.**
나중에 다시 조회하지 않아도 되도록. 아래 필드를 항상 채운다:

```yaml
pmid: "XXXXXXXX"
pmcid: "PMCXXXXXXXX"    # PMC에 있는 경우
paper_file: "저자연도_키워드.html"
paper_status: full      # 다운로드 완료 시
```

### ⚠️ 핵심 원칙: Claude가 직접 HTML을 쓰면 안 된다

API나 WebFetch로 받은 내용을 Write tool로 파일에 직접 쓰는 것은 **금지**:
- 토큰 낭비 (내용 전체가 Claude context를 통과)
- **할루시네이션 위험** — Claude가 재가공하면 내용이 왜곡될 수 있다

**항상 curl로 원본 URL에서 직접 다운로드**:

```bash
curl -s -L \
  -A "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36" \
  -H "Accept: text/html,application/xhtml+xml" \
  "https://www.ncbi.nlm.nih.gov/pmc/articles/PMCXXXXXXXX/" \
  -o "obsidian/99_Assets/papers/저자연도_키워드.html"
```

**파일명 규칙**: `저자연도_키워드.html` 또는 `저자연도_키워드.pdf`

### 다운로드 우선순위

1. **PMC ID 있음** → curl로 PMC HTML 직접 다운로드
   - URL: `https://www.ncbi.nlm.nih.gov/pmc/articles/PMCXXXXXXXX/`
   - CAPTCHA 차단 시(~21KB): 5초 대기 후 재시도 또는 다른 Accept 헤더 추가
   - 성공 기준: 파일 크기 > 50KB

2. **PMC 없음, 오픈 액세스 DOI** → curl로 출판사 URL 직접 다운로드
   - eLife: `https://elifesciences.org/articles/XXXXX`
   - Frontiers: `https://www.frontiersin.org/articles/DOI/full`
   - PLOS: `https://journals.plos.org/...article?id=DOI`
   - bioRxiv: `https://www.biorxiv.org/content/DOI.full`

3. **유료 저널** → 자동 다운로드 불가. 노트에 `[!warning]` 표시 후 사용자에게 수동 요청:
   ```yaml
   paper_file: "NOT_AVAILABLE — 기관 접속 필요"
   paper_status: missing
   ```

### 다운로드 후 검증

```bash
wc -c 저자연도_키워드.html   # 50KB 이상이어야 정상
head -3 저자연도_키워드.html  # <!DOCTYPE html> 형식이어야 원본
```

---

## Step 3: 기존 노트 업데이트

딥리서치 내용이 기존 노트에 영향을 준다면 해당 노트를 직접 업데이트한다.

**업데이트 대상 우선순위:**
1. `obsidian/30_Methodology/` — 분석 방법론 문서 (best practice, 기준 추가)
2. `obsidian/20_Concepts/` — 개념 노트 (이론적 내용)
3. `obsidian/40_Projects/` — 현재 진행 중 분석에 직접 영향을 주는 내용

업데이트 시:
- 편집 전 반드시 Read tool로 현재 내용 확인
- 기존 내용을 지우지 말고, 새 근거/수정사항을 `[!note]` 또는 날짜 표기와 함께 추가
- 재분류 필요 시 `[!warning]` callout으로 사유 명시

---

## Step 4: 프롬프트 파일 완료 처리

딥리서치를 의뢰한 프롬프트 파일이 `obsidian/60_Plans/`에 있다면,
처리 완료 후 frontmatter의 `status`를 `done`으로 변경한다.

```yaml
# 변경 전
status: ready

# 변경 후
status: done
```

---

## Step 5: 추가 검증 계획

미확인 사항을 두 수준으로 나눈다.

**레퍼런스 존재 확인** (논문이 실재하는가?)
→ PubMed MCP로 즉시 해결. 이 자리에서 처리한다.

**클레임 타당성 확인** (논문 데이터가 우리 분석 주장을 직접 지지하는가?)
→ 전문 확인 필요. 다음 중 하나로 처리:
- 서브에이전트에게 전문 URL 조회 요청
- 다음 딥리서치 프롬프트에 포함시킬 항목으로 분류

정리가 끝나면 아직 해결되지 않은 항목을 사용자에게 요약해준다.

---

## 중요 원칙

1. **노트 편집 전 반드시 Read** — Edit 전에 Read tool로 현재 내용 확인
2. **병렬 처리** — PubMed 조회, 파일 읽기 등 독립적 작업은 한 번에 묶어서 실행
3. **별도 정리 문서 금지** — 딥리서치 원본을 재정리한 새 파일을 만들지 않는다
4. **레퍼런스 존재 ≠ 클레임 타당성** — "논문이 있다"와 "논문 데이터가 우리 주장을 지지한다"는 다른 수준의 검증이다
5. **등급은 보수적으로** — 직접 확인된 것만 (A), 나머지는 (B)/(C)로 시작
6. **메타데이터 즉시 기록** — PMID/PMCID 확인 즉시 노트 frontmatter에 기록
7. **Claude 직접 쓰기 금지** — 논문 내용은 curl로 원본 다운로드. API/WebFetch 응답을 Write tool로 저장하면 토큰 낭비 + 할루시네이션 위험

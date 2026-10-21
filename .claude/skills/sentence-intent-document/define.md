# HTML 구조와 동작

- `assets/sentence-review.html`: 외부 의존성이 없는 문서 템플릿. CSS·본문·설명·JavaScript를 한 파일에 보존한다.
- `.page-header`: 제목과 날짜·문서 정보가 같은 행에 있는 헤더.
- `.document-pane`: 왼쪽 본문. `.sentence-block`마다 안정적인 고유 ID와 `tabindex="-1"`을 지정한다.
- `.phrase`: 클릭할 표현. `href`와 `aria-controls`가 동일한 `.intent-note` ID를 참조한다.
- `.intent-pane`: 선택한 표현의 설명을 표시하는 오른쪽 패널. 좁은 화면에서는 본문 아래에 배치한다.
- `.intent-note`: 표현별 설명. 선택하지 않은 설명은 `hidden`으로 숨기고, 인쇄에서는 모두 표시한다.
- `.sentence-ref`: 설명에서 본문으로 돌아가는 링크. `href`와 `aria-controls`가 동일한 `.sentence-block` ID를 참조한다.
- `selectPhrase(phrase, fromClick)`: 해당 설명 하나만 표시하고 선택한 본문 표현을 강조한다. 좁은 화면의 클릭은 설명 위치로 이동한다.
- `phrases`, `notes`, `pane`: DOM에서 조회한 선택 표현·설명·설명 패널. 문장 추가 후 초기화할 때 자동으로 조회한다.
- `referencedSentence`, `referenceTimer`: 역참조로 강조한 문장과 강조 해제 타이머. 설명 선택은 변경하지 않는다.
- `.is-referenced`: 역참조 문장을 1.8초간 강조한다. 강조는 레이아웃 크기를 바꾸지 않는다.
- `820px`: 화면 너비가 작을 때 두 패널을 세로로 배치하는 기준.
- `1440px`: 문서의 최대 너비. 본문과 설명의 비율은 `.95 : 1.05`다.

문장을 추가할 때 ID를 재사용하거나 기존 문장의 순서를 기준으로 ID를 다시 매기지 않는다.
새 설명과 선택 표현을 함께 추가한다. 본문 전체를 JavaScript 문자열로 다시 작성하지 않는다.

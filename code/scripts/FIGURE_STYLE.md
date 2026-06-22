# Figure 디자인 시스템 (Nature 스타일)

이 프로젝트의 모든 그림은 하나의 스타일을 공유한다. **단일 출처는 [`_figstyle.py`](_figstyle.py)** 이고, 스크립트는 복붙하지 말고 import 한다. 이 문서는 그 규칙과 이유를 적는다.

> 사람이 읽는 사본/맥락: `obsidian/04_Methods/Figure 디자인 시스템 — Nature 스타일 규칙.md`

---

## 왜 단일 모듈인가

`NATURE_RC` dict·색·`panel_label`·`finalize` 가 스크립트마다 복붙되고 있었다. 복붙은 (1) 값이 미묘하게 갈라지고 (2) 한 곳 고치면 나머지가 안 따라온다. 그래서 한 모듈로 모은다. (CLAUDE.md 코드 재활용 규칙: 재사용되는 건 로직이지 주제가 아니다 — 보일러플레이트는 공유 모듈로.)

## import 방법

스크립트는 `code/scripts/<topic>/run_*.py`, 모듈은 `code/scripts/_figstyle.py` (한 단계 위). 직접 실행 시 스크립트 폴더만 path에 잡히므로 부모를 추가한다:

```python
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent.parent))  # -> code/scripts
from _figstyle import apply_style, C_BLUE, C_VERM, C_GREEN, panel_label, finalize

apply_style()
```

## 구성 요소

| 이름 | 역할 |
|---|---|
| `NATURE_RC` | rcParams dict — sans-serif 8pt, top/right spine 제거, grid 없음, frameless legend, savefig 300dpi, `fonttype=42`(Illustrator 편집 가능 텍스트) |
| `apply_style()` | `plt.rcParams.update(NATURE_RC)` — import 후 한 번 호출 |
| Okabe-Ito 색 | `C_BLUE #0072B2`, `C_VERM #D55E00`, `C_GREEN #009E73`, `C_ORANGE #E69F00`, `C_SKY #56B4E9`, `C_PURPLE #CC79A7`, `C_BLACK`, `C_GREY #888888`(참조선·강조 약화). `OKABE_ITO` 는 다계열용 순서 리스트 |
| `panel_label(ax, "a")` | 축 좌상단 바깥에 굵은 소문자 패널 라벨 |
| `finalize(fig, caption, params="")` | 하단에 푸터 영역 확보 후 회색 캡션 + 파라미터/출처 줄 기록 |

## 규칙

1. **색은 Okabe-Ito만.** 색맹 안전 + 흑백 출력에도 구분됨. 임의 hex 쓰지 말 것. 참조선·비강조는 `C_GREY`.
2. **모든 그림에 `finalize` 푸터.** `caption` = 한 문장 설명, `params` = 값·N·seed 등 재현 정보. 그림만 봐도 무슨 파라미터였는지 추적 가능해야 한다.
3. **패널엔 `panel_label`.** 다패널이면 a, b, c…
4. **벡터 친화.** `fonttype=42` 유지 (PDF/EPS 텍스트가 윤곽선이 아니라 편집 가능 폰트로 들어감).
5. **장식 금지.** grid·top/right spine·legend 프레임 다 끔. 정보 위계만 남긴다.

## 현황 / 전환

- ✅ `_figstyle.py` 단일 출처 생성.
- 🔄 기존 스크립트(`260621_*`, `260622_*` 등)는 아직 자체 복사본 사용 — **앞으로 새/수정 스크립트부터 import 로 전환**. 한꺼번에 안 바꿔도 됨(값은 동일).

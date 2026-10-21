# 기존 Nature 디자인 시스템과의 연계

## 역할과 우선순위

`scientific-figure`는 비교·패널 설계·제작·검수를 수행하는 스킬이다. Nature 디자인 시스템은 글자·색·선·패널 문자·푸터 등을 제공하는 제작 모듈이다. 별도 스킬을 검색하거나 설치해야 하는 의존성으로 취급하지 않는다.

Cosearch의 기본 위치:

- `code/scripts/FIGURE_STYLE.md`: 시스템의 규칙과 사용법.
- `code/scripts/_figstyle.py`: `NATURE_RC`, 팔레트, `apply_style()`, `panel_label()`, `finalize()`의 실제 구현.

두 파일을 읽고 현재 구현을 기준으로 작업한다. 다른 위치의 디자인 시스템은 프로젝트 지침과 실제 import 경로를 따른다. 스킬 폴더에 `_figstyle.py`의 복제본을 두거나 같은 rcParams를 새 상수로 만들지 않는다.

적용 순서는 사용자 지시와 해당 작업의 요구사항 → 프로젝트 디자인 시스템 → 시스템이 없는 경우의 범용 시작값이다. 목표 저널의 공식 제출 규정과 충돌하면 변경 항목을 명시하고 해당 작업에 한정해 조정한다. ‘Nature 스타일’이라는 이름이 Nature의 현재 제출 규격 준수를 보증하지는 않는다.

## 제작 전 확인

1. 실제 figure 생성 함수가 `_figstyle.py`를 import하고 `apply_style()`을 호출하는지 확인한다. Import만 있고 호출이 없으면 적용 근거가 아니다.
2. 이후 `rcParams.update`, `style.use`, 축·문자·기호의 명시적 설정으로 무엇이 변경되는지 확인한다. 호출 여부만으로 시스템 전체 준수를 단정하지 않는다.
3. 패널 라벨과 푸터는 `panel_label`, `finalize`를 재사용한다. 프로젝트 규칙과 다르게 배치하거나 생략하는 경우 사용자 요청·출력 목적에 따른 변경 이유를 기록한다.
4. 동일 그림의 HTML/SVG 별도 renderer가 있으면 Python 기본 스타일이 자동 적용되지 않는다는 점을 확인한다. 대응하는 글자·색·선 설정을 대조한다.

## Cosearch의 Python 사용 예

저장소 루트에서 `PYTHONPATH=code`를 지정하면 기존 모듈 경로를 사용할 수 있다. 기존 실행 방식이 있으면 그 방식을 유지한다.

```python
import matplotlib as mpl
import matplotlib.pyplot as plt
from scripts._figstyle import apply_style, C_BLUE, panel_label, finalize

with mpl.rc_context():
    apply_style()
    fig, ax = plt.subplots(figsize=(width_mm / 25.4, height_mm / 25.4))
    # 확인한 자료와 기존 plotting 함수 사용. C_BLUE 등의 팔레트를 직접 import한다.
    panel_label(ax, "a")
    finalize(fig, caption, params=provenance_text)
    # 고정된 최종 폭이 필요한 작업의 명시적 출력 변경:
    mpl.rcParams["savefig.bbox"] = None
    fig.savefig(output_pdf, bbox_inches=None)
    plt.close(fig)
```

`width_mm`, `height_mm`, `caption`, `provenance_text`, `output_pdf`는 해당 작업에서 정의한 입력이다. 코드 조각을 독립 실행용 완성 스크립트로 취급하지 않는다.

현재 시스템은 `savefig.bbox="tight"`를 사용한다. 고정 폭을 지정한 작업에서는 rc_context 안에서 `savefig.bbox=None`도 설정해야 tight 설정을 해제할 수 있다. 최종 PDF 치수로 확인한다. 푸터가 포함된 전체 높이와 패널 영역을 함께 설계한다.

## 검수

사용한 모듈 경로와 변경한 설정만 작업 기록에 남긴다. 색각친화 팔레트 이름만으로 흑백·투명도·겹침 검수를 생략하지 않는다. 모듈을 사용해도 글자·범례가 읽히지 않으면 배치를 수정한다.

시스템을 변경해야 하는 경우 호출하는 다른 figure에 미치는 영향을 확인하고, 범위를 벗어나는 전역 변경 대신 해당 작업의 명시적 설정을 우선한다. 기존 figure를 일괄 재생성하지 않는다.

# 제작과 최종 출력

## 크기와 제작 설정

먼저 기존 디자인 시스템과 논문·보고서·발표의 최종 크기를 확인한다. Cosearch의 Nature 디자인 시스템이 있으면 [연계 절차](nature-design-system.md)에 따라 `_figstyle.py`를 직접 재사용한다. 아래 숫자와 예시는 **디자인 시스템이 없는 경우의 제안 시작값**이며, 기존 설정을 대체하거나 공식 제출 규정으로 사용하지 않는다. 발표용 figure에 그대로 적용하지 않는다. 목표 저널이 지정되면 공식 원문에서 현재 제출 단계의 규정을 확인하고 설정을 조정한다.

| 요소 | 시작값 |
|---|---|
| 축 라벨·일반 글자 | 8 pt |
| 눈금·범례 | 7.5 pt |
| 패널 문자 | 9 pt bold |
| 축·눈금선 | 0.7 pt |
| 개별 관측 연결선 | 0.6 pt |
| 요약선 | 1.2 pt |
| 기준선 | 0.7 pt, 필요할 때 dashed |
| 적은 수의 개별 관측점 지름 | 약 3.6 pt |
| 패널 간격 | 약 4 mm에서 조정 |

서로 다른 저널의 수치를 하나의 규정으로 통합하지 않는다. 큰 패널 문자와 작은 본문 글자를 구분하며 PDF의 모든 텍스트에 동일한 상한을 강제하지 않는다. 실제 글꼴 대체와 수식·비라틴 문자의 지원을 확인한다.

Figure 전체에서 같은 역할의 글씨와 선 크기를 통일한다. 사용자가 지정하거나 프로젝트가 관리하는 참고 도판의 최종 크기와 글씨·선 위계를 먼저 확인하고, 유사한 목적·크기의 그림은 이를 시작점으로 삼아 최종 크기에서 직접 대조한다. 실제 그림의 데이터선·개별선·기준선의 역할과 위계를 확인하며 목표 저널이 있으면 제출 규정도 확인한다. 패널 폭이 다르더라도 같은 역할의 글씨 크기를 각각 축소하지 않는다.

## 색·선·기호와 범례

- 기존 의미가 지정된 색을 우선한다. 상태·집단·연속값 중 색이 담당할 변수를 정하고 다른 변수는 배치·라벨로 구분할 수 있는지 살핀다.
- 방향과 크기를 명도로 동시에 표시하면 부호별 색과 강도의 척도를 범례에 명시한다. opacity 변화는 배경과 겹침에도 영향을 주므로 색상 명도와 동일하다고 취급하지 않는다.
- 흑백과 protan/deutan 색각 모사에서 핵심 비교가 읽히는지 확인한다. 색각 모사의 모델과 범위를 기록하며, 위치·기호·선종류·라벨 등 비교에 적합한 수단으로 조건을 구분한다.
- 중요한 개별 점을 지나치게 흐리게 하지 않는다. 흰 배경과 alpha 합성 후의 대비를 확인한다.
- 선이 적고 분리되어 있으면 직접 라벨, 의미가 같은 패널에는 가까운 공유 범례, 의미가 다른 패널에는 개별 범례를 고려한다. 범례의 글자는 읽기 쉬운 중립색으로, 실제 기호는 데이터와 같은 색·모양으로 표시한다.
- 통계 주석의 공간을 배치 단계에서 확보한다. 어떤 비교·검정의 p인지 표시한다. 별표가 효과의 방향·크기를 대신하지 않는다.

## Matplotlib 사용 예시

기존 plotting 함수를 유지하며 해당 figure에만 설정을 적용한다. 아래 코드는 기존 디자인 시스템이 없는 경우에만 사용하는 예시이며 데이터나 통계를 생성하지 않는다. `_figstyle.py`가 있다면 이 dict를 복사하지 않고 연계 문서의 예시를 사용한다.

```python
from pathlib import Path
import matplotlib as mpl
import matplotlib.pyplot as plt

style = {
    "font.family": "DejaVu Sans",  # 실제 문자 지원·프로젝트 글꼴에 맞춰 선택
    "font.size": 8, "axes.labelsize": 8,
    "xtick.labelsize": 7.5, "ytick.labelsize": 7.5,
    "legend.fontsize": 7.5, "axes.linewidth": 0.7,
    "xtick.major.width": 0.7, "ytick.major.width": 0.7,
    "axes.spines.top": False, "axes.spines.right": False,
    "pdf.fonttype": 42, "ps.fonttype": 42, "svg.fonttype": "none",
    "savefig.facecolor": "white", "savefig.bbox": None,
}
width_mm, height_mm = 180, 100  # 해당 작업에서 선택한 크기; 저널 규정 아님
out = Path("figure-output")
out.mkdir(exist_ok=True)
with mpl.rc_context(style):
    fig, ax = plt.subplots(figsize=(width_mm / 25.4, height_mm / 25.4))
    fig.subplots_adjust(left=0.15, right=0.97, bottom=0.20, top=0.92)
    # 기존 plotting 함수와 확인한 자료로 ax에 그린다.
    # 점 크기: plot(markersize)는 pt, scatter(s)는 pt²이다.
    fig.canvas.draw()
    fig.savefig(out / "figure.pdf", bbox_inches=None)
    fig.savefig(out / "figure.svg", bbox_inches=None)
    fig.savefig(out / "figure.png", dpi=300, bbox_inches=None)
    plt.close(fig)
```

SVG의 텍스트 보존은 수신 환경의 글꼴에 의존한다. PDF font embedding을 별도로 확인한다. 고정 폭이 필요할 때 `bbox_inches="tight"`는 페이지 크기를 바꾸므로 최종 치수를 다시 측정한다.

PNG·heatmap·현미경 이미지는 실제 배치 크기에 따른 effective DPI를 계산한다. PNG를 PDF에 넣은 것만으로 vector figure라고 부르지 않는다. 혼합 도판은 선·문자와 raster 부분을 각각 검수한다.

대응점·분포 등 구체적인 plotting 함수는 지표·자료 구조에 맞춰 기존 구현을 사용한다. 이 예시를 새로운 통계 분석 코드로 확대하지 않는다.

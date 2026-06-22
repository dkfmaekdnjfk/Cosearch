"""Shared Nature-style figure system for this project.

Single source of truth for the figure look that was previously copy-pasted into
every plotting script (NATURE_RC, the Okabe-Ito palette, panel_label, finalize).

Usage (scripts live in code/scripts/<topic>/run_*.py; this module sits one level up):

    import sys
    from pathlib import Path
    sys.path.insert(0, str(Path(__file__).resolve().parent.parent))  # -> code/scripts
    from _figstyle import apply_style, C_BLUE, C_VERM, panel_label, finalize

    apply_style()
    ...
    finalize(fig, "Caption sentence.", params="pKaA=3.5, N=200000, seed=...")
    fig.savefig(OUTDIR / "name.png")

Design rules and rationale are documented in:
    code/scripts/FIGURE_STYLE.md
    obsidian/04_Methods/Figure 디자인 시스템 — Nature 스타일 규칙.md
"""

import matplotlib.pyplot as plt

# ----- Nature-style rcParams ----------------------------------------------
NATURE_RC = {
    "font.family": "sans-serif",
    "font.sans-serif": ["Arial", "Helvetica", "DejaVu Sans"],
    "font.size": 8,
    "axes.labelsize": 8,
    "axes.titlesize": 8,
    "axes.titleweight": "regular",
    "xtick.labelsize": 7,
    "ytick.labelsize": 7,
    "legend.fontsize": 6.5,
    "axes.linewidth": 0.8,
    "xtick.major.width": 0.8,
    "ytick.major.width": 0.8,
    "xtick.direction": "out",
    "ytick.direction": "out",
    "xtick.major.size": 3,
    "ytick.major.size": 3,
    "axes.spines.top": False,
    "axes.spines.right": False,
    "axes.grid": False,
    "legend.frameon": False,
    "figure.dpi": 150,
    "savefig.dpi": 300,
    "savefig.bbox": "tight",
    "axes.unicode_minus": True,
    "pdf.fonttype": 42,   # embed TrueType (editable text in Illustrator)
    "ps.fonttype": 42,
}

# ----- Okabe-Ito colourblind-safe palette ---------------------------------
# https://jfly.uni-koeln.de/color/  — 8 colours discriminable for all common CVD types.
C_BLACK = "#000000"
C_ORANGE = "#E69F00"
C_SKY = "#56B4E9"
C_GREEN = "#009E73"
C_YELLOW = "#F0E442"
C_BLUE = "#0072B2"
C_VERM = "#D55E00"   # vermillion
C_PURPLE = "#CC79A7"
C_GREY = "#888888"   # neutral grey for reference lines / de-emphasis

# ordered cycle for multi-series plots (skip yellow on white backgrounds)
OKABE_ITO = [C_BLUE, C_VERM, C_GREEN, C_ORANGE, C_SKY, C_PURPLE, C_BLACK]


def apply_style():
    """Apply NATURE_RC to the global matplotlib rcParams. Call once at import time."""
    plt.rcParams.update(NATURE_RC)


def panel_label(ax, letter, dx=-0.16, dy=1.02):
    """Bold lower-case panel label (a, b, ...) just outside the top-left of an axes."""
    ax.text(dx, dy, letter, transform=ax.transAxes, fontsize=10,
            fontweight="bold", va="bottom", ha="right")


def finalize(fig, caption, params="", max_frac=0.30, height_in=0.80):
    """Reserve a footer strip and write a small grey caption (+ optional params line).

    caption    one-sentence description of what the figure shows.
    params     parameter / provenance string (values, N, seed). Printed on its own line.
    max_frac   cap on the fraction of figure height given to the footer.
    height_in  target footer height in inches; the footer fraction is
               min(max_frac, height_in / figure_height).
    """
    h = fig.get_size_inches()[1]
    frac = min(max_frac, height_in / h)
    fig.tight_layout(rect=[0, frac, 1, 1])
    text = caption if not params else caption + "\n" + params
    fig.text(0.012, 0.012, text, ha="left", va="bottom",
             fontsize=5.5, color="0.4", wrap=True)

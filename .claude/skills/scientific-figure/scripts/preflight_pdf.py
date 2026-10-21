"""Read-only PDF screening; optional PNG rendering. Requires PyMuPDF.

No journal defaults, package installation, or network access.
Exit codes: 0 no detected violations, 1 violations, 2 execution error.
"""

import argparse
import json
import math
from pathlib import Path
import sys


def positive(value):
    number = float(value)
    if not math.isfinite(number) or number <= 0:
        raise argparse.ArgumentTypeError("Expected a finite positive number")
    return number


def arguments():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("pdf", type=Path)
    for flag in ("width-mm", "height-mm", "min-font", "max-font",
                 "min-stroke", "max-stroke"):
        parser.add_argument("--" + flag, type=positive)
    parser.add_argument("--tolerance-mm", type=positive, default=0.1)
    parser.add_argument("--require-text", action="store_true")
    parser.add_argument("--require-embedded-fonts", action="store_true")
    parser.add_argument("--render-dir", type=Path)
    parser.add_argument("--dpi", type=positive, default=150)
    args = parser.parse_args()
    for kind in ("font", "stroke"):
        low, high = getattr(args, "min_" + kind), getattr(args, "max_" + kind)
        if low is not None and high is not None and low > high:
            parser.error("Minimum must not exceed maximum: " + kind)
    return args


def interval(values):
    return [min(values), max(values)] if values else None


def inspect_page(doc, page, args, fitz):
    issues = []
    size = [page.rect.width * 25.4 / 72, page.rect.height * 25.4 / 72]
    for dimension, measured, target in zip(
        ("width", "height"), size, (args.width_mm, args.height_mm)
    ):
        if target is not None and abs(measured - target) > args.tolerance_mm:
            issues.append({"kind": dimension, "actual_mm": measured, "target_mm": target})

    # Infinite clip permits detection of text that extends beyond the page.
    text = page.get_text("dict", clip=fitz.INFINITE_RECT())
    spans = [s for b in text["blocks"] for line in b.get("lines", [])
             for s in line.get("spans", []) if s["text"].strip()]
    if args.require_text and not spans:
        issues.append({"kind": "no_extractable_text"})
    bounds = fitz.Rect(page.rect)
    bounds += (-0.5, -0.5, 0.5, 0.5)
    for span in spans:
        # Text coordinates are unrotated; page.rect includes page rotation.
        box = fitz.Rect(span["bbox"]) * page.rotation_matrix
        if not bounds.contains(box):
            issues.append({"kind": "text_outside_page", "text": span["text"]})
        for limit, violated in (
            ("min_font", args.min_font is not None and span["size"] < args.min_font - 0.02),
            ("max_font", args.max_font is not None and span["size"] > args.max_font + 0.02),
        ):
            if violated:
                issues.append({"kind": limit, "text": span["text"], "size_pt": span["size"]})

    strokes = [d.get("width", 0) for d in page.get_drawings()
               if d.get("type") in ("s", "fs") and d.get("width") is not None]
    # A zero-width PDF hairline is meaningful and must not be silently ignored.
    for flag, predicate in (
        ("min_stroke", lambda x, limit: x < limit - 0.01),
        ("max_stroke", lambda x, limit: x > limit + 0.01),
    ):
        limit = getattr(args, flag)
        bad = [w for w in strokes if limit is not None and predicate(w, limit)]
        if bad:
            issues.append({"kind": flag, "count": len(bad), "range_pt": interval(bad)})

    fonts = []
    for font in page.get_fonts(full=True):
        xref = font[0]
        try:
            embedded = bool(doc.extract_font(xref)[-1]) if xref > 0 else None
        except (RuntimeError, ValueError):
            embedded = None
        fonts.append({"name": font[3], "type": font[2], "embedded": embedded})
        if args.require_embedded_fonts and embedded is not True:
            issues.append({"kind": "font_not_embedded_or_unknown", "font": font[3]})

    images = []
    for info in page.get_image_info():
        a, b, c, d, _, _ = info["transform"]
        width_pt, height_pt = math.hypot(a, b), math.hypot(c, d)
        images.append({
            "pixels": [info["width"], info["height"]],
            "placed_mm": [width_pt * 25.4 / 72, height_pt * 25.4 / 72],
            "estimated_dpi": [info["width"] * 72 / width_pt if width_pt else None,
                              info["height"] * 72 / height_pt if height_pt else None],
        })
    return {"page": page.number + 1, "size_mm": size, "text_spans": len(spans),
            "text_range_pt": interval([s["size"] for s in spans]),
            "stroke_range_pt": interval(strokes), "fonts": fonts,
            "raster_images": images, "issues": issues}


def main():
    args = arguments()
    try:
        import pymupdf as fitz
        with fitz.open(args.pdf) as doc:
            if not doc.is_pdf or doc.needs_pass or len(doc) == 0:
                raise ValueError("Expected an accessible, nonempty PDF")
            if args.render_dir is not None and args.render_dir.exists():
                raise FileExistsError("Render directory already exists; refusing overwrite")
            pages = [inspect_page(doc, page, args, fitz) for page in doc]
            if args.render_dir is not None:
                args.render_dir.mkdir(parents=True, exist_ok=False)
                for page, record in zip(doc, pages):
                    output = args.render_dir / f"page-{page.number + 1}.png"
                    page.get_pixmap(matrix=fitz.Matrix(args.dpi / 72, args.dpi / 72)).save(output)
                    record["render"] = str(output.resolve())
        count = sum(len(p["issues"]) for p in pages)
        print(json.dumps({"file": str(args.pdf.resolve()), "issue_count": count,
                          "pages": pages, "manual_review_required": [
                              "source values, pairing, sample hierarchy and statistics",
                              "legend/data overlap, clipping, meaning of colors and symbols",
                              "actual-size readability and scientific interpretation",
                              "outlined text, transformed strokes and image quality",
                          ]}, ensure_ascii=False, indent=2))
        return 1 if count else 0
    except (ImportError, OSError, RuntimeError, ValueError) as error:
        print(json.dumps({"error": str(error)}, ensure_ascii=False), file=sys.stderr)
        return 2


if __name__ == "__main__":
    sys.exit(main())

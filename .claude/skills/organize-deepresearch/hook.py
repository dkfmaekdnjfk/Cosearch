#!/usr/bin/env python3
"""
PostToolUse hook for Write tool.
Checks that new literature notes (paper_status: full) contain at least one direct quote.
If no quote is found, warns Claude to re-read the paper HTML and rewrite.
"""
import json
import os
import re
import sys


def main():
    try:
        data = json.load(sys.stdin)
    except Exception:
        sys.exit(0)

    file_path = data.get("tool_input", {}).get("file_path", "")
    if not file_path:
        sys.exit(0)

    normalized = file_path.replace("\\", "/")

    # Only check Literature notes
    if "/10_Literature/" not in normalized or not normalized.endswith(".md"):
        sys.exit(0)

    try:
        with open(file_path, encoding="utf-8") as f:
            content = f.read()
    except Exception:
        sys.exit(0)

    # Only check notes that have the full paper downloaded
    if "paper_status: full" not in content:
        sys.exit(0)

    # Extract body after frontmatter (after second ---)
    parts = re.split(r"^---\s*$", content, flags=re.MULTILINE)
    # parts[0] = "" before first ---, parts[1] = frontmatter, parts[2:] = body
    if len(parts) < 3:
        sys.exit(0)
    body = "\n".join(parts[2:])

    # Check for direct quote: "text" with at least 10 chars between double quotes
    if re.search(r'"[^"\n]{10,}"', body):
        sys.exit(0)

    # No direct quote found
    fname = os.path.basename(file_path)
    print(
        f"⚠️ [원문 검증 실패] {fname}: paper_status: full이지만 "
        f'직접 인용구("...")가 없습니다. '
        f"obsidian/99_Assets/papers/ 의 HTML 파일을 Grep/Read로 읽고 "
        f"Methods 핵심 구절을 직접 인용한 뒤 노트를 재작성하세요."
    )
    sys.exit(2)


if __name__ == "__main__":
    main()

"""Read shared gate notes; emit Claude hook context without permission overrides."""
import json
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parents[2]


def read_gate(name):
    """Return gate body without frontmatter, introduction or maintenance notes."""
    try:
        body = (PROJECT_ROOT / "obsidian" / "00_Meta" / name).read_text(encoding="utf-8")
    except (OSError, UnicodeError):
        return ""
    lines = body.splitlines()
    if lines and lines[0] == "---":
        try:
            lines = lines[lines.index("---", 1) + 1:]
        except ValueError:
            return ""
    body = "\n".join(lines)
    if "## 게이트" not in body:
        return ""
    return body.split("## 게이트", 1)[1].split("## 유지 관리", 1)[0].strip()


def emit_context(event, name):
    """Emit additionalContext only; missing/empty notes quietly pass through."""
    body = read_gate(name)
    if body:
        print(json.dumps({"hookSpecificOutput": {
            "hookEventName": event,
            "additionalContext": f"[{name}]\n{body}",
        }}, ensure_ascii=False))

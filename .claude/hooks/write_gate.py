"""Inject writing questions for edits within this project's Obsidian vault."""
import json
import sys
from pathlib import Path
from gate_context import PROJECT_ROOT, emit_context


def main():
    try:
        payload = json.load(sys.stdin)
        if not isinstance(payload, dict):
            return
        tool_input = payload.get("tool_input")
        if not isinstance(tool_input, dict):
            return
        file_path = tool_input.get("file_path")
        if not isinstance(file_path, str) or not file_path:
            return
        target = Path(file_path)
        if not target.is_absolute():
            target = PROJECT_ROOT / target
        relative = target.resolve().relative_to((PROJECT_ROOT / "obsidian").resolve())
    except (ValueError, OSError, RuntimeError):
        return
    if relative in (Path("00_Meta/ANSWER_GATES.md"), Path("00_Meta/WRITE_GATES.md")):
        return
    emit_context("PreToolUse", "WRITE_GATES.md")


if __name__ == "__main__":
    main()

"""
Claude Code Stop Hook — 세션 종료 시 메모리/EXP 노트 업데이트 경고
등록 위치: settings.local.json > hooks > Stop
"""
import sys
import os
import json
import datetime
import glob


def get_project_root():
    """Return project root from CLAUDE_PROJECT_DIR env var, or fallback to CWD."""
    return os.environ.get("CLAUDE_PROJECT_DIR", os.getcwd())


def encode_path(path):
    """Encode a filesystem path the same way Claude Code does for project keys."""
    result = ""
    for ch in path:
        if ch.isascii() and (ch.isalnum() or ch in ".-_"):
            result += ch
        else:
            result += "-"
    return result.strip("-")


def get_memory_file(project_root):
    encoded = encode_path(project_root)
    return os.path.join(
        os.path.expanduser("~"),
        ".claude", "projects", encoded, "memory",
        "project_experiment_status.md"
    )


MAX_LINES  = 50    # Claude 메모리 파일 적정 최대 줄 수
WARN_HOURS = 6     # 몇 시간 이상 미업데이트면 경고
WARN_DAYS  = 3     # Obsidian PROJECT_STATUS 며칠 이상 미업데이트면 경고


def check():
    warnings = []
    today = datetime.date.today()

    project_root   = get_project_root()
    memory_file    = get_memory_file(project_root)
    obsidian_base  = os.path.join(project_root, "obsidian")
    obsidian_exp   = os.path.join(obsidian_base, "50_Experiments")
    obsidian_status = os.path.join(obsidian_base, "00_Meta", "PROJECT_STATUS.md")

    # 1. status 파일 존재 + 크기 확인
    if not os.path.exists(memory_file):
        warnings.append("🚨  project_experiment_status.md 파일이 없습니다!")
    else:
        size = os.path.getsize(memory_file)
        if size == 0:
            warnings.append("🚨  project_experiment_status.md 가 비어있습니다!")
        else:
            mtime = datetime.datetime.fromtimestamp(os.path.getmtime(memory_file))
            age_h = (datetime.datetime.now() - mtime).total_seconds() / 3600
            if age_h > WARN_HOURS:
                warnings.append(
                    f"⚠️   Status 마지막 업데이트: {mtime.strftime('%m/%d %H:%M')} ({age_h:.0f}시간 전)"
                )
            with open(memory_file, encoding="utf-8", errors="replace") as f:
                lines = f.readlines()
            if len(lines) > MAX_LINES:
                warnings.append(
                    f"📏  Status 파일이 {len(lines)}줄 — {MAX_LINES}줄 이하로 줄여야 합니다"
                )

    # 2. Obsidian PROJECT_STATUS.md 확인
    if os.path.exists(obsidian_status):
        ps_mtime = datetime.datetime.fromtimestamp(os.path.getmtime(obsidian_status))
        ps_age_days = (datetime.datetime.now() - ps_mtime).total_seconds() / 86400
        if ps_age_days > WARN_DAYS:
            warnings.append(
                f"📋  Obsidian PROJECT_STATUS: {ps_mtime.strftime('%m/%d')} ({ps_age_days:.0f}일 전) — 업데이트 필요"
            )
    else:
        warnings.append("📋  obsidian/00_Meta/PROJECT_STATUS.md 없음")

    # 3. 오늘 EXP 노트 확인
    today_str = today.strftime("%y%m%d")  # YYMMDD
    if os.path.isdir(obsidian_exp):
        pattern = os.path.join(obsidian_exp, f"EXP {today_str}*.md")
        today_exps = glob.glob(pattern)
        if not today_exps:
            warnings.append(f"📝  오늘({today_str}) EXP 노트가 없습니다 — 세션 기록을 남겨두세요")

    # 출력
    if warnings:
        print("\n" + "=" * 55, file=sys.stderr)
        print("  세션 마무리 체크리스트", file=sys.stderr)
        print("=" * 55, file=sys.stderr)
        for w in warnings:
            print(f"  {w}", file=sys.stderr)
        print("-" * 55, file=sys.stderr)
        print("  /session-wrap 을 실행하면 자동으로 처리됩니다", file=sys.stderr)
        print("=" * 55 + "\n", file=sys.stderr)


if __name__ == "__main__":
    try:
        input_data = json.load(sys.stdin)
    except Exception:
        input_data = {}

    check()
    print(json.dumps({}))

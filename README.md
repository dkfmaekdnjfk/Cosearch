```
 ██████╗ ██████╗ ███████╗███████╗ █████╗ ██████╗  ██████╗██╗  ██╗
██╔════╝██╔═══██╗██╔════╝██╔════╝██╔══██╗██╔══██╗██╔════╝██║  ██║
██║     ██║   ██║███████╗█████╗  ███████║██████╔╝██║     ███████║
██║     ██║   ██║╚════██║██╔══╝  ██╔══██║██╔══██╗██║     ██╔══██║
╚██████╗╚██████╔╝███████║███████╗██║  ██║██║  ██║╚██████╗██║  ██║
 ╚═════╝ ╚═════╝ ╚══════╝╚══════╝╚═╝  ╚═╝╚═╝  ╚═╝ ╚═════╝╚═╝  ╚═╝
```

**Co-research with AI.** A ready-to-clone scaffold for research projects built around a simple idea: AI loses all context when a session ends. Cosearch solves this by turning Obsidian into a structured external memory store that both you and the AI read and write together.

Clone this repo, launch Claude Code, and the AI walks you through the rest.

> **`ADVISOR.md`** (project root) defines how the AI behaves as a research advisor — it prioritizes research direction over execution details, and will tell you to scrap the whole approach if needed.

---

## The problem this solves

AI is a powerful research partner — but it forgets everything between sessions. Without a shared memory, every session starts from scratch: re-explaining the project, re-establishing context, re-recovering where you left off.

Cosearch treats the Obsidian vault not just as a note-taking tool, but as the AI's long-term memory. Every session end writes a structured log. Every session start reads it back. Over time, the AI accumulates the context needed to work as a genuine collaborator.

---

## What's included

### Obsidian vault (`obsidian/`)

Structured knowledge base readable by both human and AI:

| Folder | Purpose |
|--------|---------|
| `00_Meta/` | Project status, conventions, correction log, understanding checklist |
| `10_Literature/` | Paper notes (citekey-based) |
| `20_Concepts/` | Theory and concept notes |
| `30_Methodology/` | Analysis pipeline and best practices |
| `40_Projects/` | Ongoing analysis notes |
| `50_Experiments/` | Session logs (`EXP`) and meeting notes (`MTG`) |
| `60_Plans/` | Roadmaps and next steps |
| `70_Reviews/` | Deep research results (`DR`) and code reviews (`REV`) |
| `99_Assets/` | Binary files only (images, PDFs, HTMLs) |

Comes with **Dataview** pre-installed and graph view color-coded by folder.

### Claude Code setup (`.claude/`)

**Skills:**
- `session-wrap` — End-of-session ritual: writes an EXP note, updates project status in Obsidian, and syncs the Claude memory snapshot
- `organize-deepresearch` — Absorbs a deep research `.md` file into the existing note structure rather than creating a separate summary doc
- `advisor` — Spawns an isolated agent to diagnose research direction against `ADVISOR.md` principles (layer 1→2→3) and saves the review to `08_Reviews/`
- `write-deepresearch-prompt` — Writes a self-contained prompt doc to hand off to an external AI (Claude.ai deep research etc.); never executes the search itself
- `obsidian-skills-main` — Obsidian markdown, canvas, bases, and CLI helpers

**Stop hook** (`check_memory_update.py`):
Fires automatically when Claude Code exits. Warns if today's EXP note is missing, the status file is stale, or the memory snapshot exceeds 50 lines.

**`settings.local.json`:**
Pre-approved permissions for WebSearch, PubMed, and common academic publisher domains.

### Memory system (`memory/`)

Starter `MEMORY.md` index for Claude's persistent project memory (stored at `~/.claude/projects/[encoded-path]/memory/`).

---

## Getting started

```bash
# 1. Clone
git clone https://github.com/dkfmaekdnjfk/Cosearch.git my-project
cd my-project

# 2. Fresh git history
rm -rf .git && git init

# 3. Open obsidian/ as a new vault in Obsidian

# 4. Launch Claude Code — it handles the rest
claude
```

On first launch, Claude reads `obsidian/00_Meta/START_HERE.md` and walks you through the remaining setup.

---

## Daily workflow

| When | What |
|------|------|
| Session start | "오늘 뭐하지?" — Claude reads status and picks up where you left off |
| Got deep research results | `/organize-deepresearch` — absorbs into vault |
| Need a research direction check | `/advisor` — isolated agent diagnoses direction against ADVISOR.md |
| Need to delegate a literature search | `/write-deepresearch-prompt` — writes the handoff doc, never searches itself |
| Session end | `/session-wrap` — logs the session, updates memory |

---

## Key conventions

- **EXP notes**: `EXP YYMMDD topic.md` in `50_Experiments/`
- **Literature notes**: `Author YYYY keyword.md` in `10_Literature/`
- **Deep research files**: drop in `70_Reviews/` as `DR YYMMDD topic.md`, then `/organize-deepresearch`

See `obsidian/00_Meta/CONVENTIONS.md` for the full format reference.

---

## License

MIT — see [LICENSE](LICENSE).
`obsidian-skills-main` by [@kepano](https://github.com/kepano), also MIT.

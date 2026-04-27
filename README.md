# Research Project Template

A ready-to-copy scaffold for research projects using **Obsidian** + **Claude Code**.

Clone this repo, fill in your project name, and you have a working knowledge management + AI assistant setup from day one.

---

## What's included

### Obsidian vault (`obsidian/`)

Pre-configured folder structure for research note-taking:

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

Comes with the **Dataview** community plugin pre-installed and core plugins configured.

### Claude Code setup (`.claude/`)

**Skills:**
- `session-wrap` — End-of-session ritual: writes an EXP note, updates project status in Obsidian, and syncs the Claude memory snapshot
- `organize-deepresearch` — Absorbs a deep research `.md` file into the existing note structure (literature notes, methodology updates, etc.) rather than creating a separate summary doc
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
# 1. Copy the template
cp -r research-project-template my-new-project
cd my-new-project

# 2. Start a fresh git history
rm -rf .git
git init

# 3. Fill in your project name and paths
#    Edit CLAUDE.md — replace [Project Name] and path placeholders

# 4. Open obsidian/ as a new vault in Obsidian

# 5. Launch Claude Code in the project root
claude
```

---

## Key conventions

- **EXP notes**: `EXP YYMMDD 세션주제.md` in `50_Experiments/`
- **Literature notes**: `저자연도_키워드.md` in `10_Literature/`
- **Deep research files**: drop in `70_Reviews/` as `DR YYMMDD 주제.md`, then run `/organize-deepresearch`
- **Session wrap**: run `/session-wrap` (or say "마무리하자") at the end of every session

See `obsidian/00_Meta/CONVENTIONS.md` for the full note format reference.

```
 ██████╗ ██████╗ ███████╗███████╗ █████╗ ██████╗  ██████╗██╗  ██╗
██╔════╝██╔═══██╗██╔════╝██╔════╝██╔══██╗██╔══██╗██╔════╝██║  ██║
██║     ██║   ██║███████╗█████╗  ███████║██████╔╝██║     ███████║
██║     ██║   ██║╚════██║██╔══╝  ██╔══██║██╔══██╗██║     ██╔══██║
╚██████╗╚██████╔╝███████║███████╗██║  ██║██║  ██║╚██████╗██║  ██║
 ╚═════╝ ╚═════╝ ╚══════╝╚══════╝╚═╝  ╚═╝╚═╝  ╚═╝ ╚═════╝╚═╝  ╚═╝
```

**Co-research with AI.** A ready-to-clone scaffold for research projects built around a simple idea: AI loses all context when a session ends. Cosearch solves this by turning Obsidian into a structured external memory store that both you and the AI read and write together.

Clone this repo and open it with Claude Code or Codex. `CLAUDE.md` contains the shared project instructions, and `AGENTS.md` connects Codex to the same instructions and memory.

> **`ADVISOR.md`** (project root) defines how the AI behaves as a research advisor — it prioritizes research direction over execution details, and will tell you to scrap the whole approach if needed.

---

## The problem this solves

AI is a powerful research partner — but it forgets everything between sessions. Without a shared memory, every session starts from scratch: re-explaining the project, re-establishing context, re-recovering where you left off.

Cosearch treats the Obsidian vault not just as a note-taking tool, but as the AI's long-term memory. Every session end writes a structured log. Every session start reads it back. Over time, the AI accumulates the context needed to work as a genuine collaborator.

---

## What's included

### Code / Data / Results (`code/`, `data/`, `results/`)

Research-oriented codebase structure:

| Folder | Role | Git |
|--------|------|-----|
| `code/scripts/` | Run scripts | ✅ |
| `code/pipelines/` | Pipeline configs (*.yaml) | ✅ |
| `code/notebooks/` | Exploratory notebooks | ✅ |
| `code/cosearch/` | Cosearch framework package | ✅ |
| `code/tests/` | Test code | ✅ |
| `code/legacy/` | Pre-cosearch code archive | ❌ local only |
| `config/sessions/` | Session config files | ✅ |
| `config/params/` | Analysis parameters | ✅ |
| `data/examples/` | Small sample data | ✅ |
| `data/raw/` | Raw input data | ❌ local only |
| `data/processed/` | Preprocessed data | ❌ local only |
| `data/legacy/` | Pre-cosearch data archive | ❌ local only |
| `results/final/` | Final figures & tables | ✅ |
| `results/runs/` | Script outputs — `runs/YYMM/YYMMDD_topic/` | ❌ local only |
| `results/legacy/` | Pre-cosearch results archive | ❌ local only |
| `results/logs/` | Run logs | ❌ local only |
| `results/tmp/` | Intermediate outputs | ❌ local only |

`artifacts/manifest.yaml` tracks all large local files outside Git — path, origin, and how to recreate them.

**새 대용량 파일이 생길 때 할 일:**

1. `artifacts/manifest.yaml`에 항목 추가 — `local_path`, `note`, `created_by` 기록
2. 관련 EXP 노트 Output 섹션에 경로 명시
3. `results/final/`에 넣을 최종본만 Git에 추가

Every analysis session links code → data → results through an EXP note in `obsidian/50_Experiments/`.

### Obsidian vault (`obsidian/`)

Structured knowledge base readable by both human and AI:

| Folder | Purpose |
|--------|---------|
| `00_Meta/` | Project status, glossary, answer/writing gates, correction log, understanding checklist |
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

- [`korean-copy`](.claude/skills/korean-copy/SKILL.md): Korean wording rules for research and general documents. Prefers original English technical terms and prohibits colloquial wording, pronouns, em dashes and corner brackets. Checks the shared glossary before editing.
- `session-wrap`: Records each session in an EXP note, updates project status and the shared memory snapshot, and tracks code, inputs and outputs. The snapshot must stay within 50 lines and 2,000 Unicode characters.
- `organize-deepresearch` — Absorbs a deep research `.md` file into the existing note structure rather than creating a separate summary doc
- `advisor`: Uses an isolated agent to assess research purpose, evidence and counterarguments against `ADVISOR.md`. The agent saves its assessment in `70_Reviews/` without reading previous advisor reviews.
- [`write-review-prompt`](.claude/skills/write-review-prompt/SKILL.md): Prepares an external code, methods or paper review request with context and a reading list. Does not run the review.
- `write-deepresearch-prompt` — Writes a self-contained prompt doc to hand off to an external AI (Claude.ai deep research etc.); never executes the search itself
- `teach` — Turns a concept you don't understand into a structured note in `20_Concepts/`; never explains in chat
- `sync-from-cosearch`: Compares skills and advisor principles with this template and applies selected updates. Also supports explicitly requested contributions of common improvements back to the template, excluding project-specific content.
- `obsidian-skills-main` — Obsidian markdown, canvas, bases, and CLI helpers

**Review skill (`.agents/skills/`):**

- [`write-critical-review`](.agents/skills/write-critical-review/SKILL.md): Reads project files and writes a structured review of methods, results or a full paper.

**`session-wrap`** now includes code execution tracking: when you run an analysis, the EXP note records the script, input data, command, and output paths — linking every result back to the code that made it. New large local files get logged to `artifacts/manifest.yaml`.

**Hooks:**

`.claude/settings.json` registers the answer gate, writing gate and literature ingestion checks.
`check_memory_update.py` provides an EXP/status/memory check; automatic Stop execution requires
registration in local Claude settings. Codex applies the shared checklists and available checks directly.

### Claude and Codex collaboration

`AGENTS.md` routes Codex to the same project instructions and shared memory used by Claude.
Session logs distinguish separate sessions on the same date. The current memory snapshot is
limited to 50 lines and 2,000 Unicode characters; claims retain pointers to original evidence.

Research values are checked against original numeric tables; graph digitization is excluded.
Claims retain their conditions and source locations rather than relying on compressed memory summaries.

For template maintenance, keep the cloned repository's Git history and Cosearch remote.
The “Fresh git history” step below applies to a new research project derived from the template.
Use `sync-from-cosearch` to distribute changes or contribute explicitly requested common improvements.

### Answer and writing gates

Shared question checklists live in `obsidian/00_Meta/ANSWER_GATES.md` and
`WRITE_GATES.md`. Claude hooks inject them before answers and vault writes;
Codex reads the same notes directly. Hooks provide context without overriding permissions.
Literature ingestion also checks metadata, attribution and supplementary evidence.

### Glossary and terminology

[`GLOSSARY.md`](obsidian/00_Meta/GLOSSARY.md) contains the terminology workflow:

- Register a new name before use, with its definition, classification criterion, collision check and source location.
- Prefer the original English name for technical terms.
- Replace banned terms; check watchlist terms against their actual definitions.
- Search affected documents before changing or retiring a term, and preserve received source material.

Term, banned-term and watchlist tables start empty. Research-specific terms and correction cases
are not copied into the common template. The `korean-copy` skill reads this glossary before editing.
The glossary markers do not run an automatic terminology checker.

### Memory system (`memory/`)

Starter `MEMORY.md` index for shared persistent project memory (stored at `~/.claude/projects/[encoded-path]/memory/`).

---

## Getting started

```bash
# 1. Clone
git clone https://github.com/dkfmaekdnjfk/Cosearch.git my-project
cd my-project

# 2. Fresh git history
rm -rf .git && git init

# 3. Open obsidian/ as a new vault in Obsidian

# 4. Launch Claude Code, or open the project in Codex
claude
```

On first launch, read `obsidian/00_Meta/START_HERE.md` and follow the onboarding instructions.
For a checkout used to maintain Cosearch itself, retain `.git` and the Cosearch remote;
the fresh-history step applies only to a new research project.

---

## Daily workflow

| When | What |
|------|------|
| Session start | "오늘 뭐하지?" — Claude reads status and picks up where you left off |
| Got deep research results | `/organize-deepresearch` — absorbs into vault |
| Need a research direction check | `/advisor` — isolated agent diagnoses direction against ADVISOR.md |
| Need to delegate a literature search | `/write-deepresearch-prompt` — writes the handoff doc, never searches itself |
| Korean editing | `korean-copy` applies wording rules and checks `GLOSSARY.md` |
| New terminology | Register the definition and source in `GLOSSARY.md` before use |
| External review request | `write-review-prompt` writes the handoff document |
| Template updates | `sync-from-cosearch` compares and applies selected common updates |
| Session end | `/session-wrap` — logs the session, updates memory |

---

## Key conventions

- **EXP notes**: `EXP YYMMDD topic.md` in `50_Experiments/`
- **Literature notes**: `Author YYYY keyword.md` in `10_Literature/`
- **Deep research files**: drop in `70_Reviews/` as `DR YYMMDD topic.md`, then `/organize-deepresearch`

See [`memory/naming_conventions.md`](memory/naming_conventions.md) for naming and output conventions.
See [`GLOSSARY.md`](obsidian/00_Meta/GLOSSARY.md) for terminology rules.

---

## License

MIT — see [LICENSE](LICENSE).
`obsidian-skills-main` by [@kepano](https://github.com/kepano), also MIT.

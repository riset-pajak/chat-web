# MEMORY.md

## Project Identity
Chat Web + API for RisetPajak -- FastAPI service providing REST API + Web Chat UI.

## Architecture Decision
- **Single service**: One FastAPI app serves both `/api/*` (REST) and `/chat` (Web UI)
- **Consumer pattern**: telegram-bot consumes this API, not direct SQLite access
- **Data source**: `../corpus-preparation/data/output/corpus.jsonl` → SQLite with FTS5

## Key Decisions
- SQLite as Phase 2 database (lightweight, no Docker needed)
- FTS5 for full-text search (built-in, no extra deps)
- Jinja2 for web templating (phase 2)
- CLI entry point via uvicorn (`chat-web` command)

## Design Principles
- API-first: web UI and telegram-bot consume the same endpoints
- Citation required: every LLM answer must reference source sections
- Parameterized queries only (no string interpolation in SQL)
- Pydantic validation for all request/response

## Environment
- Python 3.11.15 (pyenv)
- Located: `/home/riset-pajak/Github/riset-pajak/chat-web/`
- Port: 8000 (default uvicorn)

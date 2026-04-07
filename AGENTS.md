# AGENTS.md

## Project Name
Chat Web + API -- RisetPajak

## Mission
One FastAPI service that provides both REST API and Web Chat interface for Indonesian tax regulation research.

## Objectives
- Serve REST API endpoints for regulation search, retrieval, and LLM-powered explain/compare/ask
- Provide Web Chat UI for interactive regulation queries
- Consume data from corpus-preparation pipeline (JSONL/SQLite)

## Architecture
- Single FastAPI instance at `/api/*` (REST) and `/chat` (Web UI)
- Telegram-bot and browser both consume the same API
- Data source: `../corpus-preparation/data/output/corpus.jsonl` (Phase 2a) → SQLite with FTS5 (Phase 2b)

## Agent Behavior
- Always prioritize accuracy over speed
- Cite regulation references (PMK-68/2024, UU-6/1983, etc.)
- If data not found → return proper 404 with message
- If LLM unsure → "data tidak mencukupi untuk menjawab"
- Never hallucinate regulation numbers or content

## API Design Rules
- All data endpoints under `/api/` prefix
- GET for retrieval, POST for LLM operations
- Pydantic models for request/response validation
- SQLite queries use parameterized statements (no string interpolation)

## Safety Rules
- Never fabricate regulation content
- If parsing fails → return 500 with error detail
- LLM responses must cite source sections
- Rate limiting consideration for future

## Project Status
- Phase 1: ✅ Initiated (FastAPI app, /health, / discovery, /chat placeholder)
- Phase 2: 🔄 Next -- SQLite ingestion + API endpoints + LLM integration
- Phase 3: 📋 Planned -- Semantic search, vector store

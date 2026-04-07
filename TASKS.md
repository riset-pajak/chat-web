# TASKS.md

**Last Updated:** 2026-04-08

> chat-web = FastAPI service (REST API + Web Chat dalam satu service).
> Phase numbering mengikuti PROJECT_PLAN.md.

## Phase 1: Foundation ✅ COMPLETE
- [x] Init FastAPI project (pyproject.toml, src/chatweb/)
- [x] CLI entry point (`chat-web` command via uvicorn)
- [x] Health check endpoint (`GET /health`)
- [x] API discovery endpoint (`GET /`)
- [x] Web chat placeholder (`GET /chat` + Jinja2 template)
- [x] AGENTS.md, SOUL.md, README.md

## Phase 2: Intelligence (NEXT PHASE)

### 2a. Data Ingestion
- [ ] Baca corpus.jsonl dari `../corpus-preparation/data/output/`
- [ ] Ingest ke SQLite (tabel: regulations, sections, topics)
- [ ] Build FTS5 virtual tables untuk full-text search
- [ ] CLI command: `chat-web ingest` (sekali jalan atau incremental)

### 2b. API Endpoints (Data)
- [ ] `GET /api/regulations` -- list semua regulasi (paginasi)
- [ ] `GET /api/regulations/{identifier}` -- detail satu regulasi
- [ ] `GET /api/regulations/search?q=` -- FTS5 search
- [ ] `GET /api/articles/{identifier}/{section}` -- ambil pasal spesifik
- [ ] Pydantic response models untuk semua endpoint

### 2c. LLM Integration
- [ ] Tentukan LLM provider & model
- [ ] `POST /api/explain` -- jelaskan pasal dalam bahasa sederhana
    Input: identifier + section / full_text
    Output: penjelasan + citations
- [ ] `POST /api/ask` -- jawab pertanyaan berbasis konteks
    Input: question (query corpus via FTS5, lalu pass ke LLM dengan context)
    Output: jawaban + sumber regulasi
- [ ] `POST /api/compare` -- bandingkan dua regulasi/pasal
    Input: identifier_a + section_a, identifier_b + section_b
    Output: tabel perbandingan + analisis

### 2d. Web Chat UI
- [ ] Ganti placeholder HTML dengan chat interface
- [ ] Form input untuk questions
- [ ] Stream/long-polling untuk LLM responses
- [ ] Tampilkan citations/sumber jawaban
- [ ] Responsive design (mobile-friendly)

### 2e. Telegram Bot Integration
- [ ] Add API client function ke telegram-bot
- [ ] Ganti echo handler -> consume `/api/regulations/search`
- [ ] Add commands: `/cari`, `/pasal`, `/tanya`
- [ ] Response format disesuaikan dengan Telegram message limits

## Phase 3: Advanced Research -- PLANNED
- [ ] Semantic search (embedding model)
- [ ] Vector store integration (ChromaDB/Faiss)
- [ ] Regulation comparison visual
- [ ] Context-aware multi-turn Q&A di web chat

## Phase 4: Expert System -- FUTURE
- [ ] Compliance reasoning
- [ ] Case-based analysis
- [ ] Risk detection

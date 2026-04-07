# TOOLS.md

## Data Ingestion
- `corpus.jsonl` reader → SQLite loader
- FTS5 builder (built-in SQLite)

## API Endpoints

### GET /api/regulations
- List all regulations with pagination
- Filter: reg_type, year, topic
- Output: `[{identifier, title, year, status, section_count}, ...]`

### GET /api/regulations/{identifier}
- Full regulation detail with sections
- Output: RegulationDoc (full JSONL schema)

### GET /api/regulations/search?q=
- FTS5 text search across title + full_text + sections
- Output: scored list with highlights

### GET /api/articles/{identifier}/{section}
- Get specific pasal/ayat
- Output: `{section_number, text, metadata}`

### POST /api/explain
- LLM-powered explanation of a section
- Input: `{identifier, section}` or raw text
- Output: `{explanation, source}`

### POST /api/compare
- LLM-powered comparison of two sections/regulations
- Input: `{identifier_a, section_a, identifier_b, section_b}`
- Output: `{comparison_table, analysis}`

### POST /api/ask
- Context-aware Q&A with citation
- Input: `{question}`
- Output: `{answer, citations: [{identifier, section}]}`

### GET /chat
- Web Chat UI (Jinja2 template)

## LLM Operations
- prompt_builder: construct prompts with regulation context
- citation_extractor: extract source references from LLM response
- context_retriever: fetch relevant sections via FTS5 before LLM call

## Rules
- All data reads go through SQLite (not JSONL directly after ingest)
- LLM responses must include source citations
- Never return fabricated regulation content
- If no match found → return 404 with clear message
- Rate limiting consideration for production

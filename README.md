# RisetPajak -- Chat Web + API

FastAPI service yang menyediakan **REST API + Web Chat UI** dalam satu service.

## Arsitektur

```
corpus-preparation/    -- Data Pipeline (PDF/DOCX -> JSONL/SQLite)
         ↓
chat-web/              -- FastAPI (API + Web Chat, satu service)
         ↑         ↑
telegram-bot/    (browser)
```

## API Endpoints

| Endpoint | Deskripsi |
|----------|-----------|
| `GET /health` | Health check |
| `GET /` | API discovery |
| `GET /chat` | Web Chat UI |
| `GET /api/regulations` | List semua regulasi |
| `GET /api/regulations/{identifier}` | Detail satu regulasi |
| `GET /api/regulations/search?q=` | Cari regulasi |
| `GET /api/articles/{identifier}/{section}` | Ambil pasal spesifik |
| `POST /api/explain` | Jelaskan pasal (LLM) |
| `POST /api/compare` | Bandingkan regulasi (LLM) |
| `POST /api/ask` | Jawab pertanyaan berbasis konteks (LLM) |

## Instalasi

```bash
cd chat-web
source venv/bin/activate
pip install -e .
```

## Menjalankan

```bash
chat-web               # uvicorn on 0.0.0.0:8000
# atau manual:
uvicorn chatweb.main:app --reload
```

## Struktur

```
chat-web/
├── pyproject.toml
├── src/chatweb/
│   ├── main.py            -- FastAPI app
│   ├── cli.py             -- CLI entry point
│   ├── routes/            -- /api/* endpoints
│   ├── templates/         -- Jinja2 templates (web UI)
│   └── static/            -- CSS, JS
└── tests/
```

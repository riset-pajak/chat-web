"""FastAPI app -- REST API + Web Chat UI for RisetPajak.

Arsitektur: satu service FastAPI yang melayani dua interface:
1. REST API (dipakai telegram-bot, atau client lain)
2. Web Chat UI (dipakai browser)
"""

from __future__ import annotations

from pathlib import Path

from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

# Root: /home/riset-pajak/Github/riset-pajak/
PROJECT_ROOT = Path(__file__).resolve().parents[3]
CORPUS_DIR = PROJECT_ROOT / "corpus-preparation" / "data"

app = FastAPI(
    title="RisetPajak",
    description="API + Web Chat untuk riset regulasi perpajakan Indonesia.",
    version="0.1.0",
)

templates = Jinja2Templates(directory=str(Path(__file__).parent / "templates"))


# ── Health ──────────────────────────────────────────────────────────────

@app.get("/health")
def health_check():
    return {"status": "ok", "version": "0.1.0"}


# ── API Discovery ───────────────────────────────────────────────────────

@app.get("/")
def root():
    return {
        "name": "RisetPajak",
        "api_endpoints": {
            "GET  /api/regulations": "List semua regulasi",
            "GET  /api/regulations/{identifier}": "Detail satu regulasi",
            "GET  /api/regulations/search?q=": "Cari regulasi",
            "GET  /api/articles/{identifier}/{section}": "Ambil pasal spesifik",
            "POST /api/explain": "Jelaskan pasal (LLM)",
            "POST /api/compare": "Bandingkan regulasi (LLM)",
            "POST /api/ask": "Jawab pertanyaan berbasis konteks (LLM)",
        },
        "web": "GET /chat untuk membuka Web Chat UI",
    }


# ── Web Chat (placeholder) ──────────────────────────────────────────────

@app.get("/chat", response_class=HTMLResponse)
async def chat_page(request: Request):
    """Halaman web chat. Template akan diisi setelah UI selesai."""
    return templates.TemplateResponse("chat.html", {"request": request})

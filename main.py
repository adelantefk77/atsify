import base64
import re
from pathlib import Path

from dotenv import load_dotenv
from fastapi import FastAPI, File, Form, HTTPException, UploadFile
from fastapi.responses import HTMLResponse, JSONResponse
from starlette.concurrency import run_in_threadpool

load_dotenv()

from optimizer import is_valid_pdf, optimize_cv  # noqa: E402
from pdf_render import render_cv_pdf  # noqa: E402

BASE_DIR = Path(__file__).parent
TEMPLATES_DIR = BASE_DIR / "templates"

app = FastAPI(title="ATSify")

MAX_PDF_SIZE = 5 * 1024 * 1024  # 5 MB
UPLOAD_CHUNK_SIZE = 64 * 1024
MIN_JOB_POSTING_CHARS = 100
MAX_JOB_POSTING_CHARS = 5000


def _read_template(name: str) -> str:
    return (TEMPLATES_DIR / name).read_text(encoding="utf-8")


async def _read_upload_capped(upload: UploadFile, max_size: int) -> bytes:
    """Read an UploadFile in chunks, aborting as soon as it exceeds max_size
    instead of buffering an unbounded amount of data before checking."""
    chunks = []
    total = 0
    while True:
        chunk = await upload.read(UPLOAD_CHUNK_SIZE)
        if not chunk:
            break
        total += len(chunk)
        if total > max_size:
            raise HTTPException(status_code=400, detail="Plik PDF jest za duży (limit 5MB).")
        chunks.append(chunk)
    return b"".join(chunks)


def _safe_filename_component(name: str) -> str:
    name = re.sub(r"[^\w\-]+", "_", name.strip(), flags=re.UNICODE)
    name = name.strip("_")
    return name[:80] or "CV"


@app.get("/", response_class=HTMLResponse)
def home():
    return _read_template("index.html")


@app.get("/upload", response_class=HTMLResponse)
def upload_page():
    return _read_template("upload.html")


@app.get("/result", response_class=HTMLResponse)
def result_page():
    return _read_template("result.html")


@app.post("/api/optimize")
async def api_optimize(cv_file: UploadFile = File(...), job_posting: str = Form(...)):
    if cv_file.content_type != "application/pdf" and not cv_file.filename.lower().endswith(".pdf"):
        raise HTTPException(status_code=400, detail="Plik CV musi być w formacie PDF.")

    file_bytes = await _read_upload_capped(cv_file, MAX_PDF_SIZE)

    job_posting = job_posting.strip()
    if len(job_posting) < MIN_JOB_POSTING_CHARS:
        raise HTTPException(
            status_code=400,
            detail=f"Treść ogłoszenia jest za krótka (min. {MIN_JOB_POSTING_CHARS} znaków).",
        )
    if len(job_posting) > MAX_JOB_POSTING_CHARS:
        raise HTTPException(
            status_code=400,
            detail=f"Treść ogłoszenia jest za długa (limit {MAX_JOB_POSTING_CHARS} znaków).",
        )

    if not is_valid_pdf(file_bytes):
        raise HTTPException(
            status_code=400,
            detail="Przesłany plik nie jest poprawnym plikiem PDF.",
        )

    try:
        cv_data = await run_in_threadpool(optimize_cv, file_bytes, job_posting)
    except HTTPException:
        raise
    except Exception as exc:
        raise HTTPException(status_code=502, detail=f"Błąd podczas optymalizacji CV: {exc}") from exc

    try:
        pdf_bytes = await run_in_threadpool(render_cv_pdf, cv_data)
    except Exception as exc:
        raise HTTPException(status_code=500, detail=f"Błąd podczas generowania pliku PDF: {exc}") from exc

    safe_name = _safe_filename_component(cv_data.get("contact", {}).get("name", ""))
    filename = f"{safe_name}_CV_ATS.pdf"

    # Stateless response: no server-side storage between requests (required for
    # serverless deployment) — the client holds onto the base64 PDF itself and
    # builds the download locally.
    return JSONResponse(
        {
            "match_score": cv_data.get("match_score", 0),
            "changes": cv_data.get("changes", []),
            "filename": filename,
            "pdf_base64": base64.standard_b64encode(pdf_bytes).decode("ascii"),
        }
    )

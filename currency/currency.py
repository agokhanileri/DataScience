from __future__ import annotations

import sqlite3
from datetime import datetime, timezone
from decimal import Decimal, InvalidOperation, ROUND_HALF_UP
from typing import Any

import httpx
from fastapi import FastAPI, Form, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

DB_PATH = "conversions.db"
RATES_URL = "https://open.er-api.com/v6/latest/USD"

app = FastAPI()
templates = Jinja2Templates(directory="templates")


def db() -> sqlite3.Connection:
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    return conn


def init_db() -> None:
    with db() as conn:
        conn.execute(
            """
            CREATE TABLE IF NOT EXISTS conversions (
              id INTEGER PRIMARY KEY AUTOINCREMENT,
              usd_amount TEXT NOT NULL,
              target_currency TEXT NOT NULL,
              rate REAL NOT NULL,
              converted_amount TEXT NOT NULL,
              created_at TEXT NOT NULL
            )
            """
        )


@app.on_event("startup")
def _startup() -> None:
    init_db()


async def fetch_rates() -> dict[str, Any]:
    async with httpx.AsyncClient(timeout=10.0) as client:
        r = await client.get(RATES_URL)
        r.raise_for_status()
        data = r.json()
    if data.get("result") != "success" or "rates" not in data:
        raise RuntimeError(f"Unexpected rates payload: {data}")
    return data


def q2(x: Decimal) -> Decimal:
    return x.quantize(Decimal("0.01"), rounding=ROUND_HALF_UP)


def load_history(limit: int = 50) -> list[dict[str, Any]]:
    with db() as conn:
        rows = conn.execute(
            """
            SELECT id, usd_amount, target_currency, rate, converted_amount, created_at
            FROM conversions
            ORDER BY id DESC
            LIMIT ?
            """,
            (limit,),
        ).fetchall()
    return [dict(r) for r in rows]


@app.get("/", response_class=HTMLResponse)
async def home(request: Request) -> HTMLResponse:
    history = load_history()
    return templates.TemplateResponse(
        "index.html",
        {"request": request, "currencies": [], "result": None, "error": None, "history": history},
    )


@app.get("/currencies", response_class=HTMLResponse)
async def currencies(request: Request) -> HTMLResponse:
    error = None
    try:
        data = await fetch_rates()
        currencies = sorted(list(data["rates"].keys()))
    except Exception as e:
        currencies = []
        error = f"Failed to load currencies: {e}"
    history = load_history()
    return templates.TemplateResponse(
        "index.html",
        {"request": request, "currencies": currencies, "result": None, "error": error, "history": history},
    )


@app.post("/convert", response_class=HTMLResponse)
async def convert(
    request: Request,
    usd_amount: str = Form(...),
    target_currency: str = Form(...),
) -> HTMLResponse:
    error = None
    result = None

    try:
        amt = Decimal(usd_amount.strip())
        if amt <= 0:
            raise ValueError("USD amount must be > 0")
    except (InvalidOperation, ValueError) as e:
        history = load_history()
        return templates.TemplateResponse(
            "index.html",
            {"request": request, "currencies": [], "result": None, "error": f"Invalid amount: {e}", "history": history},
        )

    try:
        data = await fetch_rates()
        rates: dict[str, float] = data["rates"]
        if target_currency not in rates:
            raise ValueError(f"Unsupported currency: {target_currency}")
        rate = Decimal(str(rates[target_currency]))
        converted = q2(amt * rate)

        created_at = datetime.now(timezone.utc).isoformat()
        with db() as conn:
            conn.execute(
                """
                INSERT INTO conversions (usd_amount, target_currency, rate, converted_amount, created_at)
                VALUES (?, ?, ?, ?, ?)
                """,
                (str(amt), target_currency, float(rate), str(converted), created_at),
            )

        result = {
            "usd_amount": str(amt),
            "target_currency": target_currency,
            "rate": str(rate),
            "converted_amount": str(converted),
            "time": created_at,
        }
    except Exception as e:
        error = f"Conversion failed: {e}"

    try:
        currencies = sorted(list((await fetch_rates())["rates"].keys()))
    except Exception:
        currencies = []

    history = load_history()
    return templates.TemplateResponse(
        "index.html",
        {"request": request, "currencies": currencies, "result": result, "error": error, "history": history},
    )

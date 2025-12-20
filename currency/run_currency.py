#!/usr/bin/env python3
"""Run the currency FastAPI app using Uvicorn.

Usage:
  python scripts/run_currency.py

This is a convenience wrapper so you don't need to type the uvicorn command.
"""

import uvicorn

if __name__ == "__main__":
    uvicorn.run("currency.currency:app", host="127.0.0.1", port=8000, reload=True)

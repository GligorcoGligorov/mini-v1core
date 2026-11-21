# mini-v1core

A small inventory API in the spirit of VergentOne's v1Core: systems with owners, lifecycle, the servers they run on, and their CVEs.

## Stack
FastAPI · Pydantic · pytest · Docker

## Endpoints
- `GET /health` – health check
- `POST /systems` – add a system (validated by Pydantic; 422 on bad input)
- `GET /systems?owner=HR` – list systems, optional filter by owner
- `GET /systems/{id}` – one system, 404 if missing
- `GET /at-risk` – systems with CVEs or end-of-life

## Run locally
    python3 -m venv .venv && source .venv/bin/activate
    pip install -r requirements.txt
    fastapi dev main.py        # http://127.0.0.1:8000/docs

## Test
    pytest

## Docker
    docker build -t mini-v1core:1.0 .
    docker run --rm -p 8001:8000 mini-v1core:1.0

Note: data is kept in memory for simplicity; in production it would live in PostgreSQL.

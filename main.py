from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI(title="mini-v1core")

class System(BaseModel):
    id: int
    name: str
    owner: str
    lifecycle: str = "active"   # active, retiring, eol
    runs_on: list[str] = []
    cves: list[str] = []

DB: dict[int, System] = {}

@app.get("/health")
async def health():
    return {"status": "ok", "version": "1.1"}
    # додадовме "version", за да видиме која верзија одговара

@app.post("/systems", status_code=201)
async def create_system(system: System):
    DB[system.id] = system
    return system

@app.get("/systems")
async def list_systems(owner: str | None = None):
    items = list(DB.values())
    return [s for s in items if owner is None or s.owner == owner]

@app.get("/systems/{system_id}")
async def get_system(system_id: int):
    if system_id not in DB:
        raise HTTPException(status_code=404, detail="System not found")
    return DB[system_id]

@app.get("/at-risk")
async def at_risk():
    return [s for s in DB.values() if s.cves or s.lifecycle == "eol"]
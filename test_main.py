from fastapi.testclient import TestClient
from main import app
# Test
client = TestClient(app)

def test_health():
    assert client.get("/health").json()["status"] == "ok"

def test_at_risk():
    client.post("/systems", json={"id": 1, "name": "PayFlow",
                "owner": "HR", "cves": ["CVE-2021-44228"]})
    names = [s["name"] for s in client.get("/at-risk").json()]
    assert "PayFlow" in names
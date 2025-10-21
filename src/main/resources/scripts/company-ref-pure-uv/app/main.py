from fastapi import FastAPI
from app.routers import companies

app = FastAPI(
    title="Company Reference API",
    version="1.0.0",
    description="""
Reference data service for Corporate Takeover analysis.

Key features:
- Unique keys on name (normalized), LEI, and ticker
- Validate existence by name (`/companies/validate?name=...`)
- CRUD + search by name prefix + key lookups
"""
)

app.include_router(companies.router)

@app.get("/health")
def health():
    try:
        from app.db import get_client
        get_client()  # This will raise an error if not configured
        return {"status": "ok", "database": "connected"}
    except RuntimeError as e:
        return {"status": "ok", "database": "not_configured", "message": str(e)}

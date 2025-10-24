Got it—here’s a **pure async Postgres** version (no SQLAlchemy, no SQLModel) that mirrors typical CRUD you’ve been building. It uses **FastAPI + asyncpg** only.

# Project layout

```
app/
  __init__.py
  main.py
  routes.py
  repository.py
  db.py
  schemas.py
  settings.py
sql/
  001_init.sql
.env.example
pyproject.toml
```

---

# pyproject.toml (minimal)

```toml
[project]
name = "company-crud-asyncpg"
version = "0.1.0"
requires-python = ">=3.11"
dependencies = [
  "fastapi>=0.115.0",
  "uvicorn>=0.30.6",
  "asyncpg>=0.29.0",
  "pydantic>=2.9.0",
  "pydantic-settings>=2.4.0",
]

[tool.uvicorn]
factory = false
```

---

# .env.example

```env
DB_HOST=localhost
DB_PORT=5432
DB_NAME=corpdb
DB_USER=postgres
DB_PASSWORD=password
```

---

# sql/001_init.sql

```sql
CREATE TABLE IF NOT EXISTS companies (
  id BIGSERIAL PRIMARY KEY,
  name TEXT UNIQUE NOT NULL,
  country TEXT,
  sector TEXT,
  isin TEXT UNIQUE,
  ticker TEXT,
  created_at TIMESTAMPTZ NOT NULL DEFAULT now(),
  updated_at TIMESTAMPTZ NOT NULL DEFAULT now()
);

-- Optional index helpers
CREATE INDEX IF NOT EXISTS idx_companies_name ON companies (name);
CREATE INDEX IF NOT EXISTS idx_companies_isin ON companies (isin);
CREATE INDEX IF NOT EXISTS idx_companies_ticker ON companies (ticker);
```

---

# app/settings.py

```python
from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    db_host: str = "localhost"
    db_port: int = 5432
    db_name: str = "corpdb"
    db_user: str = "postgres"
    db_password: str = "password"

    class Config:
        env_file = ".env"

settings = Settings()

def dsn() -> str:
    # asyncpg DSN
    return (
        f"postgresql://{settings.db_user}:{settings.db_password}"
        f"@{settings.db_host}:{settings.db_port}/{settings.db_name}"
    )
```

---

# app/db.py

```python
import asyncpg
from contextlib import asynccontextmanager
from fastapi import FastAPI
from .settings import dsn

pool: asyncpg.Pool | None = None

async def init_pool() -> asyncpg.Pool:
    return await asyncpg.create_pool(
        dsn=dsn(),
        min_size=1,
        max_size=10,
        command_timeout=30,
    )

@asynccontextmanager
async def lifespan(app: FastAPI):
    global pool
    pool = await init_pool()
    try:
        yield
    finally:
        if pool is not None:
            await pool.close()
            pool = None

def get_pool() -> asyncpg.Pool:
    if pool is None:
        raise RuntimeError("DB pool not initialized")
    return pool
```

---

# app/schemas.py

```python
from pydantic import BaseModel, Field, ConfigDict
from typing import Optional
from datetime import datetime

class CompanyBase(BaseModel):
    name: str = Field(..., min_length=1)
    country: Optional[str] = None
    sector: Optional[str] = None
    isin: Optional[str] = Field(None, min_length=2)
    ticker: Optional[str] = Field(None, min_length=1)

class CompanyCreate(CompanyBase):
    pass

class CompanyUpdate(BaseModel):
    name: Optional[str] = None
    country: Optional[str] = None
    sector: Optional[str] = None
    isin: Optional[str] = None
    ticker: Optional[str] = None

class Company(CompanyBase):
    model_config = ConfigDict(from_attributes=True)
    id: int
    created_at: datetime
    updated_at: datetime
```

---

# app/repository.py

```python
from typing import Sequence, Optional
from datetime import datetime, timezone
import asyncpg
from .schemas import CompanyCreate, CompanyUpdate, Company

COLUMNS = "id, name, country, sector, isin, ticker, created_at, updated_at"

def _row_to_company(row: asyncpg.Record) -> Company:
    return Company(
        id=row["id"], name=row["name"], country=row["country"], sector=row["sector"],
        isin=row["isin"], ticker=row["ticker"],
        created_at=row["created_at"], updated_at=row["updated_at"],
    )

async def create_company(conn: asyncpg.Connection, data: CompanyCreate) -> Company:
    q = f"""
    INSERT INTO companies (name, country, sector, isin, ticker)
    VALUES ($1, $2, $3, $4, $5)
    RETURNING {COLUMNS};
    """
    row = await conn.fetchrow(q, data.name, data.country, data.sector, data.isin, data.ticker)
    return _row_to_company(row)

async def get_company_by_id(conn: asyncpg.Connection, company_id: int) -> Optional[Company]:
    q = f"SELECT {COLUMNS} FROM companies WHERE id=$1;"
    row = await conn.fetchrow(q, company_id)
    return _row_to_company(row) if row else None

async def get_company_by_name(conn: asyncpg.Connection, name: str) -> Optional[Company]:
    q = f"SELECT {COLUMNS} FROM companies WHERE name=$1;"
    row = await conn.fetchrow(q, name)
    return _row_to_company(row) if row else None

async def list_companies(conn: asyncpg.Connection, limit: int = 50, offset: int = 0) -> Sequence[Company]:
    q = f"SELECT {COLUMNS} FROM companies ORDER BY id LIMIT $1 OFFSET $2;"
    rows = await conn.fetch(q, limit, offset)
    return [_row_to_company(r) for r in rows]

async def update_company(conn: asyncpg.Connection, company_id: int, patch: CompanyUpdate) -> Optional[Company]:
    # Build dynamic SET list safely
    fields = []
    values = []
    i = 1
    if patch.name is not None:
        fields.append(f"name=${i}"); values.append(patch.name); i += 1
    if patch.country is not None:
        fields.append(f"country=${i}"); values.append(patch.country); i += 1
    if patch.sector is not None:
        fields.append(f"sector=${i}"); values.append(patch.sector); i += 1
    if patch.isin is not None:
        fields.append(f"isin=${i}"); values.append(patch.isin); i += 1
    if patch.ticker is not None:
        fields.append(f"ticker=${i}"); values.append(patch.ticker); i += 1

    if not fields:
        # touch updated_at anyway
        fields.append(f"updated_at=${i}")
        values.append(datetime.now(timezone.utc)); i += 1
    else:
        fields.append(f"updated_at=${i}")
        values.append(datetime.now(timezone.utc)); i += 1

    set_clause = ", ".join(fields)
    # company_id is last parameter
    values.append(company_id)

    q = f"UPDATE companies SET {set_clause} WHERE id=${i} RETURNING {COLUMNS};"
    row = await conn.fetchrow(q, *values)
    return _row_to_company(row) if row else None

async def delete_company(conn: asyncpg.Connection, company_id: int) -> bool:
    q = "DELETE FROM companies WHERE id=$1;"
    res = await conn.execute(q, company_id)  # returns like 'DELETE 1'
    return res.endswith("1")
```

---

# app/routes.py

```python
from fastapi import APIRouter, Depends, HTTPException, Query
import asyncpg
from .db import get_pool
from .schemas import Company, CompanyCreate, CompanyUpdate
from . import repository as repo

router = APIRouter(prefix="/companies", tags=["companies"])

async def with_conn(pool=Depends(get_pool)) -> asyncpg.Connection:
    async with pool.acquire() as conn:
        yield conn

@router.post("", response_model=Company, status_code=201)
async def create_company(body: CompanyCreate, conn: asyncpg.Connection = Depends(with_conn)):
    # unique-by-name check example
    existing = await repo.get_company_by_name(conn, body.name)
    if existing:
        raise HTTPException(status_code=409, detail="Company with this name already exists")
    return await repo.create_company(conn, body)

@router.get("/{company_id}", response_model=Company)
async def get_company(company_id: int, conn: asyncpg.Connection = Depends(with_conn)):
    c = await repo.get_company_by_id(conn, company_id)
    if not c:
        raise HTTPException(status_code=404, detail="Not found")
    return c

@router.get("", response_model=list[Company])
async def list_companies(
    limit: int = Query(50, ge=1, le=200),
    offset: int = Query(0, ge=0),
    conn: asyncpg.Connection = Depends(with_conn),
):
    return await repo.list_companies(conn, limit=limit, offset=offset)

@router.patch("/{company_id}", response_model=Company)
async def update_company(company_id: int, body: CompanyUpdate, conn: asyncpg.Connection = Depends(with_conn)):
    c = await repo.update_company(conn, company_id, body)
    if not c:
        raise HTTPException(status_code=404, detail="Not found")
    return c

@router.delete("/{company_id}", status_code=204)
async def delete_company(company_id: int, conn: asyncpg.Connection = Depends(with_conn)):
    ok = await repo.delete_company(conn, company_id)
    if not ok:
        raise HTTPException(status_code=404, detail="Not found")
    return
```

---

# app/main.py

```python
from fastapi import FastAPI
from .db import lifespan
from .routes import router as companies_router

def create_app() -> FastAPI:
    app = FastAPI(title="Company CRUD (asyncpg)")
    app.include_router(companies_router)
    return app

app = create_app()
app.router.lifespan_context = lifespan
```

---

# Run & init

1. Start Postgres (example):

```bash
docker run --name my-postgres \
  -e POSTGRES_PASSWORD=password -e POSTGRES_DB=corpdb \
  -p 5432:5432 -d postgres:15
```

2. Apply schema:

```bash
psql postgresql://postgres:password@localhost:5432/corpdb -f sql/001_init.sql
```

3. Launch API:

```bash
uvicorn app.main:app --reload
```

Try:

* `POST /companies` with `{ "name":"UBS", "country":"CH", "sector":"IB", "isin":"CH0024899481", "ticker":"UBS" }`
* `GET /companies?limit=20`
* `GET /companies/1`
* `PATCH /companies/1` with `{ "sector":"Wealth" }`
* `DELETE /companies/1`

---

# Pros & cons (quick)

| Approach                       | Pros                                                                                       | Cons                                                                            | When to choose                                                 |
| ------------------------------ | ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------- | -------------------------------------------------------------- |
| **Raw asyncpg (this)**         | Smallest deps, fastest path (no ORM overhead), full SQL control, easy to reason about perf | More boilerplate, manual SQL, hand-rolled mapping/validation, harder migrations | Latency-sensitive services, complex SQL, you want full control |
| **SQLAlchemy 2.x (async ORM)** | Mature, rich ecosystem, relationships, migrations (Alembic), query builder                 | Learning curve, some overhead vs raw, declarative complexity                    | Most microservices with non-trivial models/relations           |
| **SQLModel**                   | Pydantic models + SQLAlchemy under one roof, nice DX, less boilerplate                     | Tied to SQLAlchemy under the hood, smaller ecosystem vs pure SA                 | FastAPI-heavy stacks where schemas and models align nicely     |

If you want, I can drop this into a **zip** with a tiny GitHub Action that runs `uvicorn` on Azure App Service (or add a Dockerfile).

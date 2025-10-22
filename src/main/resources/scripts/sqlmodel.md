Perfect ✅ — let’s make this **fully async FastAPI + SQLModel + PostgreSQL** CRUD for `Workflow`.
No auth, no profile, just clean asynchronous code using `sqlmodel.ext.asyncio.AsyncSession` and `asyncpg`.

---

## ⚙️ Folder

```
src/
 ├─ main.py
 ├─ database.py
 ├─ entities.py
 └─ routers/
    └─ workflows.py
```

---

## 🧩 pyproject.toml

Use **`sqlmodel`** + **`asyncpg`** (not psycopg3 since async SQLModel prefers asyncpg):

```toml
[project]
name = "corporate-takeover-api"
version = "0.1.0"
requires-python = ">=3.11"
dependencies = [
  "fastapi>=0.115",
  "uvicorn>=0.30",
  "sqlmodel>=0.0.22",
  "asyncpg>=0.29"
]
```

Install:

```bash
uv sync
```

---

## 🧩 .env

```
DATABASE_URL=postgresql+asyncpg://postgres:password@localhost:5432/corp_takeover
```

---

## 🧩 database.py

```python
import os
from sqlmodel import SQLModel
from sqlmodel.ext.asyncio.session import AsyncSession
from sqlalchemy.ext.asyncio import create_async_engine
from sqlalchemy.orm import sessionmaker

DATABASE_URL = os.getenv(
    "DATABASE_URL",
    "postgresql+asyncpg://postgres:password@localhost:5432/corp_takeover",
)

engine = create_async_engine(DATABASE_URL, echo=False, future=True)
AsyncSessionLocal = sessionmaker(engine, class_=AsyncSession, expire_on_commit=False)

async def get_session():
    async with AsyncSessionLocal() as session:
        yield session

async def create_tables():
    async with engine.begin() as conn:
        await conn.run_sync(SQLModel.metadata.create_all)
```

---

## 🧩 entities.py

```python
from datetime import datetime, timezone
from typing import Optional, Literal
from uuid import UUID, uuid4
from pydantic import EmailStr
from sqlmodel import SQLModel, Field

WorkflowStatus = Literal[
    "draft", "in_queue", "in_progress", "awaiting_feedback", "failed", "completed"
]

class Workflow(SQLModel, table=True):
    id: UUID = Field(default_factory=uuid4, primary_key=True)
    gpn: str = Field(index=True, max_length=64)
    name: str = Field(max_length=256)
    email: EmailStr
    status: WorkflowStatus = "draft"
    created_at: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))

class WorkflowCreate(SQLModel):
    gpn: str
    name: str
    email: EmailStr
    status: WorkflowStatus = "draft"

class WorkflowUpdate(SQLModel):
    name: Optional[str] = None
    email: Optional[EmailStr] = None
    status: Optional[WorkflowStatus] = None
```

---

## 🧩 routers/workflows.py

```python
from typing import List
from uuid import UUID
from fastapi import APIRouter, Depends, HTTPException, status
from sqlmodel import select
from sqlmodel.ext.asyncio.session import AsyncSession

from database import get_session
from entities import Workflow, WorkflowCreate, WorkflowUpdate

router = APIRouter(prefix="/workflows", tags=["workflow"])

@router.get("/", response_model=List[Workflow])
async def list_workflows(session: AsyncSession = Depends(get_session)):
    result = await session.exec(select(Workflow).order_by(Workflow.created_at.desc()))
    return result.all()

@router.get("/{id}", response_model=Workflow)
async def get_workflow(id: UUID, session: AsyncSession = Depends(get_session)):
    wf = await session.get(Workflow, id)
    if not wf:
        raise HTTPException(404, "Workflow not found")
    return wf

@router.post("/", response_model=Workflow, status_code=status.HTTP_201_CREATED)
async def create_workflow(payload: WorkflowCreate, session: AsyncSession = Depends(get_session)):
    wf = Workflow(**payload.model_dump())
    session.add(wf)
    await session.commit()
    await session.refresh(wf)
    return wf

@router.put("/{id}", response_model=Workflow)
async def update_workflow(id: UUID, payload: WorkflowUpdate, session: AsyncSession = Depends(get_session)):
    wf = await session.get(Workflow, id)
    if not wf:
        raise HTTPException(404, "Workflow not found")

    for k, v in payload.model_dump(exclude_unset=True).items():
        setattr(wf, k, v)

    session.add(wf)
    await session.commit()
    await session.refresh(wf)
    return wf

@router.delete("/{id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_workflow(id: UUID, session: AsyncSession = Depends(get_session)):
    wf = await session.get(Workflow, id)
    if not wf:
        return
    await session.delete(wf)
    await session.commit()
```

---

## 🧩 main.py

```python
from fastapi import FastAPI
from database import create_tables
from routers.workflows import router as workflows_router

app = FastAPI(title="Corporate Takeover API", version="1.0.0")

@app.on_event("startup")
async def startup():
    await create_tables()

app.include_router(workflows_router)

@app.get("/healthz")
async def health():
    return {"ok": True}
```

---

## 🧩 Run Postgres

```bash
docker run --name my-postgres \
  -e POSTGRES_PASSWORD=password \
  -e POSTGRES_USER=postgres \
  -e POSTGRES_DB=corp_takeover \
  -p 5432:5432 -d container-registry.ubs.net/postgres:15.9
```

---

## 🧩 Run the API

```bash
uv run uvicorn main:app --reload --port 8000
```

Then open: [http://localhost:8000/docs](http://localhost:8000/docs)

---

## 🧩 Quick sanity check (curl or HTTP client)

```bash
curl -X POST http://localhost:8000/workflows \
     -H "Content-Type: application/json" \
     -d '{"gpn":"GPN100","name":"Alice","email":"alice@ubs.com","status":"in_queue"}'
```

---

## ✅ Summary

| Feature               | Status                  |
| --------------------- | ----------------------- |
| **Framework**         | FastAPI (async)         |
| **ORM**               | SQLModel (async engine) |
| **DB**                | PostgreSQL via asyncpg  |
| **Auth/Profile**      | None                    |
| **Startup migration** | Auto create table       |
| **CRUD**              | Fully async, complete   |

---

Would you like me to add an **initial SQL seed script** (auto-run on startup if table empty)?
That can help with demo data population.

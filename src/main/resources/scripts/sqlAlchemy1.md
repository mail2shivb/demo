Perfect 👌 — let’s now rebuild your **FastAPI + SQLAlchemy (async)** CRUD for `Workflow`
✅ PostgreSQL backend
✅ pure `async` (no SQLModel)
✅ minimal, clean, production-ready

---

## ⚙️ Folder structure

```
src/
 ├─ main.py
 ├─ database.py
 ├─ models.py
 ├─ schemas.py
 └─ routers/
    └─ workflows.py
```

---

## 🧩 `pyproject.toml`

Use **SQLAlchemy async** + **asyncpg**:

```toml
[project]
name = "corporate-takeover-api"
version = "0.1.0"
requires-python = ">=3.11"
dependencies = [
  "fastapi>=0.115",
  "uvicorn>=0.30",
  "sqlalchemy>=2.0",
  "asyncpg>=0.29",
  "pydantic>=2.8"
]
```

Install:

```bash
uv sync
```

---

## 🧩 `.env`

```
DATABASE_URL=postgresql+asyncpg://postgres:password@localhost:5432/corp_takeover
```

---

## 🧩 `database.py`

```python
import os
from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.orm import sessionmaker, declarative_base

DATABASE_URL = os.getenv(
    "DATABASE_URL",
    "postgresql+asyncpg://postgres:password@localhost:5432/corp_takeover",
)

engine = create_async_engine(DATABASE_URL, echo=False, future=True)

AsyncSessionLocal = sessionmaker(
    bind=engine,
    class_=AsyncSession,
    expire_on_commit=False,
)

Base = declarative_base()

async def get_session():
    async with AsyncSessionLocal() as session:
        yield session

async def init_db():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
```

---

## 🧩 `models.py`

```python
from datetime import datetime, timezone
from uuid import uuid4
from sqlalchemy import String, DateTime
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import Mapped, mapped_column
from database import Base

class Workflow(Base):
    __tablename__ = "workflows"

    id: Mapped[uuid4] = mapped_column(UUID(as_uuid=True), primary_key=True, default=uuid4)
    gpn: Mapped[str] = mapped_column(String(64), nullable=False, index=True)
    name: Mapped[str] = mapped_column(String(256), nullable=False)
    email: Mapped[str] = mapped_column(String(256), nullable=False)
    status: Mapped[str] = mapped_column(String(32), nullable=False, default="draft")
    created_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True), default=lambda: datetime.now(timezone.utc), nullable=False
    )
```

---

## 🧩 `schemas.py`

```python
from datetime import datetime
from typing import Optional, Literal
from uuid import UUID
from pydantic import BaseModel, EmailStr

WorkflowStatus = Literal[
    "draft", "in_queue", "in_progress", "awaiting_feedback", "failed", "completed"
]

class WorkflowBase(BaseModel):
    gpn: str
    name: str
    email: EmailStr
    status: WorkflowStatus = "draft"

class WorkflowCreate(WorkflowBase):
    pass

class WorkflowUpdate(BaseModel):
    name: Optional[str] = None
    email: Optional[EmailStr] = None
    status: Optional[WorkflowStatus] = None

class WorkflowOut(WorkflowBase):
    id: UUID
    created_at: datetime

    class Config:
        from_attributes = True
```

---

## 🧩 `routers/workflows.py`

```python
from typing import List
from uuid import UUID
from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from database import get_session
from models import Workflow
from schemas import WorkflowCreate, WorkflowUpdate, WorkflowOut

router = APIRouter(prefix="/workflows", tags=["workflow"])

@router.get("/", response_model=List[WorkflowOut])
async def list_workflows(session: AsyncSession = Depends(get_session)):
    result = await session.execute(select(Workflow).order_by(Workflow.created_at.desc()))
    return result.scalars().all()

@router.get("/{id}", response_model=WorkflowOut)
async def get_workflow(id: UUID, session: AsyncSession = Depends(get_session)):
    wf = await session.get(Workflow, id)
    if not wf:
        raise HTTPException(404, "Workflow not found")
    return wf

@router.post("/", response_model=WorkflowOut, status_code=status.HTTP_201_CREATED)
async def create_workflow(payload: WorkflowCreate, session: AsyncSession = Depends(get_session)):
    wf = Workflow(**payload.model_dump())
    session.add(wf)
    await session.commit()
    await session.refresh(wf)
    return wf

@router.put("/{id}", response_model=WorkflowOut)
async def update_workflow(id: UUID, payload: WorkflowUpdate, session: AsyncSession = Depends(get_session)):
    wf = await session.get(Workflow, id)
    if not wf:
        raise HTTPException(404, "Workflow not found")

    for k, v in payload.model_dump(exclude_unset=True).items():
        setattr(wf, k, v)

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

## 🧩 `main.py`

```python
from fastapi import FastAPI
from database import init_db
from routers.workflows import router as workflows_router

app = FastAPI(title="Corporate Takeover API", version="1.0.0")

@app.on_event("startup")
async def on_startup():
    await init_db()

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

Open Swagger:
👉 [http://localhost:8000/docs](http://localhost:8000/docs)

---

## ✅ Quick test

**Create:**

```bash
curl -X POST http://localhost:8000/workflows \
  -H "Content-Type: application/json" \
  -d '{"gpn":"GPN101","name":"Alice","email":"alice@ubs.com","status":"in_queue"}'
```

**List:**
`curl http://localhost:8000/workflows`

---

### ⚡ Summary

| Component     | Tech                         |
| ------------- | ---------------------------- |
| Web framework | FastAPI                      |
| ORM           | SQLAlchemy 2.0 (async)       |
| DB driver     | asyncpg                      |
| DB            | PostgreSQL                   |
| Style         | Pure async, no profiles/auth |
| Features      | Auto table create, full CRUD |

---

Would you like me to next add:

* 🧱 Alembic migration support (for schema evolution), or
* 🧪 async unit tests (pytest + async SQLAlchemy + FastAPI TestClient)?

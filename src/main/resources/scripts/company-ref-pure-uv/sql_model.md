Got it — here’s the same endpoint rebuilt with **SQLModel (async)** instead of “raw” SQLAlchemy. It keeps your router shape, a typed session dependency, and the “transform to response” step.

---

# `src/database.py`

```python
from collections.abc import AsyncGenerator
from sqlmodel import SQLModel
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.orm import sessionmaker

DATABASE_URL = "postgresql+asyncpg://postgres:password@localhost:5432/mydb"

engine = create_async_engine(DATABASE_URL, echo=False, future=True)
_session = sessionmaker(engine, class_=AsyncSession, expire_on_commit=False)

async def init_db() -> None:
    # call this once at startup
    async with engine.begin() as conn:
        await conn.run_sync(SQLModel.metadata.create_all)

async def get_session() -> AsyncGenerator[AsyncSession, None]:
    async with _session() as session:
        yield session
```

---

# `src/entities_sqlmodel.py`

```python
from __future__ import annotations

from datetime import datetime, timezone
from enum import Enum
from typing import Sequence

from sqlmodel import SQLModel, Field


class WorkflowStatus(str, Enum):
    draft = "draft"
    active = "active"
    archived = "archived"


# DB table
class Workflow(SQLModel, table=True):
    __tablename__ = "workflows"

    row_key: str = Field(primary_key=True, max_length=64)
    created_by_gpn: str = Field(max_length=64)
    created_by_name: str = Field(max_length=256)
    created_by_email: str = Field(max_length=256)
    status: WorkflowStatus = Field(default=WorkflowStatus.draft)
    created_at: datetime = Field(
        default_factory=lambda: datetime.now(timezone.utc), nullable=False
    )


# Response DTO (what your API returns)
class WorkflowBase(SQLModel):
    gpn: str
    name: str
    email: str
    created_at: datetime
    status: WorkflowStatus


def transform_workflows_to_response(
    workflows: Sequence[Workflow],
) -> list[WorkflowBase]:
    return [
        WorkflowBase(
            gpn=w.created_by_gpn,
            name=w.created_by_name,
            email=w.created_by_email,
            created_at=w.created_at,
            status=w.status,
        )
        for w in workflows
    ]
```

---

# `src/routers/workflow_sqlmodel.py`

```python
from collections.abc import Sequence
from typing import Annotated

from fastapi import APIRouter, Depends
from sqlmodel import select
from sqlmodel.ext.asyncio.session import AsyncSession

from src.database import get_session
from src.entities_sqlmodel import Workflow, WorkflowBase, transform_workflows_to_response

router = APIRouter(prefix="/workflows/sqlmodel", tags=["workflow"])

SessionDep = Annotated[AsyncSession, Depends(get_session)]


@router.get("/", response_model=list[WorkflowBase])
async def list_workflows(session: SessionDep) -> list[WorkflowBase]:
    stmt = select(Workflow).order_by(Workflow.created_at.desc())
    result = await session.execute(stmt)
    workflows: Sequence[Workflow] = result.scalars().all()
    return transform_workflows_to_response(workflows)
```

---

### Notes

* **Why `AsyncSession`?** It lets FastAPI handle DB I/O without blocking the event loop, so other requests aren’t stalled while awaiting Postgres. With SQLModel async you still use SQLAlchemy’s `AsyncSession` under the hood.
* If you don’t need the transform step, you can **rename the columns to match the DTO** (or use `Field(..., alias="...")` with Pydantic v2 config), then return `list[Workflow]` directly as your `response_model`.

Wire `init_db()` in your FastAPI startup event:

```python
@app.on_event("startup")
async def on_startup():
    await init_db()
```

This is a drop-in swap for your SQLAlchemy version, just using SQLModel’s ergonomics.

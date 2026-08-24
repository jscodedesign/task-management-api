from datetime import datetime

from pydantic import BaseModel


class TodoCreate(BaseModel):
    title: str


class TodoUpdate(BaseModel):
    title: str | None = None
    completed: bool | None = None
    description: str | None = None
    priority: int | None = None
    due_date: datetime | None = None


class TodoResponse(BaseModel):
    id: int
    title: str
    completed: bool
    description: str | None
    priority: int
    due_date: datetime | None
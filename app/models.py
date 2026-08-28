from datetime import datetime

from sqlalchemy import ForeignKey, String
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column


class Base(DeclarativeBase):
    pass


class User(Base):
    __tablename__ = "users"

    id: Mapped[int] = mapped_column(primary_key=True)
    username: Mapped[str] = mapped_column(String(50), unique=True, index=True)
    password_hash: Mapped[str] = mapped_column(String(255))


class Task(Base):
    __tablename__ = "tasks"

    id: Mapped[int] = mapped_column(primary_key=True)
    title: Mapped[str] = mapped_column(String(200))
    completed: Mapped[bool] = mapped_column(default=False)
    description: Mapped[str | None] = mapped_column(String(500), nullable=True)
    priority: Mapped[int] = mapped_column(default=1)
    due_date: Mapped[datetime | None] = mapped_column(nullable=True)
    user_id: Mapped[int] = mapped_column(ForeignKey("users.id"))
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from sqlalchemy import select

from app.database import SessionLocal
from app.models import Task, User
from app.schemas import (
    TaskCreate,
    TaskUpdate,
    TaskResponse,
    UserCreate,
    UserResponse,
    UserLogin,
    TokenResponse,
)
from app.auth import hash_password, verify_password, create_access_token


router = APIRouter()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


# =========================
# USERS
# =========================

@router.post("/users", response_model=UserResponse)
def create_user(user: UserCreate, db: Session = Depends(get_db)):
    existing_user = db.execute(
        select(User).where(User.username == user.username)
    ).scalar_one_or_none()

    if existing_user is not None:
        raise HTTPException(
            status_code=400,
            detail="Username already exists"
        )

    new_user = User(
        username=user.username,
        password_hash=hash_password(user.password)
    )

    db.add(new_user)
    db.commit()
    db.refresh(new_user)

    return new_user


@router.post("/login", response_model=TokenResponse)
def login(user: UserLogin, db: Session = Depends(get_db)):
    existing_user = db.execute(
        select(User).where(User.username == user.username)
    ).scalar_one_or_none()

    if existing_user is None:
        raise HTTPException(
            status_code=401,
            detail="Invalid username or password"
        )

    if not verify_password(
        user.password,
        existing_user.password_hash
    ):
        raise HTTPException(
            status_code=401,
            detail="Invalid username or password"
        )

    access_token = create_access_token(existing_user.id)

    return {
        "access_token": access_token,
        "token_type": "bearer"
    }


# =========================
# TASKS
# =========================

@router.post("/tasks", response_model=TaskResponse)
def create_task(
    task: TaskCreate,
    db: Session = Depends(get_db)
):
    new_task = Task(
        title=task.title,
        user_id=1
    )

    db.add(new_task)
    db.commit()
    db.refresh(new_task)

    return new_task


@router.get("/tasks", response_model=list[TaskResponse])
def get_tasks(db: Session = Depends(get_db)):
    statement = select(Task)

    result = db.execute(statement)

    tasks = result.scalars().all()

    return tasks


@router.get("/tasks/{task_id}", response_model=TaskResponse)
def get_task(
    task_id: int,
    db: Session = Depends(get_db)
):
    statement = select(Task).where(Task.id == task_id)

    result = db.execute(statement)

    task = result.scalar_one_or_none()

    if task is None:
        raise HTTPException(
            status_code=404,
            detail="Task not found"
        )

    return task


@router.put("/tasks/{task_id}", response_model=TaskResponse)
def update_task(
    task_id: int,
    task_update: TaskUpdate,
    db: Session = Depends(get_db)
):
    statement = select(Task).where(Task.id == task_id)

    result = db.execute(statement)

    task = result.scalar_one_or_none()

    if task is None:
        raise HTTPException(
            status_code=404,
            detail="Task not found"
        )

    task.title = task_update.title
    task.completed = task_update.completed

    db.commit()
    db.refresh(task)

    return task


@router.delete("/tasks/{task_id}")
def delete_task(
    task_id: int,
    db: Session = Depends(get_db)
):
    statement = select(Task).where(Task.id == task_id)

    result = db.execute(statement)

    task = result.scalar_one_or_none()

    if task is None:
        raise HTTPException(
            status_code=404,
            detail="Task not found"
        )

    db.delete(task)
    db.commit()

    return {
        "message": "Task deleted"
    }

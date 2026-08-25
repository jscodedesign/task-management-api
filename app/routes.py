from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from sqlalchemy import select

from app.database import SessionLocal
from app.models import Todo
from app.schemas import TodoCreate, TodoUpdate

router = APIRouter()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.post("/todos")
def create_todo(todo: TodoCreate, db: Session = Depends(get_db)):
    new_todo = Todo(
        title=todo.title
    )

    db.add(new_todo)
    db.commit()
    db.refresh(new_todo)

    return new_todo

@router.get("/todos")
def get_todos(db: Session = Depends(get_db)):
    statement = select(Todo)

    result = db.execute(statement)

    todos = result.scalars().all()

    return todos



@router.get("/todos/{todo_id}")
def get_todo(todo_id: int, db: Session = Depends(get_db)):
    statement = select(Todo).where(Todo.id == todo_id)

    result = db.execute(statement)

    todo = result.scalar_one_or_none()

    return todo




@router.delete("/todos/{todo_id}")
def delete_todo(todo_id: int, db: Session = Depends(get_db)):
    statement = select(Todo).where(Todo.id == todo_id)
    result = db.execute(statement)

    todo = result.scalar_one_or_none()

    if todo is None:
        raise HTTPException(status_code=404, detail="Todo nicht gefunden")

    db.delete(todo)
    db.commit()

    return {"message": "Todo gelöscht"}





@router.put("/todos/{todo_id}")
def update_todo(
    todo_id: int,
    todo_update: TodoUpdate,
    db: Session = Depends(get_db)
):
    statement = select(Todo).where(Todo.id == todo_id)
    result = db.execute(statement)

    todo = result.scalar_one_or_none()

    if todo is None:
        raise HTTPException(status_code=404, detail="Todo nicht gefunden")

    todo.title = todo_update.title
    todo.completed = todo_update.completed

    db.commit()
    db.refresh(todo)

    return todo
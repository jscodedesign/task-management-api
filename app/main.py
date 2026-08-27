from fastapi import FastAPI
from app.database import engine
from app.models import Base
from app.routes import router

app = FastAPI(
    title="Task Management API",
    description="A RESTful API for managing tasks and user data",
    version="1.0.0",
)


app.include_router(router)

@app.get("/")
def root():
    return {"message": "Task API is running!"}

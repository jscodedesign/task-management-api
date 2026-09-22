# Task Management API

<p align="center">
  <img src="https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white" alt="Python">
  <img src="https://img.shields.io/badge/FastAPI-009688?style=for-the-badge&logo=fastapi&logoColor=white" alt="FastAPI">
  <img src="https://img.shields.io/badge/PostgreSQL-4169E1?style=for-the-badge&logo=postgresql&logoColor=white" alt="PostgreSQL">
  <img src="https://img.shields.io/badge/SQLAlchemy-D71F00?style=for-the-badge&logo=sqlalchemy&logoColor=white" alt="SQLAlchemy">
  <img src="https://img.shields.io/badge/Alembic-6BA81E?style=for-the-badge" alt="Alembic">
  <img src="https://img.shields.io/badge/Pydantic-E92063?style=for-the-badge&logo=pydantic&logoColor=white" alt="Pydantic">
  <img src="https://img.shields.io/badge/JWT-000000?style=for-the-badge&logo=jsonwebtokens&logoColor=white" alt="JWT">
  <img src="https://img.shields.io/badge/Pytest-0A9EDC?style=for-the-badge&logo=pytest&logoColor=white" alt="Pytest">
  <img src="https://img.shields.io/badge/Uvicorn-499848?style=for-the-badge" alt="Uvicorn">
  <img src="https://img.shields.io/badge/Docker-2496ED?style=for-the-badge&logo=docker&logoColor=white" alt="Docker">
  <img src="https://img.shields.io/badge/GitHub_Actions-2088FF?style=for-the-badge&logo=github-actions&logoColor=white" alt="GitHub Actions">
</p>

<p align="center">
  <a href="#features">Features</a> •
  <a href="#tech-stack">Tech Stack</a> •
  <a href="#project-structure">Project Structure</a> •
  <a href="#getting-started">Getting Started</a> •
  <a href="#testing">Testing</a> •
  <a href="#docker">Docker</a>
</p>

---

A RESTful API for managing tasks and users, built with **FastAPI** and **PostgreSQL**.

The project provides JWT-based authentication, user-specific task management, database migrations with Alembic, request validation with Pydantic, and automated testing with pytest.

## 🛠️ Tech Stack

| Technology | Purpose |
|:---|:---|
| **Python** | Programming language |
| **FastAPI** | REST API framework |
| **PostgreSQL** | Relational database |
| **SQLAlchemy** | ORM / database interaction |
| **Alembic** | Database migrations |
| **Pydantic** | Request and response validation |
| **JWT** | Authentication |
| **Pytest** | Automated testing |
| **Uvicorn** | ASGI server |
| **Docker** | Containerization |
| **GitHub Actions** | Continuous integration |

## ✨ Features

- User registration
- JWT-based authentication
- Protected task endpoints
- Create, read, update, and delete tasks
- User-specific task ownership
- Task priorities
- Task descriptions
- Due dates
- PostgreSQL database
- SQLAlchemy ORM
- Alembic database migrations
- Request and response validation with Pydantic
- Interactive API documentation with Swagger UI and ReDoc
- Automated tests with pytest

## 📂 Project Structure

```text
task-management-api/
│
├── .github/
│   └── workflows/
│
├── alembic/
│   ├── versions/
│   ├── env.py
│   ├── script.py.mako
│   └── README
│
├── app/
│   ├── auth.py
│   ├── database.py
│   ├── main.py
│   ├── models.py
│   ├── routes.py
│   ├── schemas.py
│   └── __init__.py
│
├── tests/
│   ├── conftest.py
│   └── test_tasks.py
│
├── .dockerignore
├── .env.example
├── .gitignore
├── Dockerfile
├── docker-compose.yml
├── alembic.ini
├── pyproject.toml
├── requirements.txt
└── README.md
```

## 🚀 Getting Started

### 1. Clone the repository

    git clone https://github.com/jscodedesign/task-management-api.git
    cd task-management-api

### 2. Create a virtual environment

On Windows:

    python -m venv .venv

Activate the virtual environment:

    .venv\Scripts\activate

### 3. Install dependencies

    python -m pip install -r requirements.txt

### 4. Configure environment variables

Create a `.env` file in the project root:

    DATABASE_URL=postgresql+psycopg://postgres:your_password@localhost/postgres
    SECRET_KEY=your_secret_key

The `.env` file contains sensitive configuration and must **not** be committed to the repository.

It is excluded through `.gitignore`.

### 5. Set up the database

Make sure PostgreSQL is running and the configured database is available.

Run the existing Alembic migrations:

    alembic upgrade head

## Running the API

Start the development server with:

    uvicorn app.main:app --reload

The API will be available at:

    http://127.0.0.1:8000

## 📚 API Documentation

FastAPI automatically generates interactive API documentation.

### Swagger UI

Open:

    http://127.0.0.1:8000/docs

Swagger UI can be used to explore the available endpoints and send requests directly to the API.

### ReDoc

Open:

    http://127.0.0.1:8000/redoc

# 🔐 Authentication

The API uses **JWT bearer authentication** to protect task endpoints.

### Authentication Flow

    Create User
         │
         ▼
       Login
         │
         ▼
    Receive JWT Token
         │
         ▼
    Send Token with Requests
         │
         ▼
    Access Protected Endpoints

First, create a user through the user registration endpoint.

After logging in, the API returns an access token.

The token can then be provided in the `Authorization` header:

    Authorization: Bearer <your-access-token>

In Swagger UI, click **Authorize** and provide the required authentication credentials.

Protected endpoints require a valid JWT token.

## 📝 API Examples

### Create a User

**Endpoint**

    POST /users

**Request**

    {
      "username": "john",
      "password": "securepassword"
    }

**Response**

    {
      "id": 1,
      "username": "john"
    }

### Create a Task

**Endpoint**

    POST /tasks

**Request**

    {
      "title": "Learn Python",
      "description": "Finish the FastAPI project",
      "priority": 1
    }

**Response**

    {
      "id": 1,
      "title": "Learn Python",
      "completed": false,
      "description": "Finish the FastAPI project",
      "priority": 1,
      "due_date": null
    }

## 🔄 Database Migrations

The project uses **Alembic** to manage database schema changes.

After modifying the SQLAlchemy models, create a new migration:

    alembic revision --autogenerate -m "describe your change"

Apply pending migrations:

    alembic upgrade head

Roll back the latest migration:

    alembic downgrade -1

## 🧪 Testing

Run the test suite with:

    pytest

For more detailed output:

    pytest -v

The tests cover the API functionality and help ensure that existing behavior remains stable when the project is changed.

## 🔒 Environment Variables

| Variable | Description |
|---|---|
| `DATABASE_URL` | PostgreSQL connection string |
| `SECRET_KEY` | Secret key used for JWT authentication |

> **Security:** Never commit real credentials, secret keys, database passwords, or other sensitive configuration to the repository.

## 🐳 Docker

The project includes Docker configuration for running the API and PostgreSQL together. Database migrations are applied automatically when the API container starts.

Start the containers with:

    docker compose up --build

Docker Desktop with the WSL 2 based engine is required.
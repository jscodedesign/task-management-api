# Task Management API

A RESTful API for managing tasks and users, built with **FastAPI** and **PostgreSQL**.

The project provides JWT-based authentication, user-specific task management, database migrations with Alembic, request validation with Pydantic, and automated testing with pytest.

## Tech Stack

- **Python**
- **FastAPI**
- **PostgreSQL**
- **SQLAlchemy**
- **Alembic**
- **Pydantic**
- **JWT**
- **Pytest**
- **Uvicorn**

## Features

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

## Project Structure

    todo-app/
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
    ├── .gitignore
    ├── requirements.txt
    └── README.md

## Getting Started

### 1. Clone the repository

    git clone <your-repository-url>
    cd todo-app

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

## API Documentation

FastAPI automatically generates interactive API documentation.

### Swagger UI

Open:

    http://127.0.0.1:8000/docs

Swagger UI can be used to explore the available endpoints and send requests directly to the API.

### ReDoc

Open:

    http://127.0.0.1:8000/redoc

## Authentication

The API uses **JWT bearer authentication** to protect task endpoints.

First, create a user through the user registration endpoint.

After logging in, the API returns an access token.

The token can then be provided in the `Authorization` header:

    Authorization: Bearer <your-access-token>

In Swagger UI, click **Authorize** and provide the required authentication credentials.

Protected endpoints require a valid JWT token.

## API Examples

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

## Database Migrations

The project uses **Alembic** to manage database schema changes.

After modifying the SQLAlchemy models, create a new migration:

    alembic revision --autogenerate -m "describe your change"

Apply pending migrations:

    alembic upgrade head

Roll back the latest migration:

    alembic downgrade -1

## Testing

Run the test suite with:

    pytest

For more detailed output:

    pytest -v

The tests cover the API functionality and help ensure that existing behavior remains stable when the project is changed.

## Environment Variables

| Variable | Description |
|---|---|
| `DATABASE_URL` | PostgreSQL connection string |
| `SECRET_KEY` | Secret key used for JWT authentication |

> **Security:** Never commit real credentials, secret keys, database passwords, or other sensitive configuration to the repository.

## Development

The project is currently focused on the backend/API layer.

Potential future improvements include:

- Refresh token support
- More granular authorization
- Task filtering and sorting
- Pagination
- Improved error handling
- Additional test coverage
- Docker support
- CI/CD with GitHub Actions
- Production deployment

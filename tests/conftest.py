import os

import pytest
from dotenv import load_dotenv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from fastapi.testclient import TestClient

from app.main import app
from app.models import Base, User
from app.database import get_db
from app.auth import hash_password


load_dotenv(".env.test")

DATABASE_URL = os.getenv("DATABASE_URL")

engine = create_engine(DATABASE_URL)
TestingSessionLocal = sessionmaker(bind=engine)


@pytest.fixture
def client():
    Base.metadata.create_all(bind=engine)

    db = TestingSessionLocal()

    test_user = User(
        username="testuser",
        password_hash=hash_password("testpassword"),
    )

    db.add(test_user)
    db.commit()
    db.refresh(test_user)

    def override_get_db():
        try:
            yield db
        finally:
            pass

    app.dependency_overrides[get_db] = override_get_db

    with TestClient(app) as test_client:
        login_response = test_client.post(
            "/login",
            json={
                "username": "testuser",
                "password": "testpassword",
            },
        )

        token = login_response.json()["access_token"]

        test_client.headers.update(
            {"Authorization": f"Bearer {token}"}
        )

        yield test_client

    app.dependency_overrides.clear()
    db.close()
    Base.metadata.drop_all(bind=engine)


@pytest.fixture
def second_client(client):
    db = TestingSessionLocal()

    second_user = User(
        username="seconduser",
        password_hash=hash_password("secondpassword")
    )

    db.add(second_user)
    db.commit()
    db.refresh(second_user)

    app.dependency_overrides[get_db] = lambda: db

    with TestClient(app) as test_client:
        login_response = test_client.post(
            "/login",
            json={
                "username": "seconduser",
                "password": "secondpassword",
            }
        )

        token = login_response.json()["access_token"]

        test_client.headers.update(
            {"Authorization": f"Bearer {token}"}
        )

        yield test_client

    app.dependency_overrides.clear()
    db.close()


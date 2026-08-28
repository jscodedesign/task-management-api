import os

import pytest
from dotenv import load_dotenv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from fastapi.testclient import TestClient

from app.main import app
from app.models import Base, User
from app.routes import get_db


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
        password_hash="testpassword"
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
        yield test_client

    app.dependency_overrides.clear()
    db.close()
    Base.metadata.drop_all(bind=engine)

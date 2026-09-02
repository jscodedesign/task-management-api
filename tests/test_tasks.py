def test_root(client):
    response = client.get("/")

    assert response.status_code == 200
    assert response.json() == {"message": "Task API is running!"}


def test_create_task(client):
    response = client.post(
        "/tasks",
        json={"title": "Learn FastAPI"}
    )

    assert response.status_code == 200

    data = response.json()

    assert data["title"] == "Learn FastAPI"
    assert data["completed"] is False
    assert "id" in data


def test_get_tasks(client):
    client.post(
        "/tasks",
        json={"title": "Learn SQLAlchemy"}
    )

    response = client.get("/tasks")

    assert response.status_code == 200

    data = response.json()

    assert len(data) == 1
    assert data[0]["title"] == "Learn SQLAlchemy"


def test_get_task(client):
    create_response = client.post(
        "/tasks",
        json={"title": "Learn PostgreSQL"}
    )

    task_id = create_response.json()["id"]

    response = client.get(f"/tasks/{task_id}")

    assert response.status_code == 200
    assert response.json()["title"] == "Learn PostgreSQL"


def test_update_task(client):
    create_response = client.post(
        "/tasks",
        json={"title": "Learn Python"}
    )

    task_id = create_response.json()["id"]

    response = client.put(
        f"/tasks/{task_id}",
        json={
            "title": "Learn Advanced Python",
            "completed": True
        }
    )

    assert response.status_code == 200

    data = response.json()

    assert data["title"] == "Learn Advanced Python"
    assert data["completed"] is True


def test_delete_task(client):
    create_response = client.post(
        "/tasks",
        json={"title": "Temporary task"}
    )

    task_id = create_response.json()["id"]

    response = client.delete(f"/tasks/{task_id}")

    assert response.status_code == 200

    get_response = client.get(f"/tasks/{task_id}")

    assert get_response.status_code == 404


def test_get_task_not_found(client):
    response = client.get("/tasks/999999")

    assert response.status_code == 404
    assert response.json() == {"detail": "Task not found"}


def test_login_wrong_password(client):
    response = client.post(
        "/login",
        json={
            "username": "testuser",
            "password": "wrongpassword"
        }
    )

    assert response.status_code == 401


def test_login_unknown_user(client):
    response = client.post(
        "/login",
        json={
            "username": "unknownuser",
            "password": "testpassword"
        }
    )

    assert response.status_code == 401


def test_tasks_without_token():
    from fastapi.testclient import TestClient
    from app.main import app

    with TestClient(app) as test_client:
        response = test_client.get("/tasks")

    assert response.status_code == 401


def test_user_cannot_access_other_users_task(client, second_client):
    response = client.post(
        "/tasks",
        json={"title": "Private task"},
    )

    task_id = response.json()["id"]

    response = second_client.get(f"/tasks/{task_id}")

    assert response.status_code == 404


def test_user_cannot_update_other_users_task(client, second_client):
    response = client.post(
        "/tasks",
        json={"title": "Private task"},
    )

    task_id = response.json()["id"]

    response = second_client.put(
        f"/tasks/{task_id}",
        json={"title": "Hacked task"},
    )

    assert response.status_code == 404


def test_user_cannot_delete_other_users_task(client, second_client):
    response = client.post(
        "/tasks",
        json={"title": "Private task"},
    )

    task_id = response.json()["id"]

    response = second_client.delete(
        f"/tasks/{task_id}"
    )

    assert response.status_code == 404


def test_create_user(client):
    response = client.post(
        "/users",
        json={
            "username": "newuser",
            "password": "newpassword"
        }
    )

    assert response.status_code == 200

    data = response.json()

    assert data["username"] == "newuser"
    assert "id" in data
    assert "password" not in data

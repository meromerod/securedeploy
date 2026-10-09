from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)


def test_root():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json()["message"] == "SecureDeploy API is running"



import pytest
from fastapi.testclient import TestClient
from app.main import app


@pytest.fixture
def client():
    # Entering this context runs FastAPI's startup/lifespan code.
    with TestClient(app) as test_client:
        yield test_client


def test_root(client):
    response = client.get("/")
    assert response.status_code == 200
    assert response.json()["message"] == "SecureDeploy API is running"


def test_health(client):
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json()["status"] == "healthy"


def test_create_task(client):
    response = client.post(
        "/tasks",
        json={"title": "Learn Docker"},
    )
    assert response.status_code == 201
    assert response.json()["title"] == "Learn Docker"
    assert response.json()["completed"] is False


def test_get_tasks(client):
    response = client.get("/tasks")
    assert response.status_code == 200
    assert isinstance(response.json(), list)


def test_delete_missing_task(client):
    response = client.delete("/tasks/999999")
    assert response.status_code == 404

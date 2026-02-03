from fastapi.testclient import TestClient

from app.main import app

client = TestClient(app)


def test_example_get():
    response = client.get("/api/v1/example/upper", params={"text": "hello"})
    assert response.status_code == 200
    assert response.json()["upper"] == "HELLO"


def test_example_post():
    response = client.post("/api/v1/example/upper", json={"text": "hello"})
    assert response.status_code == 200
    assert response.json()["upper"] == "HELLO"

import pytest
from app.app import create_app
def test_health_check(client):
    response = client.get("/")
    assert response.status_code == 200

def test_get_tasks(client):
    response = client.get("/tasks")
    assert response.status_code == 200
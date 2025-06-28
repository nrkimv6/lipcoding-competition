import pytest
from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_read_root():
    response = client.get("/")
    assert response.status_code == 200
    assert "message" in response.json()

def test_health_check():
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json()["status"] == "healthy"

def test_get_mentors():
    response = client.get("/api/v1/mentors")
    assert response.status_code == 200
    assert "mentors" in response.json()

def test_get_mentees():
    response = client.get("/api/v1/mentees")
    assert response.status_code == 200
    assert "mentees" in response.json()

from fastapi import FastAPI
from fastapi.testclient import TestClient

app = FastAPI()
client = TestClient(app)

def test_get_blogs():
    response = client.get('/get_blogs')
    assert response.status_code == 200

def test_add():
    response = client.get('/add')
    assert response.status_code == 200

def test_delete():
    response = client.get('/delete')
    assert response.status_code == 200


def test_update():
    response = client.get('/update')
    assert response.status_code == 200

def test_user_add():
    response = client.get('/user_add')
    assert response.status_code == 200

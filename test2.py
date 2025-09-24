import pytest
import pytest_check as check
from app import app

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_404(client):
    response = client.get('/nonexistent')
    assert response.status_code == 404

def test_app_is_working(client):
    response = client.get('/')
    check.equal(response.status_code, 200)
    check.is_in(b"Hello World!", response.data)

def test_submit_route_without_name(client):
    response = client.post('/submit')
    assert response.status_code == 200
    assert b"Thanks, Guest" in response.data

def test_submit_json_response(client):
    response = client.post('/submit', json={'name': 'Alice'})
    assert response.status_code == 200
    assert response.is_json
    assert response.get_json() == {"message": "Thanks, Alice"}
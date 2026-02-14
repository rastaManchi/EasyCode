import pytest
from httpx import Client, WSGITransport
from app import app


@pytest.fixture
def client():
    transport = WSGITransport(app=app)
    with Client(transport=transport, base_url="http://test") as ac:
        yield ac
        
    
def test_test(client):
    result = 2 + 2
    assert result == 4.0
    

def test_home(client):
    response = client.get('/')
    assert response.status_code == 200
    

def test_profile(client):
    response = client.get('/profile/')
    assert 'Вы не авторизованы' in str(response.content, encoding='utf-8')

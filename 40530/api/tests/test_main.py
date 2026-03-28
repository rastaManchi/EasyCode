import pytest
import sys
import sqlite3
import tempfile
import os


import db as db_module
from app import app as flask_app


@pytest.fixture
def client():
    with flask_app.test_client() as client:
        yield client
    
    
def test_home_unauth(client):
    response = client.get('/api/home')
    assert response.status_code == 401
    
def test_home_auth(client):
    response = client.get('/api/home', headers={"Authorization": "SADJFGSKLVSDKKFGCASZXKC"})
    assert response.status_code == 200
    
    
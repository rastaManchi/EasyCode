import os
import sys


absolute_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
sys.path.insert(0, absolute_path)

import db as db_module
from app import app as flask_app
import sqlite3
import pytest
import tempfile


@pytest.fixture
def client():
    original_conn = db_module.conn
    original_cur = db_module.cur
    
    db_fd, db_path = tempfile.mkstemp()
    test_conn = sqlite3.connect(db_path, check_same_thread=False)
    test_cur = test_conn.cursor()
    
    test_cur.executescript('''
            CREATE TABLE IF NOT EXISTS users(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT,
            email TEXT,
            password TEXT,
            isadmin INTEGER DEFAULT 0);
            
            CREATE TABLE IF NOT EXISTS posts(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT,
            content TEXT,
            user_id INTEGER,
            status INTEGER DEFAULT 0,
            FOREIGN KEY(user_id) REFERENCES users(id));
            
            CREATE TABLE IF NOT EXISTS auth_tokens(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            token TEXT,
            user_id INTEGER,
            expires_at TIMESTAMP,
            FOREIGN KEY(user_id) REFERENCES users(id));
            
            CREATE TABLE IF NOT EXISTS api_tokens(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            token TEXT,
            user_id INTEGER,
            expires_at TIMESTAMP,
            requests_count INTEGER DEFAULT 0,
            FOREIGN KEY(user_id) REFERENCES users(id));                       
    ''')
    
    db_module.conn = test_conn
    db_module.cur = test_cur
    
    db_module.add_user('TestAdmin', 'testAdmin@testAdmin', 'qwerty')
    db_module.set_isadmin(1, 1)
    
    db_module.add_user('TestUser', 'test@test', 'qwerty')
    
    test_conn.commit()
    
    with flask_app.test_client() as client:
        yield client
        
    db_module.conn = original_conn
    db_module.cur = original_cur
    test_conn.close()
    os.close(db_fd)
    os.unlink(db_path)
    

def test_get_unauth_posts(client):
    response = client.get('/api/posts')
    assert response.status_code == 401
    
    
def test_get_auth_posts(client):
    response = client.post('/api/login', json={
        "email": "test@test",
        "password": "qwerty"
    })
    token = response.get_json().get('token')
    response = client.get('/api/posts', headers={
        'Authorization': token
    })
    assert response.status_code == 200
    
    
def test_login(client):
    response = client.post('/api/login')
    assert response.status_code == 500
    response = client.post('/api/login', json={
        "email": "test",
        "password": "test"
    })
    assert response.status_code == 401
    response = client.post('/api/login', json={
        "email": "test@test",
        "password": "qwerty"
    })
    assert response.status_code == 200

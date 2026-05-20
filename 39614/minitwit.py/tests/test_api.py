import pytest
import tempfile
import os, sys

import sqlite3


from app import app as FlaskApp
import help as db_module


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
                    is_admin INTEGER DEFAULT 0
                );
                
                CREATE TABLE IF NOT EXISTS posts(
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    title TEXT,
                    content TEXT,
                    user_id INTEGER,
                    status INTEGER DEFAULT 0,
                    FOREIGN KEY (user_id) REFERENCES users(id)
                );
                
                CREATE TABLE IF NOT EXISTS auth_tokens(
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    token TEXT,
                    user_id INTEGER,
                    expires_at TIMESTAMP,
                    FOREIGN KEY (user_id) REFERENCES users(id)
                );
                
                CREATE TABLE IF NOT EXISTS api_tokens(
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    token TEXT,
                    user_id INTEGER,
                    expires_at TIMESTAMP,
                    requests INTEGER DEFAULT 0,
                    FOREIGN KEY (user_id) REFERENCES users(id)
                );
                           ''')
    test_conn.commit()
    
    db_module.conn = test_conn
    db_module.cur = test_cur
    
    db_module.add_user('Test', 'test@test', 'qwerty')
    
    with FlaskApp.test_client() as client:
        yield client
        
    db_module.conn = original_conn
    db_module.cur = original_cur
    test_conn.close()
    os.close(db_fd)
    os.unlink(db_path)
    
    
def test_get_posts(client):
    response = client.get('/api/v1/posts')
    assert response.status_code == 401
    
    
def test_auth_get_posts(client):
    token = client.post('/api/v1/login', json={
        'email': 'test@test',
        'password':'qwerty'
    }).get_json().get('token')
    auth_retry = client.get('/api/v1/posts', headers={
        'Authorization': token
    })
    assert auth_retry.status_code == 200

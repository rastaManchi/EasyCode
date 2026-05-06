import sys
import os
import pytest
import tempfile
import sqlite3


from app_dir.app import app as FlaskApp
import app_dir.db as db_module


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
        
        CREATE TABLE IF NOT EXISTS notifications(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            user_id INTEGER,
            action TEXT,
            details TEXT,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            FOREIGN KEY (user_id) REFERENCES users(id)
        );
        
        CREATE TABLE IF NOT EXISTS auth_tokens(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            user_id INTEGER,
            token TEXT,
            expires_at TIMESTAMP,
            FOREIGN KEY (user_id) REFERENCES users(id)
        );
        
        CREATE TABLE IF NOT EXISTS api_tokens(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            token TEXT,
            requests_count INTEGER DEFAULT 0,
            expires_at TIMESTAMP,
            owner INTEGER,
            FOREIGN KEY (owner) REFERENCES users(id)
        );
                           ''')
    test_conn.commit()
    
    db_module.add_user('Test', 'test2@test2', 'qwerty')
    
    with FlaskApp.test_client() as client:
        yield client
        
    db_module.conn = original_conn
    db_module.cur = original_cur
    test_conn.close()
    os.close(db_fd)
    os.unlink(db_path)
    
    
def test_api_unauth_posts(client):
    resposne = client.get('/api/posts')
    json_data = resposne.get_json()
    assert resposne.status_code == 401
    assert json_data['msg'] == 'Не указан Authorization'
    
    
def test_api_auth_posts(client):
    response = client.post('/api/login', json={
        "email": "test2@test2",
        "password": "qwerty"
        })
    token = response.get_json()['auth_token']
    r = client.get('/api/posts', headers={
        'Authorization': token
    })
    print(r.get_json())
    assert r.status_code == 200
    
    
def test_api_login(client):
    response = client.post('/api/login', json={
        "email": "test2@test2",
        "password": "qwerty"
        })
    assert response.status_code == 200
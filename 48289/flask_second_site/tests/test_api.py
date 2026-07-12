import pytest
import tempfile
import sqlite3
import os

from app import app as flask_app
import db as app_module

@pytest.fixture
def client():
    original_conn = app_module.conn
    original_cur = app_module.cur
    
    
    db_fd, db_path = tempfile.mkstemp()
    test_conn = sqlite3.connect(db_path, check_same_thread=False)
    test_cur = test_conn.cursor()
    
    test_cur.executescript('''
        CREATE TABLE IF NOT EXISTS users(
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT,
                email TEXT,
                password TEXT
        );
        CREATE TABLE IF NOT EXISTS posts(
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                title TEXT,
                content TEXT,
                author INTEGER,
                FOREIGN KEY (author) REFERENCES users(id)
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
                FOREIGN KEY (user_id) REFERENCES users(id)
        )''')
    test_conn.commit()
    
    app_module.conn = test_conn
    app_module.cur = test_cur
    
    app_module.create_user('test', 'test@test', 'test')
    
    with flask_app.test_client() as client:
        yield client
    
    app_module.conn = original_conn
    app_module.cur = original_cur
    test_conn.close()
    os.close(db_fd)
    os.unlink(db_path)
    
def test_api_users_unauth(client):
    response = client.get('/api/users')
    assert response.status_code == 401
    assert response.get_json()['msg'] == 'Токен не указан'
    
def test_api_login(client):
    empty_response = client.post('/api/login')
    assert empty_response.status_code == 415
    response = client.post('/api/login', json={
        'login': 'test@test',
        'password': 'test'
    })
    assert response.status_code == 200
    assert response.get_json().get('token')
    
    

    
    
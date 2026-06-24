# tests/test_api.py
import sys
import os
import pytest
import tempfile
import sqlite3
from werkzeug.security import generate_password_hash

# Добавляем путь к родительской папке, чтобы импортировать app.py
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import app as app_module          # сам модуль (нужен для подмены глобальных переменных)
from app import app as flask_app  # экземпляр Flask (нужен для тестового клиента)

@pytest.fixture
def client():
    """Создаёт тестовый клиент с временной базой данных."""
    # Сохраняем оригинальные глобальные переменные модуля app
    original_conn = app_module.conn
    original_cur = app_module.cur

    # Создаём временный файл базы данных
    db_fd, db_path = tempfile.mkstemp()
    test_conn = sqlite3.connect(db_path, check_same_thread=False)
    test_cur = test_conn.cursor()

    # Создаём таблицы (такая же структура, как в app.py)
    test_cur.executescript('''
        CREATE TABLE users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT,
            email TEXT,
            password TEXT,
            last_login TIMESTAMP,
            role TEXT DEFAULT 'user'
        );
        CREATE TABLE categories (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT UNIQUE NOT NULL,
            description TEXT
        );
        CREATE TABLE posts (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT,
            content TEXT,
            user_id INTEGER,
            category_id INTEGER,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            FOREIGN KEY (user_id) REFERENCES users(id),
            FOREIGN KEY (category_id) REFERENCES categories(id)
        );
        CREATE TABLE notifications (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            user_id INTEGER,
            action TEXT,
            details TEXT,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            FOREIGN KEY (user_id) REFERENCES users(id)
        );
        CREATE TABLE auth_tokens (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            user_id INTEGER,
            token TEXT UNIQUE,
            expires_at TIMESTAMP,
            FOREIGN KEY (user_id) REFERENCES users(id)
        );
    ''')

    # Добавляем тестового пользователя (пароль хеширован)
    hashed = generate_password_hash('password123')
    test_cur.execute(
        'INSERT INTO users (name, email, password, role) VALUES (?, ?, ?, ?)',
        ('Test User', 'test@example.com', hashed, 'user')
    )
    # Добавляем тестовую категорию
    test_cur.execute(
        'INSERT INTO categories (name, description) VALUES (?, ?)',
        ('Тестовая категория', 'Описание')
    )
    test_conn.commit()

    # Подменяем глобальные переменные модуля app на тестовые
    app_module.conn = test_conn
    app_module.cur = test_cur

    # Создаём тестовый клиент Flask
    with flask_app.test_client() as client:
        yield client

    # Возвращаем оригинальные соединения и удаляем временный файл
    app_module.conn = original_conn
    app_module.cur = original_cur
    test_conn.close()
    os.close(db_fd)
    os.unlink(db_path)

# ------------------------------------------------------------
# Тесты
# ------------------------------------------------------------
def test_get_posts(client):
    """Проверяет получение списка постов."""
    response = client.get('/api/v1/posts')
    assert response.status_code == 200
    json_data = response.get_json()
    assert json_data['success'] is True
    assert 'data' in json_data

def test_get_single_post_not_found(client):
    """Проверяет обработку несуществующего поста."""
    response = client.get('/api/v1/posts/999')
    assert response.status_code == 404
    json_data = response.get_json()
    assert json_data['success'] is False

def test_login_success(client):
    """Проверяет успешный вход и получение токена."""
    response = client.post('/api/v1/login', json={
        'email': 'test@example.com',
        'password': 'password123'
    })
    assert response.status_code == 200
    json_data = response.get_json()
    assert json_data['success'] is True
    assert 'token' in json_data['data']

def test_login_wrong_password(client):
    """Проверяет вход с неверным паролем."""
    response = client.post('/api/v1/login', json={
        'email': 'test@example.com',
        'password': 'wrong'
    })
    assert response.status_code == 401
    json_data = response.get_json()
    assert json_data['success'] is False
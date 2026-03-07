import secrets
from datetime import datetime, timedelta


def create_auth_token(user_id, remember=False):
    """Создание токена аутентификации"""
    token = secrets.token_urlsafe(32)
    expires = datetime.now() + timedelta(days=30 if remember else 1)
    # Здесь нужно сохранить токен в БД
    return token


print(create_auth_token(1))
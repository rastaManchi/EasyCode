import os
from dotenv import load_dotenv
import smtplib
load_dotenv()

from_email = os.getenv("EMAIL_USER")
password = os.getenv("EMAIL_PASSWORD")

if not from_email or not password:
    print("ОШИБКА: Не найдены EMAIL_USER или EMAIL_PASSWORD в .env файле!")
    exit()
try:
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login(from_email, password)
    print("Успешный вход в SMTP сервер Gmail!")
    server.quit()
except smtplib.SMTPAuthenticationError:
    print("Ошибка аутентификации - неверный логин или пароль")
except Exception as e:
    print(f"Ошибка подключения: {e}")
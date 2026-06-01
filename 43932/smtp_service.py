from dotenv import load_dotenv
load_dotenv()
import os
import smtplib


EMAIL_LOGIN = os.getenv('EMAIL_LOGIN')
EMAIL_PASSWORD = os.getenv('EMAIL_PASSWORD')


def test():
    if not EMAIL_LOGIN or not EMAIL_PASSWORD:
        print("ОШИБКА: Не найдены EMAIL_USER или EMAIL_PASSWORD в .env файле!")
        exit()
    try:
        server = smtplib.SMTP('smtp.mail.ru', 587)
        server.starttls()
        server.login(EMAIL_LOGIN, EMAIL_PASSWORD)
        print("Успешный вход в SMTP сервер Mail!")
        server.quit()
    except smtplib.SMTPAuthenticationError:
        print("Ошибка аутентификации - неверный логин или пароль")
    except Exception as e:
        print(f"Ошибка подключения: {e}")
        
test()

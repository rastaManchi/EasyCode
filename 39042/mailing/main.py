import smtplib  # Импортируем библиотеку по работе с SMTP

# Дополнительные модули
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage

from_email = "" # Почта, для которой ставились галочки. Письма будут отправляться с этого адреса
to_email = "bulatzakirrov@yandex.ru" # Почта, на которую отправляем письмо
email_password = ""  # Пароль, который создали и скопировали в 4 пункте инструкции

message = MIMEMultipart('alternative')  # Создаем объект сообщения. Alternative - режим форматирования (потом будем добавлять HTML)
message['From'] = from_email
message['To'] = to_email
message['Subject'] = 'Тема сообщения'  # Тема сообщения


# Подразумеваем, что картинка находится на том же уровне вложенности, что и этот скрипт
# Флаг rb означает, что картинка открыается в бинарном формате
fp = open('dfgdfgdfd/test.webp', 'rb')
msgImage = MIMEImage(fp.read()) # Создаём объект картинки, который поймёт письмо
fp.close()
# Соотносим id объекта с названием, которое сможем использовать в коде
# Content-ID - обязательный ключ. В значении <image1> обязательны только алмазные скобки
msgImage.add_header('Content-ID', '<image>')
# Прикрепляем объект изображения к объекту письма
message.attach(msgImage)

text = "Текст сообщения"
html_text = '''
<html>
<head>
    <style>
        @import url('https://fonts.googleapis.com/css2?family=Manrope&display=swap');
        body {
            margin: 0;
            padding: 0;
            font-family: 'Manrope', sans-serif;
        }
        button {
            background: rgb(0, 166, 255);
            color: white;
            padding: 32px 16px;
            font-family: 'Manrope', sans-serif;
            border: none;
            outline: none;
            border-radius: 7px;
            box-sizing: border-box;
            display: block;
        }
    </style>
</head>
<body>
    <h1>Заголовок</h1>
    <p>Абзац</p>
    <img src="cid:image" width="300">
    <button>И даже кнопку можно!</button>
</body>
</html>
'''

message.attach(MIMEText(text, 'plain'))  # Добавляем в сообщение текст
message.attach(MIMEText(html_text, 'html'))  # Добавляем в сообщение html-версию письма

server = smtplib.SMTP_SSL('smtp.yandex.ru', 465)  # Создаем объект SMTP
# Получаем доступ к серверу - грубо говоря, авторизуемся с помощью почты и пароля, как обычно
server.login(from_email, email_password) 
server.send_message(message)  # Отправляем сообщение
server.quit()
import smtplib  # Импортируем библиотеку по работе с SMTP

# Дополнительные модули
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage

def check_email(email, msg):
    from_email = "bulatzakirrov@yandex.ru" # Почта, для которой ставились галочки. Письма будут отправляться с этого адреса
    to_email = email # Почта, на которую отправляем письмо
    email_password = "okssbsjlswdjicht"  # Пароль, который создали и скопировали в 4 пункте инструкции

    message = MIMEMultipart('alternative')  # Создаем объект сообщения. Alternative - режим форматирования (потом будем добавлять HTML)
    message['From'] = from_email
    message['To'] = to_email
    message['Subject'] = 'Тема сообщения'  # Тема сообщения

    text = msg

    fp = open('2.png', 'rb')
    msgImage = MIMEImage(fp.read())
    fp.close()

    msgImage.add_header('Content-ID', '<image>')
    message.attach(msgImage)

    html_text = '''
    <html>
        <head>
            <style>
                body {
                    color: red;
                }
            </style>
        </head>
        <body>
            <h1>Текст сообщения</h1>
            <img src="cid:image" width="300">
        </body>
    </html>
    '''


    message.attach(MIMEText(text, 'plain'))  # Добавляем в сообщение текст
    # message.attach(MIMEText(html_text, 'html'))

    server = smtplib.SMTP_SSL('smtp.yandex.ru', 465)  # Создаем объект SMTP
    server.login(from_email, email_password) # Получаем доступ к серверу (грубо говоря, авторизуемся с помощью почты и пароля, как обычно)
    server.send_message(message)  # Отправляем сообщение
    server.quit()
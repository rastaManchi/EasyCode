import smtplib


server = smtplib.SMTP('smtp.mail.ru', 587)
server.starttls()
server.login('bulat-zakirov.01@mail.ru', 'QZ9Hwnx2aKsKF5xjPaza')


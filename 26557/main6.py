import requests, json
from bs4 import BeautifulSoup as bs


headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/140.0.0.0 YaBrowser/25.10.0.0 Safari/537.36"
}

r = requests.get('https://www.gismeteo.ru/weather-kazan-4364/month/', headers=headers)
data = bs(r.content, 'lxml')
items = data.findAll(class_='row-item-month-date')
for item in items:
    desc = item.get('data-tooltip')
    temps = item.findAll('temperature-value')
    min = temps[1].get('value')
    max = temps[0].get('value')
    print(f'Описание: {desc}\nМин: {min}\nМакс: {max}\n')
    print('-'*20)
    
    
# GET: https://vk.ru/friends?search="Максим"
# POST: https://vk.ru/login/
        # -b {'username': '123', 'pass': 'qwerty'} 
# DELETE PUT UPDATE

# websockets
# ws:// wss://
# ws://vk.ru/dfgkdhbsfldfghb
# CONNECTING 
# HANDSHAKING
# Двусторонняя связь
# DISCONNECT
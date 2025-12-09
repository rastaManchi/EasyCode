import requests
from bs4 import BeautifulSoup as bs

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:145.0) Gecko/20100101 Firefox/145.0'
}
r = requests.get('https://www.gismeteo.ru/weather-kazan-4364/month/', headers=headers)
data = bs( r.content, 'lxml')
spisok = data.findAll('div', class_='temp')
for item in spisok:
    maxt, mint = item.findAll('temperature-value')
    print(maxt.get('value'), mint.get('value'))
    print('_'*20)
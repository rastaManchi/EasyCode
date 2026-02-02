import requests
import json


#http://api.openweathermap.org/geo/1.0/direct?q={city name},{state code},{country code}&limit={limit}&appid={API key}
#https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={API key}


city = input('Введите город: ')
API_KEY = "3140cf48db6a89dd9eb2dc1338ae400d"
r = requests.get(f"http://api.openweathermap.org/geo/1.0/direct?q={city}&appid={API_KEY}")
data = json.loads(r.content)
lat = data[0]['lat']
lon = data[0]['lon']


r = requests.get(f"https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={API_KEY}")
data = json.loads(r.content)
temp = data['main']['temp'] - 273

print(f"Температура: {round(temp)}")


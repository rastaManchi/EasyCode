import requests
import json


city = input('Из какого вы города: ')
limit = 1
API_key = '3140cf48db6a89dd9eb2dc1338ae400d'
r = requests.get(f"http://api.openweathermap.org/geo/1.0/direct?q={city}&limit={limit}&appid={API_key}")
data = json.loads(r.content)[0]
lat = data['lat']
lon = data['lon']
print(lat, lon)

r = requests.get(f"https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={API_key}")
data = json.loads(r.content)
print(data)
import requests
import json


def get_weather(city):
    r = requests.get(f"http://api.openweathermap.org/geo/1.0/direct?q={city}&limit=1&appid=3140cf48db6a89dd9eb2dc1338ae400d")
    data = json.loads(r.content)[0]
    lat, lon = data['lat'], data['lon']
    print(lat, lon)

    r = requests.get(f"https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid=3140cf48db6a89dd9eb2dc1338ae400d")
    data = json.loads(r.content)
    weather = data['weather'][0]['main']
    temp = data['main']['temp'] - 273
    feels_temp = data['main']['feels_like'] - 273
    wind_speed = data['wind']['speed']

    return f"Погода: {weather}\nТемп: {temp}\nОщущ: {feels_temp}\nВетер: {wind_speed}"
    

print(get_weather("Казань"))

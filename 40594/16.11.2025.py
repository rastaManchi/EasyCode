import requests, json

weather_API = '3140cf48db6a89dd9eb2dc1338ae400d'


# f"https://api.openweathermap.org/data/2.5/forecast/daily?lat={lat}&lon={lon}&cnt=5&appid={weather_API}"
# f"http://api.openweathermap.org/geo/1.0/direct?q={city}&limit=1&appid={weather_API}"


def find_locate(city):
    r = requests.get(f"http://api.openweathermap.org/geo/1.0/direct?q={city}&limit=1&appid={weather_API}")
    data = json.loads(r.content)
    print(data)
    lat = data[0]['lat']
    lon = data[0]['lon']
    return lat, lon


def get_weather(lat, lon):
    ddfkbfgdikbg = requests.get(f"https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&cnt=5&appid={weather_API}")
    data = json.loads(ddfkbfgdikbg.content)
    print(data)


lat, lon = find_locate('Серноводск')
get_weather(lat, lon)
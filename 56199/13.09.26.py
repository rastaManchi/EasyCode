import requests

def get_lat_lon():
    city = input("Введите название города: ")
    result = requests.get(f"http://api.openweathermap.org/geo/1.0/direct?q={city}&limit=1&appid=<Ваш API Key>")
    data = result.json()[0]
    lat, lon = data.get('lat'), data.get('lon')
    return lat, lon

lat, lon = get_lat_lon()

def get_weather():
    result = requests.get(f"https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid=<Ваш API Key>")
    data = result.json()
    temp = data['main']['temp'] - 273
    print(temp)



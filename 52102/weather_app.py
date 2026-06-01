import tkinter as tk
import requests


def get_wearther_from_openweather(city):
    r = requests.get(f"http://api.openweathermap.org/geo/1.0/direct?q={city}&appid=3140cf48db6a89dd9eb2dc1338ae400d")
    data = r.json()
    lat = data[0]['lat']
    lon = data[0]['lon']
    r = requests.get(f"https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid=3140cf48db6a89dd9eb2dc1338ae400d")
    data = r.json()
    main = data['main']
    temp = round(main['temp'] - 273, 2)
    feels_like = round(main['feels_like'] - 273, 2)
    return f"\ntemp: {temp}\nfeels_like: {feels_like}"


def get_weather():
    city = city_entry.get()
    result_text = get_wearther_from_openweather(city)
    result.set(f"Погода в {city}: {result_text}")


root = tk.Tk()
root.title('Погода')

head_title = tk.Label(text='Введите название города')
head_title.pack(pady=10)

city_entry = tk.Entry()
city_entry.pack(pady=10)


btn = tk.Button(text='Узнать погоду', command=get_weather)
btn.pack(pady=10)


result = tk.StringVar()
result_text = tk.Label(textvariable=result, font='Arial 18')
result_text.pack(pady=10)


root.mainloop()

import tkinter as tk
import requests

root = tk.Tk()
root.title("Погодное приложение")

tk.Label(text="Введите название города:").pack()

city_entry= tk.Entry()
city_entry.pack()

def get_weather():
    city= city_entry.get()
    
    result = requests.get(f"https://geocoding-api.open-meteo.com/v1/search?name={city}&count=1&language=ru&format=json")
    data = result.json().get("results")[0]
    lat, lon = data.get('latitude'), data.get('longitude')

    weather = requests.get(f"https://api.open-meteo.com/v1/forecast?latitude={lat}&longitude={lon}&current=temperature_2m,wind_speed_10m&hourly=temperature_2m,relative_humidity_2m,wind_speed_10m")
    weather_data = weather.json().get("current")
    temp = weather_data.get("temperature_2m")
    resalt_text.set(f"температура: {temp}")

button = tk.Button(text = "Получить погоду", command=get_weather)
button.pack()

resalt_text= tk.StringVar()
result_label= tk.Label(textvariable= resalt_text)
result_label.pack()

root.mainloop()
import tkinter as tk
from tkinter import *
import requests
import time


def KtoF(K):
    F = (K - 273.15) * (9/5) + 32
    return str(round(F, 1))

def getWeather(canvas):
    city = textfield.get()
    api = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid=6d312dc441a47f4477d4556c96acc886"
    json_data = requests.get(api).json()
    condition = json_data["weather"][0]["main"]
    tempCurrent = KtoF(json_data["main"]["temp"])
    tempMin = KtoF(json_data["main"]["temp_min"])
    tempMax = KtoF(json_data["main"]["temp_max"])
    def timeConvert(time_of_day):
        return time.strftime("%H:%M:%S", time.gmtime(json_data["sys"][time_of_day] - 21600))
    sunrise = timeConvert("sunrise")
    sunset = timeConvert("sunset")

    temp_info = f"{condition}\nTemperature: {tempCurrent}ºF\nLow: {tempMin} High: {tempMax}"
    time_info = f"\nSunrise: {sunrise}\nSunset: {sunset}"

    loc.configure(text=temp_info, font = ("Modern", 25, "bold"))
    temp.configure(text=time_info, font = ("Modern", 30))

canvas = tk.Tk()
canvas.geometry("800x600")
canvas.title("Weather App")
inputlbl = tk.Label(canvas, text="Enter a City Below:").pack()


# TEXT INPUT
textfield = tk.Entry(canvas, font=("Helvetica", 25))
textfield.pack()
textfield.focus()
textfield.bind('<Return>', getWeather)

loc = tk.Label(canvas)
loc.pack()

temp = tk.Label(canvas)
temp.pack()


canvas.mainloop()

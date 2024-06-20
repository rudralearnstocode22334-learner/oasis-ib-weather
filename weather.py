from tkinter import *
from tkinter import messagebox
import requests
import datetime


APIk= open('api_key.txt', 'r').read()

def get_weather(city, unit):
    url = "https://api.openweathermap.org/data/2.5/weather?"
    prms = {
        'q': city,
        'appid': APIk,
        'units': unit
    }
    response = requests.get(url, params=prms)
    return response.json()

def save_weather():
    city = city_entry.get()
    if not city:
        messagebox.showerror("Error", "Please enter a city name")
        return
    
    if unit_var.get() == 'Celsius':
        unit = 'metric'
    else:
        unit = 'imperial'

    weather_data = get_weather(city, unit)
    with open("weather_data.txt", "a") as f:
        f.write(f"City: {weather_data['name']}, Country: {weather_data['sys']['country']}, Temprature: {weather_data['main']['temp']}, Humidity: {weather_data['main']['humidity']}, Weather Description: {weather_data['weather'][0]['description']}, Wind Speed: {weather_data['wind']['speed']}, At time: {datetime.datetime.now()}\n")

def show_save_btn():
    save_btn.grid(row=0, column=1, sticky="e", pady=10)

        
def update_weather():
    city = city_entry.get()
    if not city:
        messagebox.showerror("Error", "Please enter a city name")
        return
    
    if unit_var.get() == 'Celsius':
        unit = 'metric'
    else:
        unit = 'imperial'

    
    try:
        weather_data = get_weather(city, unit)
        if weather_data.get('cod') != 200:
            messagebox.showerror("Error", weather_data.get('message', 'Invalid City Name'))
            return

        city_name = weather_data['name']
        country = weather_data['sys']['country']
        temperature = weather_data['main']['temp']
        humidity = weather_data['main']['humidity']
        weather_desc = weather_data['weather'][0]['description']
        wind_speed = weather_data['wind']['speed']

        city_label.config(text=f"{city_name}, {country}")
        city_label.pack(pady=10, fill=X)
        temp_label.config(text=f"Temperature: {temperature}°{unit_var.get()[0]}")
        temp_label.pack(pady=5, fill=X)
        humidity_label.config(text=f"Humidity: {humidity}%")
        humidity_label.pack(pady=5, fill=X)
        weather_label.config(text=f"Weather: {weather_desc}")
        weather_label.pack(pady=5, fill=X)
        wind_label.config(text=f"Wind Speed: {wind_speed} m/s")
        wind_label.pack(fill=X, pady=10)

        show_save_btn()

    except Exception as e:
        messagebox.showerror("Error", str(e))


root = Tk()
root.title("Weather App")
root.geometry("400x550")
root.configure(bg="#FED8B1")


f_upper=Frame(root,bg="#ECB176")
Label(text=" Weather App", font="Poppins 20 bold", bg="#ECB176", fg="#6F4E37", pady=5).pack(fill=X)
f_upper.pack()

Label(text="Enter the City Name and Get Weather",bg="#FED8B1",font="Poppins 12", fg="#6F4E37", pady=10 ).pack(fill=X)


frm_1=Frame(root,bg="#FED8B1")

Label(frm_1, text="Enter City:", font="Poppins 12 bold", bg="#FED8B1", fg="#6F4E37").grid(row=0, column=0, pady=10, padx=5)
city_entry = Entry(frm_1, font="Poppins 11 bold", bg="#A67B5B", fg="white")
city_entry.grid(row=0, column=1,pady=5, padx=5)

frm_1.pack()


unit_var = StringVar(value="Celsius")

frm_2= Frame(root,bg="#FED8B1")
Radiobutton(frm_2, text="Celsius", variable=unit_var, value="Celsius", font="Poppins 10 ", bg="#FED8B1", fg="#6F4E37").grid(row=0, column=0, padx=10, sticky="w")

Radiobutton(frm_2, text="Fahrenheit", variable=unit_var, value="Fahrenheit", font="Poppins 10", bg="#FED8B1", fg="#6F4E37").grid(row=0, column=1, padx=10, sticky="e")

frm_2.pack()

frm_3=Frame(root,bg="#FED8B1")
fetch_btn = Button(frm_3, text="Get Weather", font="Poppins 12 bold", command=update_weather, bg="#6F4E37", fg="white", padx=5)
fetch_btn.grid(row=0, column=0,pady=10, sticky="w")

save_btn = Button(frm_3, text="Save Weather", font="Poppins 12 bold", command=save_weather, bg="#6F4E37", fg="white", padx=5)

frm_3.pack()

frm_4=Frame(root,bg="#ECB176" )

city_label = Label(frm_4, font="Poppins 14 bold", bg="#6F4E37", fg="#FED8B1")
temp_label = Label(frm_4, font="Poppins 12", bg="#ECB176", fg="#6F4E37")
humidity_label = Label(frm_4, font="Poppins 12", bg="#ECB176", fg="#6F4E37")
weather_label = Label(frm_4, font="Poppins 12", bg="#ECB176", fg="#6F4E37")
wind_label = Label(frm_4, font="Poppins 12", bg="#ECB176", fg="#6F4E37",)

frm_4.pack(pady=10)

root.mainloop()

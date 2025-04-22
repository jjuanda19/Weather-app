import tkinter as tk
from tkinter import ttk
import requests

url= "https://api.openweathermap.org/data/2.5/weather?"
API_key= "your_api_key_here"

def getWeather(city):
    full_url=url+ "q=" + city + "&appid=" + API_key + "&units=metric"
    response= requests.get(full_url)
    data=response.json()

    if data["cod"] != "404":
        main_data=data['main']
        current_teperature= main_data['temp']
        weather= data['weather']
        weather_description=weather[0]['description']
        country= data['sys']['country']
        
        return round(current_teperature),weather_description, country
       
    else:
        return None, None


 

root = tk.Tk()
titltle=root.title('Weather app')
back_ground= root.configure(background="light blue")

window_width =800 
window_height= 600

screen_width= root.winfo_screenwidth()
screen_height= root.winfo_screenheight()

center_x =int(screen_width/2 - window_height/2)
center_y = int(screen_height/2 - window_height/2)

root.geometry(f'{window_width}x{window_height}+{center_x}+{center_y}')
root.resizable(False,False)

city_label= ttk.Label(root,background='light blue', text='Introduce the city you would like to know the Weather' , font=('Times New Roman', 15))
city_label.place(x=200, y=200)


city_entry = ttk.Entry(root,width=40, font=('Times New Roman', 12))
city_entry.place(x=250, y=250)

def get_entry_value():
    city= city_entry.get()
    temperature, weather_description, country = getWeather(city)
    if temperature is not None:
        
         info_label.config(text=f"The weather in {city}, {country} is {temperature}°C with {weather_description}")
    else:
        
         info_label.config(text="City Not Found")


cheeck_button= ttk.Button(text='Cheeck', width= 20, command= get_entry_value)
cheeck_button.place(x=340, y=290)

info_label= ttk.Label(root,background='light blue', font=('Times New Roman', 15))
info_label.place(x=200, y=400)



root.mainloop()

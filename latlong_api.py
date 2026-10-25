import requests
from tkinter import *
latitude=""
longitude=""
def city_latlong():
    global latitude
    global longitude
    city=E1.get()
    url = f"https://geocoding-api.open-meteo.com/v1/search?name={city}&count=1&language=en&format=json"
    data=requests.get(url).json()
    city=(data['results'][0]['name'])
    latitude=(data['results'][0]['latitude'])
    longitude=(data['results'][0]['longitude'])
    L1=Label(root,text=f"City: {city}\nLatitude: {latitude}\nLongitude: {longitude}",font=("Arial",14,"bold"))
    L1.grid(row=3,column=0,padx=10,pady=10)
    

def display_weather_data():
    # Current Weather
    global latitude
    global longitude
    url = "https://api.open-meteo.com/v1/forecast"
    params = {
        "latitude": {latitude},
        "longitude": {longitude},
        "current": ["temperature_2m", "relative_humidity_2m", "wind_speed_10m"],
        "timezone": "auto",
    }
    weather_data=requests.get(url,params=params).json()
    current_time=(weather_data['current']['time'])
    current_temp=(weather_data['current']['temperature_2m'])
    current_humidity=(weather_data['current']['relative_humidity_2m'])
    wind_speed=(weather_data['current']['wind_speed_10m'])

    L2=Label(root,text=f"Time: {current_time}",font=("Arial",14,"bold"))
    L2.grid(row=5,column=0,padx=10,pady=10)
    L3=Label(root,text=f"Current Temperature: {current_temp}",font=("Arial",14,"bold"))
    L3.grid(row=6,column=0,padx=10,pady=10)
    L4=Label(root,text=f"Current Humidity: {current_humidity}",font=("Arial",14,"bold"))
    L4.grid(row=7,column=0,padx=10,pady=10)
    L5=Label(root,text=f"Current Wind Speed: {wind_speed}",font=("Arial",14,"bold"))
    L5.grid(row=8,column=0,padx=10,pady=10)
    


root=Tk()
root.title("City Latitude and Longitude")

L0=Label(root,text="Enter City Name:")
L0.grid(row=0,column=0,padx=10,pady=10)
E1=Entry(root,font=("Arial",14))
E1.grid(row=1,column=0,padx=10,pady=10)
B1=Button(root,text="Get Latitude and Longitude",command=city_latlong,font=("Arial",10,"bold"),bg="green",fg="white")
B1.grid(row=2,column=0,padx=10,pady=10)
B2=Button(root,text="Display Weather Data",command=display_weather_data,font=("Arial",10,"bold"),bg="blue",fg="white")
B2.grid(row=4,column=0,columnspan=2,padx=10,pady=10)
root.mainloop()
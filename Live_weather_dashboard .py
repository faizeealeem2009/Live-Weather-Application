import requests
from tkinter import *

# 1st City
url = "https://geocoding-api.open-meteo.com/v1/search?name=Malegaon&count=1&language=en&format=json"
data=requests.get(url).json()
city1=data['results'][0]['name']
lat1=data['results'][0]['latitude']
long1=data['results'][0]['longitude']

# 2nd City
url = "https://geocoding-api.open-meteo.com/v1/search?name=Mumbai&count=1&language=en&format=json"
data=requests.get(url).json()
city2=data['results'][0]['name']
lat2=data['results'][0]['latitude']
long2=data['results'][0]['longitude']

# 3rd City
url = "https://geocoding-api.open-meteo.com/v1/search?name=Aurangabad&count=1&language=en&format=json"
data=requests.get(url).json()
city3=data['results'][0]['name']
lat3=data['results'][0]['latitude']
long3=data['results'][0]['longitude']

# 4th City
url = "https://geocoding-api.open-meteo.com/v1/search?name=Nashik&count=1&language=en&format=json"
data=requests.get(url).json()
city4=data['results'][0]['name']
lat4=data['results'][0]['latitude']
long4=data['results'][0]['longitude']

# 5th City
url = "https://geocoding-api.open-meteo.com/v1/search?name=Lucknow&count=1&language=en&format=json"
data=requests.get(url).json()
city5=data['results'][0]['name']
lat5=data['results'][0]['latitude']
long5=data['results'][0]['longitude']


# Current Temperature

# 1st City
url = "https://api.open-meteo.com/v1/forecast"
params = {
    "latitude": lat1,
    "longitude": long1,
    "current": ["temperature_2m", "relative_humidity_2m"],
    "timezone": "auto",
    }
weather_data=requests.get(url,params=params).json()
current_time1=(weather_data['current']['time'])
current_temp1=(weather_data['current']['temperature_2m'])
current_humidity1=(weather_data['current']['relative_humidity_2m'])

# 2nd City
url = "https://api.open-meteo.com/v1/forecast"
params = {
    "latitude": lat2,
    "longitude": long2,
    "current": ["temperature_2m", "relative_humidity_2m"],
    "timezone": "auto",
    }
weather_data=requests.get(url,params=params).json()
current_time2=(weather_data['current']['time'])
current_temp2=(weather_data['current']['temperature_2m'])
current_humidity2=(weather_data['current']['relative_humidity_2m'])

# 3rd City
url = "https://api.open-meteo.com/v1/forecast"
params = {
    "latitude": lat3,
    "longitude": long3,
    "current": ["temperature_2m", "relative_humidity_2m"],
    "timezone": "auto",
    }
weather_data=requests.get(url,params=params).json()
current_time3=(weather_data['current']['time'])
current_temp3=(weather_data['current']['temperature_2m'])
current_humidity3=(weather_data['current']['relative_humidity_2m'])

# 4th City
url = "https://api.open-meteo.com/v1/forecast"
params = {
    "latitude": lat4,
    "longitude": long4,
    "current": ["temperature_2m", "relative_humidity_2m"],
    "timezone": "auto",
    }
weather_data=requests.get(url,params=params).json()
current_time4=(weather_data['current']['time'])
current_temp4=(weather_data['current']['temperature_2m'])
current_humidity4=(weather_data['current']['relative_humidity_2m'])

# 5th City
url = "https://api.open-meteo.com/v1/forecast"
params = {
    "latitude": lat5,
    "longitude": long5,
    "current": ["temperature_2m", "relative_humidity_2m"],
    "timezone": "auto",
    }
weather_data=requests.get(url,params=params).json()
current_time5=(weather_data['current']['time'])
current_temp5=(weather_data['current']['temperature_2m'])
current_humidity5=(weather_data['current']['relative_humidity_2m'])

# Tkinter Window
root=Tk()

root.title("Live Weather Dashboard")

L1=Label(root,text="Live Weather Dashboad",font=("Arial",24,"bold"))
L1.grid(row=0,column=0,columnspan=5,padx=10,pady=10)

L2=Label(root,text=f"City:{city1}\nLatitude: {lat1}\nLongitude: {long1}\nTime: {current_time1}\nTemperature: {current_temp1} °C\nHumidity: {current_humidity1}%",font=("Arial",12,"bold"))
L2.grid(row=1,column=0,padx=10,pady=10)

L3=Label(root,text=f"City:{city2}\nLatitude: {lat2}\nLongitude: {long2}\nTime: {current_time2}\nTemperature: {current_temp2} °C\nHumidity: {current_humidity2}%",font=("Arial",12,"bold"))
L3.grid(row=1,column=1,padx=10,pady=10)

L4=Label(root,text=f"City:{city3}\nLatitude: {lat3}\nLongitude: {long3}\nTime: {current_time3}\nTemperature: {current_temp3} °C\nHumidity: {current_humidity3}%",font=("Arial",12,"bold"))
L4.grid(row=1,column=2,padx=10,pady=10)

L5=Label(root,text=f"City:{city4}\nLatitude: {lat4}\nLongitude: {long4}\nTime: {current_time4}\nTemperature: {current_temp4} °C\nHumidity: {current_humidity4}%",font=("Arial",12,"bold"))
L5.grid(row=1,column=3,padx=10,pady=10)

L6=Label(root,text=f"City:{city5}\nLatitude: {lat5}\nLongitude: {long5}\nTime: {current_time5}\nTemperature: {current_temp5} °C\nHumidity: {current_humidity5}%",font=("Arial",12,"bold"))
L6.grid(row=1,column=4,padx=10,pady=10)

root.mainloop()
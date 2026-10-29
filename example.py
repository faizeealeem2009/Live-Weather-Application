import requests
url = "https://api.open-meteo.com/v1/forecast"
params = {
	"latitude": 20.554750,
	"longitude": 74.510033,
	"daily": "sunrise",
	"hourly": "temperature_2m",
	"current": ["temperature_2m", "relative_humidity_2m", "precipitation", "rain", "showers", "snowfall", "weather_code"],
	"timezone": "Asia/Tokyo",
}

r=requests.get(url,params=params)
x=r.json()
print(x["current"]['time'])
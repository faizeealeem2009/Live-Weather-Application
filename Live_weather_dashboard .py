import csv
import queue
import sqlite3
import threading
from contextlib import closing
from pathlib import Path

from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure
import requests
from tkinter import *

# 1st City
url = "https://geocoding-api.open-meteo.com/v1/search?name=Malegaon&count=1&language=en&format=json"
data=requests.get(url, timeout=20).json()
city1=data['results'][0]['name']
lat1=data['results'][0]['latitude']
long1=data['results'][0]['longitude']

# 2nd City
url = "https://geocoding-api.open-meteo.com/v1/search?name=Mumbai&count=1&language=en&format=json"
data=requests.get(url, timeout=20).json()
city2=data['results'][0]['name']
lat2=data['results'][0]['latitude']
long2=data['results'][0]['longitude']

# 3rd City
url = "https://geocoding-api.open-meteo.com/v1/search?name=Aurangabad&count=1&language=en&format=json"
data=requests.get(url, timeout=20).json()
city3=data['results'][0]['name']
lat3=data['results'][0]['latitude']
long3=data['results'][0]['longitude']

# 4th City
url = "https://geocoding-api.open-meteo.com/v1/search?name=Nashik&count=1&language=en&format=json"
data=requests.get(url, timeout=20).json()
city4=data['results'][0]['name']
lat4=data['results'][0]['latitude']
long4=data['results'][0]['longitude']

# 5th City
url = "https://geocoding-api.open-meteo.com/v1/search?name=Lucknow&count=1&language=en&format=json"
data=requests.get(url, timeout=20).json()
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
weather_data=requests.get(url, params=params, timeout=20).json()
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
weather_data=requests.get(url, params=params, timeout=20).json()
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
weather_data=requests.get(url, params=params, timeout=20).json()
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
weather_data=requests.get(url, params=params, timeout=20).json()
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
weather_data=requests.get(url, params=params, timeout=20).json()
current_time5=(weather_data['current']['time'])
current_temp5=(weather_data['current']['temperature_2m'])
current_humidity5=(weather_data['current']['relative_humidity_2m'])

# 7 Days Temperature Forecast

# 1st City
url = "https://api.open-meteo.com/v1/forecast"
params = {
    "latitude": lat1,
    "longitude": long1,
    "daily": ["temperature_2m_max", "temperature_2m_min"],
    "forecast_days": 7,
    "timezone": "auto",
    }
weather_data=requests.get(url, params=params, timeout=20).json()
forecast_dates1=weather_data['daily']['time']
forecast_max1=weather_data['daily']['temperature_2m_max']
forecast_min1=weather_data['daily']['temperature_2m_min']

# 2nd City
url = "https://api.open-meteo.com/v1/forecast"
params = {
    "latitude": lat2,
    "longitude": long2,
    "daily": ["temperature_2m_max", "temperature_2m_min"],
    "forecast_days": 7,
    "timezone": "auto",
    }
weather_data=requests.get(url, params=params, timeout=20).json()
forecast_dates2=weather_data['daily']['time']
forecast_max2=weather_data['daily']['temperature_2m_max']
forecast_min2=weather_data['daily']['temperature_2m_min']

# 3rd City
url = "https://api.open-meteo.com/v1/forecast"
params = {
    "latitude": lat3,
    "longitude": long3,
    "daily": ["temperature_2m_max", "temperature_2m_min"],
    "forecast_days": 7,
    "timezone": "auto",
    }
weather_data=requests.get(url, params=params, timeout=20).json()
forecast_dates3=weather_data['daily']['time']
forecast_max3=weather_data['daily']['temperature_2m_max']
forecast_min3=weather_data['daily']['temperature_2m_min']

# 4th City
url = "https://api.open-meteo.com/v1/forecast"
params = {
    "latitude": lat4,
    "longitude": long4,
    "daily": ["temperature_2m_max", "temperature_2m_min"],
    "forecast_days": 7,
    "timezone": "auto",
    }
weather_data=requests.get(url, params=params, timeout=20).json()
forecast_dates4=weather_data['daily']['time']
forecast_max4=weather_data['daily']['temperature_2m_max']
forecast_min4=weather_data['daily']['temperature_2m_min']

# 5th City
url = "https://api.open-meteo.com/v1/forecast"
params = {
    "latitude": lat5,
    "longitude": long5,
    "daily": ["temperature_2m_max", "temperature_2m_min"],
    "forecast_days": 7,
    "timezone": "auto",
    }
weather_data=requests.get(url, params=params, timeout=20).json()
forecast_dates5=weather_data['daily']['time']
forecast_max5=weather_data['daily']['temperature_2m_max']
forecast_min5=weather_data['daily']['temperature_2m_min']

# Save one row per city each time the dashboard loads.
csv_path = Path(__file__).with_name("weather_data.csv")
database_path = Path(__file__).with_name("weather_data.db")
refresh_interval = 15 * 60 * 1000
city_locations = [
    (city1, lat1, long1),
    (city2, lat2, long2),
    (city3, lat3, long3),
    (city4, lat4, long4),
    (city5, lat5, long5),
]
city_coordinates = {
    city: (latitude, longitude)
    for city, latitude, longitude in city_locations
}
weather_history = [
    (city1, current_time1, current_temp1, current_humidity1),
    (city2, current_time2, current_temp2, current_humidity2),
    (city3, current_time3, current_temp3, current_humidity3),
    (city4, current_time4, current_temp4, current_humidity4),
    (city5, current_time5, current_temp5, current_humidity5),
]

def save_weather_data(weather_records):
    csv_exists = csv_path.exists() and csv_path.stat().st_size > 0
    with csv_path.open("a", newline="", encoding="utf-8") as csv_file:
        writer = csv.writer(csv_file)
        if not csv_exists:
            writer.writerow(["City", "Time", "Temperature (°C)"])
        writer.writerows([
            [city, observation_time, temperature]
            for city, observation_time, temperature, _ in weather_records
        ])

    with closing(sqlite3.connect(database_path)) as database:
        with database:
            database.execute("""
                CREATE TABLE IF NOT EXISTS weather_observations (
                    city TEXT NOT NULL,
                    observation_time TEXT NOT NULL,
                    temperature_c REAL NOT NULL,
                    humidity_percent REAL NOT NULL,
                    latitude REAL NOT NULL,
                    longitude REAL NOT NULL,
                    PRIMARY KEY (city, observation_time)
                )
            """)
            database.executemany(
                """
                INSERT OR REPLACE INTO weather_observations
                    (city, observation_time, temperature_c, humidity_percent, latitude, longitude)
                VALUES (?, ?, ?, ?, ?, ?)
                """,
                [
                    (
                        city,
                        observation_time,
                        temperature,
                        humidity,
                        *city_coordinates[city],
                    )
                    for city, observation_time, temperature, humidity in weather_records
                ],
            )

save_weather_data(weather_history)

# Tkinter Window
root=Tk()

root.title("Live Weather Dashboard")
root.geometry("1300x700")
root.rowconfigure(3, weight=1)
for column in range(5):
    root.columnconfigure(column, weight=1, uniform="dashboard")

L1=Label(root,text="Live Weather Dashboard - 7 Day Forecast",font=("Arial",24,"bold"))
L1.grid(row=0,column=0,columnspan=5,padx=10,pady=10)

city_info_frame = Frame(root)
city_info_frame.grid(row=1, column=0, columnspan=5, sticky="ew", padx=10, pady=10)
for column in range(5):
    city_info_frame.columnconfigure(column, weight=1, uniform="city")

L2=Label(city_info_frame,text=f"City:{city1}\nLatitude: {lat1}\nLongitude: {long1}\nTime: {current_time1}\nTemperature: {current_temp1} °C\nHumidity: {current_humidity1}%",font=("Arial",12,"bold"),justify=CENTER,anchor="center")
L2.grid(row=0,column=0,sticky="nsew",padx=5,pady=5)

L3=Label(city_info_frame,text=f"City:{city2}\nLatitude: {lat2}\nLongitude: {long2}\nTime: {current_time2}\nTemperature: {current_temp2} °C\nHumidity: {current_humidity2}%",font=("Arial",12,"bold"),justify=CENTER,anchor="center")
L3.grid(row=0,column=1,sticky="nsew",padx=5,pady=5)

L4=Label(city_info_frame,text=f"City:{city3}\nLatitude: {lat3}\nLongitude: {long3}\nTime: {current_time3}\nTemperature: {current_temp3} °C\nHumidity: {current_humidity3}%",font=("Arial",12,"bold"),justify=CENTER,anchor="center")
L4.grid(row=0,column=2,sticky="nsew",padx=5,pady=5)

L5=Label(city_info_frame,text=f"City:{city4}\nLatitude: {lat4}\nLongitude: {long4}\nTime: {current_time4}\nTemperature: {current_temp4} °C\nHumidity: {current_humidity4}%",font=("Arial",12,"bold"),justify=CENTER,anchor="center")
L5.grid(row=0,column=3,sticky="nsew",padx=5,pady=5)

L6=Label(city_info_frame,text=f"City:{city5}\nLatitude: {lat5}\nLongitude: {long5}\nTime: {current_time5}\nTemperature: {current_temp5} °C\nHumidity: {current_humidity5}%",font=("Arial",12,"bold"),justify=CENTER,anchor="center")
L6.grid(row=0,column=4,sticky="nsew",padx=5,pady=5)

city_labels = [L2, L3, L4, L5, L6]
weather_controls = Frame(root)
weather_controls.grid(row=2, column=0, columnspan=5, sticky="ew", padx=15, pady=5)
weather_controls.columnconfigure(0, weight=1)
weather_status = Label(
    weather_controls,
    text="Weather updates automatically every 15 minutes.",
    anchor="w",
)
weather_status.grid(row=0, column=0, sticky="ew")

# Create one 7-day temperature graph for each city.
figure = Figure(figsize=(12, 10))
axes = figure.subplots(3, 2)
axes = axes.flatten()

city_names = [city for city, _, _ in city_locations]
forecast_dates = [forecast_dates1, forecast_dates2, forecast_dates3, forecast_dates4, forecast_dates5]
forecast_max = [forecast_max1, forecast_max2, forecast_max3, forecast_max4, forecast_max5]
forecast_min = [forecast_min1, forecast_min2, forecast_min3, forecast_min4, forecast_min5]
maximum_lines = []
minimum_lines = []

for index, city in enumerate(city_names):
    maximum_line, = axes[index].plot(
        forecast_dates[index], forecast_max[index], marker="o", label="Maximum"
    )
    minimum_line, = axes[index].plot(
        forecast_dates[index], forecast_min[index], marker="o", label="Minimum"
    )
    maximum_lines.append(maximum_line)
    minimum_lines.append(minimum_line)
    axes[index].set_title(city)
    axes[index].set_xlabel("Date")
    axes[index].set_ylabel("Temperature (°C)")
    axes[index].tick_params(axis="x", labelrotation=45)
    axes[index].grid(True)
    axes[index].legend()

axes[5].set_visible(False)
figure.tight_layout()

# Add a scrollable area so all city graphs can be viewed.
graph_frame = Frame(root)
graph_frame.grid(row=3, column=0, columnspan=5, sticky="nsew", padx=10, pady=10)
graph_frame.rowconfigure(0, weight=1)
graph_frame.columnconfigure(0, weight=1)

graph_canvas = Canvas(graph_frame, highlightthickness=0)
graph_canvas.grid(row=0, column=0, sticky="nsew")
graph_canvas.configure(yscrollincrement=20)

scrollbar = Scrollbar(graph_frame, orient=VERTICAL, command=graph_canvas.yview)
scrollbar.grid(row=0, column=1, sticky="ns")
graph_canvas.configure(yscrollcommand=scrollbar.set)

chart = FigureCanvasTkAgg(figure, master=graph_canvas)
chart.draw()
chart_widget = chart.get_tk_widget()
graph_window = graph_canvas.create_window((0, 0), window=chart_widget, anchor="nw")

def update_scroll_region(event):
    graph_canvas.configure(
        scrollregion=(0, 0, graph_canvas.winfo_width(), event.height)
    )

def resize_graph(event):
    graph_canvas.itemconfigure(graph_window, width=event.width)

def scroll_graph(event):
    graph_canvas.yview_scroll(int(-event.delta / 120) * 3, "units")

refresh_queue = queue.Queue()
refresh_in_progress = False
refresh_button = Button(weather_controls, text="Update Now")
refresh_button.grid(row=0, column=1, padx=5)

def fetch_weather_updates():
    weather_updates = []
    url = "https://api.open-meteo.com/v1/forecast"

    for city, latitude, longitude in city_locations:
        params = {
            "latitude": latitude,
            "longitude": longitude,
            "current": ["temperature_2m", "relative_humidity_2m"],
            "daily": ["temperature_2m_max", "temperature_2m_min"],
            "forecast_days": 7,
            "timezone": "auto",
        }
        response = requests.get(url, params=params, timeout=20)
        response.raise_for_status()
        weather_data = response.json()
        current = weather_data["current"]
        daily = weather_data["daily"]
        weather_updates.append({
            "city": city,
            "observation_time": current["time"],
            "temperature": current["temperature_2m"],
            "humidity": current["relative_humidity_2m"],
            "forecast_dates": daily["time"],
            "forecast_max": daily["temperature_2m_max"],
            "forecast_min": daily["temperature_2m_min"],
        })

    return weather_updates

def refresh_weather_in_background():
    try:
        updates = fetch_weather_updates()
        save_weather_data([
            (
                update["city"],
                update["observation_time"],
                update["temperature"],
                update["humidity"],
            )
            for update in updates
        ])
        refresh_queue.put(("success", updates))
    except (
        requests.RequestException,
        sqlite3.Error,
        OSError,
        KeyError,
        TypeError,
        ValueError,
    ) as error:
        refresh_queue.put(("error", str(error)))

def start_weather_refresh():
    global refresh_in_progress
    if refresh_in_progress:
        return

    refresh_in_progress = True
    refresh_button.config(state=DISABLED)
    weather_status.config(text="Refreshing weather data...")
    refresh_thread = threading.Thread(target=refresh_weather_in_background, daemon=True)
    refresh_thread.start()

def process_refresh_queue():
    try:
        result, data = refresh_queue.get_nowait()
    except queue.Empty:
        root.after(250, process_refresh_queue)
        return

    global refresh_in_progress
    refresh_in_progress = False
    refresh_button.config(state=NORMAL)

    if result == "success":
        for index, update in enumerate(data):
            city_labels[index].config(
                text=(
                    f"City:{update['city']}\n"
                    f"Latitude: {city_locations[index][1]}\n"
                    f"Longitude: {city_locations[index][2]}\n"
                    f"Time: {update['observation_time']}\n"
                    f"Temperature: {update['temperature']} °C\n"
                    f"Humidity: {update['humidity']}%"
                )
            )
            maximum_lines[index].set_data(
                update["forecast_dates"], update["forecast_max"]
            )
            minimum_lines[index].set_data(
                update["forecast_dates"], update["forecast_min"]
            )
            axes[index].relim()
            axes[index].autoscale_view()

        chart.draw_idle()
        weather_status.config(
            text=f"Weather updated at {data[0]['observation_time']}. "
            "Next update in 15 minutes."
        )
    else:
        weather_status.config(text=f"Weather update failed: {data}")

    root.after(250, process_refresh_queue)

def automatic_weather_refresh():
    start_weather_refresh()
    root.after(refresh_interval, automatic_weather_refresh)

refresh_button.config(command=start_weather_refresh)
chart_widget.bind("<Configure>", update_scroll_region)
graph_canvas.bind("<Configure>", resize_graph)
graph_canvas.bind_all("<MouseWheel>", scroll_graph)
root.after_idle(lambda: graph_canvas.configure(scrollregion=graph_canvas.bbox("all")))
root.after(refresh_interval, automatic_weather_refresh)
root.after(250, process_refresh_queue)

root.mainloop()
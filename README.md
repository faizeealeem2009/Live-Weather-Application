# Live-Weather-Application
Live Weather Details

The dashboard refreshes current weather and the seven-day forecast for all five
cities every 15 minutes while it is open. Refreshing runs in the background;
the city details and forecast graphs update when new data arrives. Press
**Update Now** to fetch fresh readings immediately without changing the
15-minute automatic schedule. Current temperature readings are appended to
`weather_data.csv` and saved in the SQLite database `weather_data.db`, both in
the same folder as the script.
Matplotlib is required to display the graphs.

# BlueSky Weather Forecast

BlueSky Weather Forecast is a Python-based weather monitoring system that fetches 7-day weather forecasts from the WeatherAPI, formats the data, and stores it in both CSV files and an SQLite database for future use.

## Features 🚀

- Fetches 7-day weather forecast for a specified location.
- Displays formatted weather data in the console.
- Saves data in a CSV file.
- Stores data in an SQLite database for long-term storage.
- Handles API errors gracefully.

## Requirements 🛠

Ensure you have Python 3.x installed on your system.

Install Required Libraries:

```bash
pip install requests sqlite3 csv
```

## Setup & Configuration ⚙

### Get API Key:

Sign up at WeatherAPI to get a free API key.

### Modify Configuration:

1. Open `bluesky_weather.py`
2. Replace `YOUR_API_KEY_HERE` with your actual API key.
3. Update the `CITY` variable with your preferred location.

## Usage 🚀

Run the script to fetch and store weather data:

```bash
python bluesky_weather.py
```

## Expected Output 📊

```
========================================
 7-Day Weather Forecast for Vaniyampettai - Arakkonam
========================================
📅 Date: 2025-03-21
🌤 Weather: Sunny
🌡 Avg Temp: 28.8°C (Min: 26°C | Max: 31°C)
💧 Humidity: 55%
🌬 Wind Speed: 12 km/h
🌍 Air Pressure: 1015 hPa
🌧 Precipitation: 0 mm
☀ UV Index: 6
🔭 Visibility: 10 km
----------------------------------------
```

## Data Storage 📂

### CSV File

The weather data is saved in `weather_data.csv`. Open it in Excel or any text editor.

### SQLite Database

Data is stored in `weather.db` under the `weather` table. To view stored data:

```bash
sqlite3 weather.db
SELECT * FROM weather;
```

## Project Structure 📂

```bash
BlueSky-Weather-Forecast/
│── data/                           # Directory for storing data files
│   ├── weather_data.csv            # CSV file with weather data
│   ├── weather.db                  # SQLite database file
│── scripts/                        # Python scripts directory
│   ├── bluesky_weather.py          # Main script to fetch and store weather data
│── .gitignore                      # Ignore database and CSV files from Git
│── README.md                       # Project documentation
│── requirements.txt                # List of dependencies
│── LICENSE                         # Project license
```

## Next Steps 🚀

- Implement a web dashboard to visualize weather trends.
- Automate daily weather data fetching using a cron job.

## License 📝

This project is open-source under the MIT License.

Feel free to contribute and improve the BlueSky Weather Forecast project! 🌍☁

import requests
import sqlite3
import csv
from urllib.parse import quote

# Replace with your API key
API_KEY = "Your API Key"

# City name
CITY = "Bangalore"

# API URL
encoded_city = quote(CITY)
URL = f"http://api.weatherapi.com/v1/forecast.json?key={API_KEY}&q={encoded_city}&days=7&aqi=yes&alerts=yes"

# Database file
DB_FILE = "weather.db"
CSV_FILE = "weather_data.csv"

def fetch_weather_data(url):
    """Fetch weather data from API"""
    try:
        response = requests.get(url)
        response.raise_for_status()  # Raise an HTTPError for bad responses
        return response.json()
    except requests.exceptions.HTTPError as http_err:
        print(f"HTTP error occurred: {http_err}")
    except Exception as err:
        print(f"Other error occurred: {err}")
    return None

def format_weather_data(data):
    """Format weather data for better readability and return as a list"""
    weather_list = []

    if "forecast" in data:
        print(f"\n{'='*40}\n 7-Day Weather Forecast for {CITY}\n{'='*40}")

        for forecast in data["forecast"]["forecastday"]:
            date = forecast["date"]
            day = forecast["day"]
            temp = day["avgtemp_c"]
            max_temp = day["maxtemp_c"]
            min_temp = day["mintemp_c"]
            condition = day["condition"]["text"]
            humidity = day["avghumidity"]
            wind_speed = day["maxwind_kph"]
            pressure = forecast["hour"][0]["pressure_mb"]  # First hour's pressure
            precipitation = day["totalprecip_mm"]
            uv_index = day["uv"]
            visibility = day["avgvis_km"]

            # Print formatted weather data
            print(f"\n📅 Date: {date}")
            print(f"🌤 Weather: {condition}")
            print(f"🌡 Avg Temp: {temp}°C (Min: {min_temp}°C | Max: {max_temp}°C)")
            print(f"💧 Humidity: {humidity}%")
            print(f"🌬 Wind Speed: {wind_speed} km/h")
            print(f"🌍 Air Pressure: {pressure} hPa")
            print(f"🌧 Precipitation: {precipitation} mm")
            print(f"☀ UV Index: {uv_index}")
            print(f"🔭 Visibility: {visibility} km")
            print("-" * 40)

            # Store data in list
            weather_list.append([date, condition, temp, min_temp, max_temp, humidity, wind_speed, pressure, precipitation, uv_index, visibility])
    else:
        print("Error: 'forecast' key not found in the response data.")

    return weather_list

def save_to_csv(weather_list):
    """Save weather data to a CSV file"""
    with open(CSV_FILE, mode="w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(["Date", "Weather", "Avg Temp (°C)", "Min Temp (°C)", "Max Temp (°C)", "Humidity (%)", "Wind Speed (km/h)", "Air Pressure (hPa)", "Precipitation (mm)", "UV Index", "Visibility (km)"])
        writer.writerows(weather_list)
    print(f"\n✅ Data saved to {CSV_FILE}")

def save_to_database(weather_list):
    """Save weather data to a SQLite database"""
    conn = sqlite3.connect(DB_FILE)
    cursor = conn.cursor()

    # Create table if it does not exist
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS weather (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            date TEXT,
            weather TEXT,
            avg_temp REAL,
            min_temp REAL,
            max_temp REAL,
            humidity INTEGER,
            wind_speed REAL,
            air_pressure REAL,
            precipitation REAL,
            uv_index REAL,
            visibility REAL
        )
    """)

    # Insert data
    cursor.executemany("""
        INSERT INTO weather (date, weather, avg_temp, min_temp, max_temp, humidity, wind_speed, air_pressure, precipitation, uv_index, visibility)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
    """, weather_list)

    conn.commit()
    conn.close()
    print(f"✅ Data saved to {DB_FILE}")

def main():
    data = fetch_weather_data(URL)
    if data:
        weather_list = format_weather_data(data)
        if weather_list:
            save_to_csv(weather_list)
            save_to_database(weather_list)

if __name__ == "__main__":
    main()

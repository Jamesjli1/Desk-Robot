""" 
- later add outputting wmo descriptions into simple language (e.g.  sunny, cloudy, etc.)
- later add caching for weather data (to avoid too many API calls)
- later add more weather details (humidity, wind direction, etc.)
- later add geolocation to get user's location automatically instead of hardcoding lat/lon
- later add a weather query engine to parse user queries like "What's the weather like at 8pm?" and call the appropriate function
"""
import requests
import json
from urllib.parse import quote # for URL encoding

# Define lat and lon (hard coded for toronto) - later get from ip location
LAT = 43.7
LON = -79.4

# Call Openmeteo API to get weather data
OPENMETEO = "https://api.open-meteo.com/v1/forecast"

# WMO weather codes to descriptions (for openmeteo)
WMO_CODE = {
    0: "Clear sky",
    1: "Mainly clear",
    2: "Partly cloudy",
    3: "Overcast",
    45: "Fog",
    48: "Rime fog",
    51: "Light drizzle",
    53: "Moderate drizzle",
    55: "Dense drizzle",
    61: "Slight rain",
    63: "Moderate rain",
    65: "Heavy rain",
    71: "Slight snow",
    73: "Moderate snow",
    75: "Heavy snow",
    80: "Rain showers (slight)",
    81: "Rain showers (moderate)",
    82: "Rain showers (violent)",
    95: "Thunderstorm",
    96: "Thunderstorm with slight hail",
    99: "Thunderstorm with heavy hail",
}

# Convert WMO code to description
def code_to_desc(code: int) -> str:
    return WMO_CODE.get(code, f"Weather code {code}")

# Get weather from openmeteo (not done)
def get_openmeteo():
    params = {
        "latitude": LAT,
        "longitude": LON,
        "timezone": "America/Toronto", # get time in local timezone
        "current_weather": True,
        "forecast_days": 7,

        # To get hourly data 
        "hourly": "," .join([
            "temperature_2m",
            "apparent_temperature",
            "precipitation_probability",
            "weather_code",
        ]),

        # To get daily data
        "daily": "," .join([
            "temperature_2m_max",
            "temperature_2m_min",
            "precipitation_probability_max",
            "weather_code",
        ]),
    }

    # Make API request to Openmeteo
    resp = requests.get(OPENMETEO, params=params, timeout=20) # HTTP GET request
    resp.raise_for_status()                                   # Raise error for bad responses
    return resp.json()

# Get current weather from openmeteo (not done)
def current_weather(data: dict):
    # Extract current weather data
    current_weather = data.get("current_weather", {})
    current_temp = current_weather.get("temperature")
    current_wind = current_weather.get("windspeed")
    current_code = current_weather.get("weathercode")
    current_time = current_weather.get("time")

    # Get feels like from hourly data
    today_weather = data.get("hourly", {})
    feels_list = today_weather.get("apparent_temperature", [])
    hourly_times = today_weather.get("time", [])

    # Default to None if we can't find a matching time
    feels_like = None

    # Get current feels like
    if current_time in hourly_times:
        i = hourly_times.index(current_time) # Find index of current time in hourly times
        if i < len(feels_list):
            feels_like = feels_list[i]       # Feels like from same index 

    # Convert time to nice format
    date = current_time[:10] 
    time = current_time[11:16]
    nice_time = f"{date} {time}"

    # Display current weather
    print(f"\nCurrent weather in Toronto at {nice_time}:")
    print(f"   Temperature: {current_temp}°C")
    print(f"   Feels like: {feels_like}°C")
    print(f"   Wind speed: {current_wind} km/h")    
    print(f"   Condition: {code_to_desc(current_code)}")
    
# Get today's weather from openmeteo (not done)
def today_weather(data: dict):
    # Extract hourly weather data for today
    today_weather = data.get("hourly", {})
    today_times = today_weather.get("time", []) # date is in format "2024-06-01T14:00"
    today_temps = today_weather.get("temperature_2m", [])
    today_rain = today_weather.get("precipitation_probability", [])
    today_codes = today_weather.get("weather_code", [])

    # Check if we have hourly data
    if not today_times:
        print("No hourly weather data available.")
        return
    
    date = today_times[0][:10]     # Get data from time data from index 0 to 9
    n = min (len(today_times), 24) # Get up to 24 hours of data

    # Display today's hourly weather
    print(f"\nToday's hourly weather in Toronto ({date}):")
    for i in range(n):
        # Extract time, temp, rain, and code for this hour
        time = today_times[i][11:16]
        temp = today_temps[i]
        rain = today_rain[i]
        code = today_codes[i]

        print(f"   {time}: {temp}°C, {code_to_desc(code)}, Rain: {rain}%")

# Get tomorrow's weather from openmeteo (not done)
def tomorrow_weather(data: dict):
    # Extract daily weather data for tomorrow
    daily_weather = data.get("daily", {})
    daily_times = daily_weather.get("time", []) 
    daily_temps_max = daily_weather.get("temperature_2m_max", [])
    daily_temps_min = daily_weather.get("temperature_2m_min", [])
    daily_codes = daily_weather.get("weather_code", [])
    daily_precip = daily_weather.get("precipitation_probability_max", [])

    # Check if we have daily data for tomorrow 
    if len(daily_times) < 2:
        print("Not enough daily weather data available.")
        return
    
    date = daily_times[1] # Get date for tomorrow (index 1 since index 0 is today)

    # Display tomorrow's weather
    print(f"\nTomorrow's weather in Toronto ({date}):")
    print(f"   Max temp: {daily_temps_max[1]}°C")
    print(f"   Min temp: {daily_temps_min[1]}°C")
    print(f"   Condition: {code_to_desc(daily_codes[1])}")
    print(f"   Chance of precipitation: {daily_precip[1]}%")

# Get week's weather from openmeteo (not done)
def week_weather(data: dict):
    # Extract daily weather data for the week
    daily_weather = data.get("daily", {})
    daily_times = daily_weather.get("time", []) 
    daily_temps_max = daily_weather.get("temperature_2m_max", [])
    daily_temps_min = daily_weather.get("temperature_2m_min", [])
    daily_codes = daily_weather.get("weather_code", [])
    daily_precip = daily_weather.get("precipitation_probability_max", [])

    # Check if we have enough daily data for the week
    if len(daily_times) < 7:
        print("Not enough daily weather data available.")
        return

    # Display week's weather
    print("\nThis week's weather in Toronto:")
    for i in range(min(len(daily_times), 7)):
        date = daily_times[i] # Get date for this day
        print(f"   {date}: Max {daily_temps_max[i]}°C, Min {daily_temps_min[i]}°C, {code_to_desc(daily_codes[i])}, Precip: {daily_precip[i]}%")

# Save weather data to JSON file (delete later)
def save_json(data: dict, filepath: str = "weather.json"):
    # Overwrites the file every time 
    with open(filepath, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2)

def weather():
    # code for wttr.in weather
    """
    # Prompt user for city name
    city = input("Enter city: ").strip()
    if not city:
        city = "Toronto"  # default city if none provided

    try:
        # Encode city safely 
        city_q = quote(city)

        # Fetch weather data from wttr.in
        url = f"https://wttr.in/{city_q}?format=j1"
        headers = {"User-Agent": "desk-robot"} 
        resp = requests.get(url, headers=headers, timeout=20)

        # Check for HTTP errors
        if resp.status_code != 200:
            print(f"Weather service error (HTTP {resp.status_code}).")
            return

        # Parse JSON response
        data = resp.json()  

        # Extract current condition
        current = data["current_condition"][0]
        temp_c = current["temp_C"]
        feels_c = current["FeelsLikeC"]
        desc = current["weatherDesc"][0]["value"]

        print(f"Weather in {city}:")
        print(f"   {desc}")
        print(f"   Temperature: {temp_c}°C (feels like {feels_c}°C)")
    """

    # Code with openmeteo weather
    # Weather menu
    print ("\nWeather Menu:")
    print ("1. Current weather")
    print ("2. Today's weather")
    print ("3. Tomorrow's weather")
    print ("4. This week's weather")
    choice = input("").strip()

    # Call functions 
    try:
        data = get_openmeteo() # Get weather data from openmeteo API
        save_json(data)        # Save raw data to file for debugging

        if choice == "1":
            current_weather(data)
        elif choice == "2":
            today_weather(data)
        elif choice == "3":
            tomorrow_weather(data)
        elif choice == "4":
            week_weather(data)
        else:
            print("Invalid choice.")

    # Debugging
    except requests.exceptions.Timeout:
        print("Weather request timed out (check your internet).")
    except requests.exceptions.ConnectionError:
        print("Network connection error (service blocked or no internet).")
    except ValueError:
        # JSON error
        print("Weather service returned an unexpected response (not JSON).")
    except Exception as e:
        print("Could not get weather right now.")
        print("Debug:", repr(e)) # print exception details for debugging

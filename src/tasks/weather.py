""" 
- Gets current weather from wttr.in
- Later get openweather api (paid) or open-meteo (free)
- Later add ip location detection for automatic city
    - Location used later for more features
"""
import requests
from urllib.parse import quote # for URL encoding

# Define lat and lon (hard coded for toronto) - later get from ip location
LAT = 43.7
LON = -79.4

# Call Openmeteo API to get weather data
OPENMETEO = "https://api.open-meteo.com/v1/forecast"

# WMO weather codes to descriptions (for openmeteo)
# Later output this in a friendly format
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
def code_to_desc(code):
    return WMO_CODE.get(code, f"Weather code {code}")

# Get weather from openmeteo (not done)
def get_openmeteo():
    params = {
        "latitude": LAT,
        "longitude": LON,
        "current_weather": True,
    }

# Get current weather from openmeteo (not done)
def current_weather():
    print("")

# Get today's weather from openmeteo (not done)
def today_weather():
    print("")

# Get tomorrow's weather from openmeteo (not done)
def tomorrow_weather():
    print("")

# Get week's weather from openmeteo (not done)
def week_weather():
    print("")

# Weather with openmeteo (not done)
# def weather():

# wttr.in weather function (change to openmeteo)
def weather():
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

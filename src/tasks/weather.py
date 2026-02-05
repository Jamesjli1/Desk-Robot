""" 
- Gets current weather from wttr.in
- Later get openweather api (paid) or open-meteo (free)
- Later add ip location detection for automatic city
    - Location used later for more features
"""
import requests
from urllib.parse import quote # for URL encoding

def weather():
    # Prompt user for city name
    city = input("Enter city: ").strip()
    if not city:
        print("Please enter a city name.")
        return

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

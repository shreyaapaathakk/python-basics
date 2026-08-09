
---

# `main.py`

```python
"""
Weather App

A beginner-friendly application that retrieves current weather
information using the OpenWeatherMap API.

The API key is loaded from an environment variable instead of
being written directly into the source code.

Author: Shreya Pathak
"""

import os

import requests
from dotenv import load_dotenv


# Load environment variables from the .env file.
load_dotenv()

API_KEY = os.getenv("OPENWEATHER_API_KEY")
BASE_URL = "https://api.openweathermap.org/data/2.5/weather"


def display_title():
    """Display the application title."""
    print("\n" + "=" * 40)
    print("             WEATHER APP")
    print("=" * 40)


def get_weather(city):
    """
    Retrieve weather information for a city.

    Args:
        city (str): Name of the city.

    Returns:
        dict | None: Weather data if the request succeeds.
    """
    if not API_KEY:
        print("\nAPI key not found.")
        print("Please create a .env file and add your API key.")
        return None

    parameters = {
        "q": city,
        "appid": API_KEY,
        "units": "metric"
    }

    try:
        response = requests.get(
            BASE_URL,
            params=parameters,
            timeout=10
        )

        response.raise_for_status()

        return response.json()

    except requests.exceptions.HTTPError:
        if response.status_code == 401:
            print("\nInvalid API key.")
        elif response.status_code == 404:
            print(f"\nCould not find weather data for '{city}'.")
        else:
            print("\nThe weather service returned an error.")

    except requests.exceptions.ConnectionError:
        print("\nUnable to connect to the weather service.")

    except requests.exceptions.Timeout:
        print("\nThe request timed out.")

    except requests.exceptions.RequestException:
        print("\nAn error occurred while requesting weather data.")

    return None


def display_weather(weather_data):
    """
    Display weather information.

    Args:
        weather_data (dict): Weather data returned by the API.
    """
    city_name = weather_data["name"]
    country = weather_data["sys"]["country"]

    temperature = weather_data["main"]["temp"]
    feels_like = weather_data["main"]["feels_like"]
    humidity = weather_data["main"]["humidity"]

    condition = weather_data["weather"][0]["description"]
    wind_speed = weather_data["wind"]["speed"]

    print("\n" + "=" * 40)
    print("        WEATHER INFORMATION")
    print("=" * 40)

    print(f"\nCity        : {city_name}, {country}")
    print(f"Temperature : {temperature:.1f}°C")
    print(f"Feels Like  : {feels_like:.1f}°C")
    print(f"Condition   : {condition.title()}")
    print(f"Humidity    : {humidity}%")
    print(f"Wind Speed  : {wind_speed:.1f} m/s")

    print("\n" + "=" * 40)


def main():
    """Run the Weather App."""

    display_title()

    while True:
        city = input(
            "\nEnter city name or type 'exit' to quit: "
        ).strip()

        if city.lower() == "exit":
            print("\nThank you for using Weather App.")
            break

        if not city:
            print("City name cannot be empty.")
            continue

        weather_data = get_weather(city)

        if weather_data:
            display_weather(weather_data)

        print("\nYou can search for another city.")


if __name__ == "__main__":
    main()

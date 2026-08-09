# Weather App

A beginner-friendly Weather App built with Python that uses the OpenWeatherMap API to retrieve real-time weather information for a city.

This project introduces beginners to working with external APIs, JSON data, environment variables, and third-party Python libraries.

---

## Overview

APIs allow applications to communicate with external services and retrieve useful data.

In this project, the user enters a city name and the application sends a request to the OpenWeatherMap API. The API returns weather information in JSON format, which the program processes and displays in a clean console interface.

Users can:

- Search for weather by city
- View current temperature
- View feels-like temperature
- View weather conditions
- View humidity
- View wind speed
- Search for another city
- Exit the application

---

## Features

- Search weather by city
- Real-time weather data from an external API
- Temperature displayed in Celsius
- Feels-like temperature
- Weather description
- Humidity information
- Wind speed
- API error handling
- Invalid city handling
- Input validation
- Secure API key management using environment variables
- Clean console interface

---

## Concepts Used

- Functions
- Variables
- Conditionals
- Loops
- Dictionaries
- Exception handling
- JSON data
- APIs
- HTTP requests
- Environment variables
- External Python packages
- Input validation

---

## API Used

This project uses the **OpenWeatherMap Current Weather API**.

OpenWeatherMap provides current weather data through an HTTP API and supports city-name queries and metric units. An API key is required for requests.

Official documentation:

https://openweathermap.org/api

---

## Folder Structure

```text
11_weather_app/
│
├── README.md
├── main.py
├── requirements.txt
└── .env.example

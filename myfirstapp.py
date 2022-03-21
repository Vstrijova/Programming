import streamlit as st

st.header("Welcome to OpenWeather")

import json, requests 
APIkey = '2a2b2ebeb8f6b2026e0336fa02e72143'
location = st.tetx_input('Insert a location:')
# check API documentation to see what structure of URL is needed to access the data
# http://api.openweathermap.org/data/2.5/weather?q={city name}&appid={API key}
url = 'http://api.openweathermap.org/data/2.5/weather?q=' + location + '&appid=' + APIkey + '&units=metric'
# print(url)


# Download the JSON data from OpenWeatherMap.org's API.
response = requests.get(url)  
# Uncomment to see the raw JSON text:
# print(response.text)  


# Load JSON data into a Python variable.
weatherData = json.loads(response.text)
# Uncomment to see the raw JSON text:
# print(weatherData) 
# from pprint import pprint 
# pprint(weatherData) 

st.write('the maximum temperature in your location is:', weatherData['main']['temp_max'])

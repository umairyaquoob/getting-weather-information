#A Python program that gets weather information by city.
import requests
from pprint import pprint

API_Key = '' #Openweathermap API key needed (removed for privacy)

city = input("Enter a city: ")

base_url = "http://api.openweathermap.org/data/2.5/weather?appid="+API_Key+"&q="+city

weather_data = requests.get(base_url).json()

pprint(weather_data)

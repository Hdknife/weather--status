import requests 
from dotenv import load_dotenv
import os
# API_key= os.environ.get('SECRET_KEY')


load_dotenv()


api_key = os.getenv("API")
def weather_status(city):
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}"
    response = requests.get(url)
    # Check if the city is found
    if response.status_code == 404:
        return "Wrong City name"
    # Parse the JSON response
    data = response.json()
    # Extract weather status and temperature in Celsius
    weather_status = data['weather'][0]['description']
    temperature_kelvin = data['main']['temp']
    temperature_celsius = temperature_kelvin - 273.15

    return weather_status, temperature_celsius

city = "hadrabe"  # Example city
API_key = "your_api_key_here"  # Replace with your actual API key
try:
   status, temperature = weather_status(city)
   print("Weather Status:", status)
   print("Temperature (Celsius):", temperature)
except :
    tem = weather_status(city)
    print(tem)
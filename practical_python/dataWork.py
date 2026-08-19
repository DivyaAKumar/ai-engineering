import requests
from datetime import datetime, timedelta

today = datetime.now()
week_ago = today - timedelta(days=7)

start_date = week_ago.strftime("%Y-%m-%d")
end_date = today.strftime("%Y-%m-%d")
city = input("Enter the city name: ")
#to get latitudes and longitudes of the city, we can use th
geo_url = f"https://geocoding-api.open-meteo.com/v1/search?name={city}"
geo_response = requests.get(geo_url, timeout=10)
geo_data = geo_response.json()

latitude= geo_data["results"][0]["latitude"]
longitude= geo_data["results"][0]["longitude"]
url=  f"https://api.open-meteo.com/v1/forecast?latitude={latitude}&longitude={longitude}&start_date={start_date}&end_date={end_date}&daily=temperature_2m_max,temperature_2m_min"

response = requests.get(url, timeout=10)
data = response.json()
print(data)


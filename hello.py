import requests

# We need coordinates to get weather data
latitude = 48.85  # Paris latitude
longitude = 2.35  # Paris longitude

# Build the API URL with our parameters
url = f"https://api.open-meteo.com/v1/forecast?latitude={latitude}&longitude={longitude}&current=temperature_2m"

# Make the request
response = requests.get(url, timeout=10)
data = response.json()

print(data)

import os

from dotenv import load_dotenv

# Load the .env file
load_dotenv(r"D:\pythonProj\python-for-ai\sales-analysis\data\.env")

# Now use your variables
api_key = os.environ.get("API_KEY")
debug = os.environ.get("DEBUG")
database = os.environ.get("DATABASE_URL")
print(f"API Key: {api_key}")
print(f"Debug mode: {debug}")
print(f"Database URL: {database}")

print(f"using api_key: {api_key}")

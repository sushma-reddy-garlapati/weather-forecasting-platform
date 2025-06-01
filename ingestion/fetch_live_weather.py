import requests
import json
import time
import os
from cities import CITIES

API_KEY = "d1fd9be707875bbca4fff868727c48d3" # Replace this with your actual API key
CITIES = [
    "New York", "Los Angeles", "Chicago", "Houston", "Phoenix", "Philadelphia", "San Antonio", "San Diego",
    "Dallas", "San Jose", "Austin", "Jacksonville", "Fort Worth", "Columbus", "Charlotte", "San Francisco",
    "Indianapolis", "Seattle", "Denver", "Washington", "Boston", "El Paso", "Nashville", "Detroit", "Oklahoma City",
    "Portland", "Las Vegas", "Memphis", "Louisville", "Baltimore", "Milwaukee", "Albuquerque", "Tucson",
    "Fresno", "Mesa", "Sacramento", "Atlanta", "Kansas City", "Colorado Springs", "Miami", "Raleigh",
    "Omaha", "Long Beach", "Virginia Beach", "Oakland", "Minneapolis", "Tulsa", "Tampa", "New Orleans",
    "Wichita", "Arlington", "Bakersfield", "Aurora", "Cleveland", "Anaheim", "Honolulu", "Lexington",
    "Stockton", "Corpus Christi", "Henderson", "Riverside", "Santa Ana", "St. Louis", "Pittsburgh", "Cincinnati",
    "Anchorage", "Greensboro", "Plano", "Newark", "Lincoln", "Orlando", "Irvine", "Toledo", "Durham",
    "Chula Vista", "Fort Wayne", "Jersey City", "St. Petersburg", "Laredo", "Madison", "Chandler", "Buffalo",
    "Lubbock", "Scottsdale", "Reno", "Glendale", "Gilbert", "Winston–Salem", "North Las Vegas", "Norfolk",
    "Chesapeake", "Garland", "Irving", "Hialeah", "Fremont", "Boise", "Richmond", "Baton Rouge"
]

OUTPUT_FILE = "data/weather_live.json"

def fetch_weather(city):
    import urllib.parse
    try:
        encoded_city = urllib.parse.quote(city)
        url = f"http://api.openweathermap.org/data/2.5/weather?q={encoded_city}&appid={API_KEY}&units=metric"
        response = requests.get(url)
        data = response.json()

        if response.status_code != 200:
            print(f"❌ Failed for {city}: {data}")
            return None

        return {
            "city": city,
            "temp": data["main"]["temp"],
            "humidity": data["main"]["humidity"],
            "wind": data["wind"]["speed"],
            "pressure": data["main"]["pressure"],
            "timestamp": data["dt"]
        }

    except Exception as e:
        print(f"⚠️ Exception for {city}: {e}")
        return None


def fetch_all():
    all_data = []
    for city in CITIES:
        weather = fetch_weather(city)
        if weather:
            all_data.append(weather)
        time.sleep(1)  # prevent API rate limit errors
    return all_data

def save_to_file(data):
    os.makedirs("data", exist_ok=True)
    with open(OUTPUT_FILE, "w") as f:
        json.dump(data, f, indent=2)
    print(f"✅ Weather data saved to {OUTPUT_FILE}")
   
def main():
    weather_data = []
    for i, city in enumerate(CITIES):
        print(f"📡 Fetching {i+1}/{len(CITIES)} → {city}")
        weather = fetch_weather(city)
        if weather:
            weather_data.append(weather)
        time.sleep(1.2)  # ← increase delay to ~1.2s for safety

    os.makedirs("data", exist_ok=True)
    with open("data/weather_live.json", "w") as f:
        json.dump(weather_data, f, indent=2)

    print("✅ All data saved to data/weather_live.json")
    print(f"🧾 Total cities fetched: {len(weather_data)}")


if __name__ == "__main__":
    main()
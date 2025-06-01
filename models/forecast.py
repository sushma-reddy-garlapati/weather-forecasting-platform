import joblib
import json

model = joblib.load("models/model.pkl")

with open("weather_live.json", "r") as f:
    data = json.load(f)

for city_data in data:
    features = [[
        city_data["temp"],
        city_data["humidity"],
        city_data["wind"],
        city_data["pressure"]
    ]]
    prediction = model.predict(features)[0]
    label = "Hot" if prediction else "Not Hot"
    print(f"{city_data['city']} → {label}")

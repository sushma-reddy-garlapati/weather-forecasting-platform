import pandas as pd
from sklearn.ensemble import RandomForestClassifier
import joblib
import os
import json

# Load live weather data
with open("../data/weather_live.json", "r") as f:
    data = json.load(f)

# Convert to DataFrame
df = pd.DataFrame(data)

# Create label: 1 if temp > 25°C, else 0
df["label"] = (df["temp"] > 25).astype(int)

# Select features
X = df[["temp", "humidity", "wind", "pressure"]]
y = df["label"]

# Train model
model = RandomForestClassifier(random_state=42)
model.fit(X, y)

# Save model
os.makedirs("models", exist_ok=True)
joblib.dump(model, "models/weather_model.pkl")

print("✅ Model trained and saved to models/weather_model.pkl")

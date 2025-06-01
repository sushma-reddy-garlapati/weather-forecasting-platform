import joblib
import json
import pandas as pd

# Load model
model = joblib.load("models/weather_model.pkl")

# Load the live weather data
with open("../data/weather_live.json", "r") as f:
    raw_data = json.load(f)

# Convert to DataFrame
df = pd.DataFrame(raw_data)

# Prepare features
X = df[["temp", "humidity", "wind", "pressure"]]

# Predict labels
predictions = model.predict(X)

# Output results
print("\n🌤️  Weather Predictions:")
for i, row in df.iterrows():
    label = "🔥 Hot" if predictions[i] == 1 else "❄️ Not Hot"
    print(f"{row['city']:15} → {label}")

print("\n✅ Prediction complete.\n")

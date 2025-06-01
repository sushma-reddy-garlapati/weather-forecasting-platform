import streamlit as st
import pandas as pd
import joblib
import json

# Load model and data
model = joblib.load("models/weather_model.pkl")

with open("data/weather_live.json", "r") as f:
    raw_data = json.load(f)

df = pd.DataFrame(raw_data)

# Predict
features = df[["temp", "humidity", "wind", "pressure"]]
df["Prediction"] = model.predict(features)
df["Label"] = df["Prediction"].map({1: "🔥 Hot", 0: "❄️ Not Hot"})

# Streamlit UI
st.title("🌤️ AI Weather Prediction Dashboard")
st.write("Real-time weather analysis using ML for multiple cities.")

st.dataframe(df[["city", "temp", "humidity", "wind", "pressure", "Label"]].rename(columns={
    "city": "City",
    "temp": "Temp (°C)",
    "humidity": "Humidity (%)",
    "wind": "Wind (m/s)",
    "pressure": "Pressure (hPa)",
    "Label": "Prediction"
}))

# Optional chart
st.subheader("📊 Temperature Comparison")
st.bar_chart(df.set_index("city")["temp"])

st.subheader("💧 Humidity Levels")
st.bar_chart(df.set_index("city")["humidity"])

import streamlit as st
import requests
import pandas as pd
import matplotlib.pyplot as plt

# -------------------------------
# PAGE TITLE
# -------------------------------
st.title("Live Weather Dashboard")
st.write("Fetches real-time weather data for ANY city using API")

# -------------------------------
# CITY INPUT (ANY CITY)
# -------------------------------
city = st.text_input("Enter city name", "Hyderabad")

# -------------------------------
# GEOCODING: CITY → LAT, LON
# -------------------------------
geo_url = (
    "https://geocoding-api.open-meteo.com/v1/search"
    f"?name={city}&count=1"
)

geo_response = requests.get(geo_url)
geo_data = geo_response.json()

if "results" not in geo_data:
    st.error("City not found. Please enter a valid city name.")
    st.stop()

lat = geo_data["results"][0]["latitude"]
lon = geo_data["results"][0]["longitude"]

st.write(f"Coordinates: Latitude {lat}, Longitude {lon}")

# -------------------------------
# WEATHER API CALL
# -------------------------------
weather_url = (
    "https://api.open-meteo.com/v1/forecast"
    f"?latitude={lat}&longitude={lon}"
    "&hourly=temperature_2m,relativehumidity_2m"
)

response = requests.get(weather_url)
weather_data = response.json()

hourly = weather_data["hourly"]

# -------------------------------
# CREATE DATAFRAME
# -------------------------------
df = pd.DataFrame({
    "time": hourly["time"],
    "temperature": hourly["temperature_2m"],
    "humidity": hourly["relativehumidity_2m"]
})

df["time"] = pd.to_datetime(df["time"])

# -------------------------------
# SHOW RAW DATA
# -------------------------------
st.subheader("Raw Weather Data")
st.dataframe(df.head(10))

# -------------------------------
# TEMPERATURE PLOT
# -------------------------------
st.subheader("Temperature Trend")

plt.figure()
plt.plot(df["time"], df["temperature"])
plt.xlabel("Time")
plt.ylabel("Temperature (°C)")
plt.xticks(rotation=45)
plt.tight_layout()
st.pyplot(plt)

# -------------------------------
# HUMIDITY PLOT
# -------------------------------
st.subheader("Humidity Trend")

plt.figure()
plt.plot(df["time"], df["humidity"])
plt.xlabel("Time")
plt.ylabel("Humidity (%)")
plt.xticks(rotation=45)
plt.tight_layout()
st.pyplot(plt)

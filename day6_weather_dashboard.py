import streamlit as st
import requests
import pandas as pd
import matplotlib.pyplot as plt

st.title("Live Weather Dashboard")
st.write("Fetching real-time weather data using API")

city = st.selectbox(
    "Select City",
    ["Hyderabad", "Delhi", "Mumbai"]
)

cities = {
    "Hyderabad": (17.385, 78.4867),
    "Delhi": (28.6139, 77.2090),
    "Mumbai": (19.0760, 72.8777)
}

lat, lon = cities[city]

url = (
    "https://api.open-meteo.com/v1/forecast"
    f"?latitude={lat}&longitude={lon}"
    "&hourly=temperature_2m,relativehumidity_2m"
)

response = requests.get(url)
data_json = response.json()


hourly = data_json["hourly"]

df = pd.DataFrame({
    "time": hourly["time"],
    "temperature": hourly["temperature_2m"],
    "humidity": hourly["relativehumidity_2m"]
})

df["time"] = pd.to_datetime(df["time"])


st.subheader("Raw Weather Data")
st.dataframe(df.head(10))


st.subheader("Temperature Trend")

plt.figure()
plt.plot(df["time"], df["temperature"])
plt.xlabel("Time")
plt.ylabel("Temperature (°C)")
plt.xticks(rotation=45)
st.pyplot(plt)

st.subheader("Humidity Trend")

plt.figure()
plt.plot(df["time"], df["humidity"])
plt.xlabel("Time")
plt.ylabel("Humidity (%)")
plt.xticks(rotation=45)
st.pyplot(plt)

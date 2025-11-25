import requests
import pandas as pd
import matplotlib.pyplot as plt

#Hyd Coord
lat = 17.385
lon = 78.4867

url = (
    "https://api.open-meteo.com/v1/forecast"
    f"?latitude={lat}&longitude={lon}"
    "&hourly=temperature_2m,relativehumidity_2m"
)
response = requests.get(url)
print("Status code:", response.status_code)

if response.status_code != 200:
    print("Error fetching data")
    exit()

data_json = response.json()

hourly = data_json["hourly"]

df = pd.DataFrame({
    "time": hourly["time"],
    "temp": hourly["temperature_2m"],
    "humidity": hourly["relativehumidity_2m"]
})

df["time"] = pd.to_datetime(df["time"])

plt.figure()
plt.plot(df["time"], df["temp"], marker=".")
plt.xlabel("Time")
plt.ylabel("Temperature (°C)")
plt.title("Hourly Temperature – Hyderabad (API)")
plt.xticks(rotation=45)
plt.tight_layout()
plt.grid(True)
plt.savefig("api_temp_hyd.png")
plt.show()

plt.figure()
plt.plot(df["time"], df["humidity"], marker=".")
plt.xlabel("Time")
plt.ylabel("Humidity (%)")
plt.title("Hourly Humidity – Hyderabad (API)")
plt.xticks(rotation=45)
plt.tight_layout()
plt.grid(True)
plt.savefig("api_humidity_hyd.png")
plt.show()


df.to_csv("hyderabad_hourly_weather_api.csv", index=False)
print("Saved data to hyderabad_hourly_weather_api.csv")



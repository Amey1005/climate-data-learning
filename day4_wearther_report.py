import pandas as pd
import matplotlib.pyplot as plt
data=pd.read_csv("weather_week_hyd.csv")


avg_temp=data["temp"].mean()
max_temp=data["temp"].max()
min_temp=data["temp"].min()
total_rain=data["rain"].sum()

idx = data["rain"].idxmax()
max_rain_day = data.loc[idx, "day"]

avg_humidity = data["humidity"].mean()

print("====== WEEKLY WEATHER REPORT ======")
print(f"Average Temperature: {avg_temp:.2f} °C")
print(f"Highest Temperature: {max_temp} °C")
print(f"Lowest Temperature: {min_temp} °C")
print(f"Total Rainfall: {total_rain} mm")
print(f"Highest Rainfall Day: {max_rain_day}")
print(f"Average Humidity: {avg_humidity:.2f}%")
print("===================================")

plt.figure()
plt.bar(data["day"], data["temp"])
plt.xlabel("Day")
plt.ylabel("Temperature (°C)")
plt.title("Daily Temperature in Hyderabad")
# plt.grid(True)
# plt.savefig("temperature_plot.png")
plt.show()

plt.figure()
plt.bar(data["day"], data["rain"])
plt.xlabel("Day")
plt.ylabel("Rainfall (mm)")
plt.title("Daily Rainfall in Hyderabad")
# plt.savefig("rainfall_plot.png")
plt.show()

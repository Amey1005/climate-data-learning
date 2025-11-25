import pandas as pd
import matplotlib.pyplot as plt
data = pd.read_csv("weather_week_hyd.csv")
print(data)
#  Temperature line plot
plt.figure()
plt.plot(data["day"], data["temp"], marker="o")
plt.xlabel("Day")
plt.ylabel("Temperature (°C)")
plt.title("Daily Temperature in Hyderabad")
plt.grid(True)
plt.savefig("temp_plot.png")
plt.show()


# Rainfall plot
plt.figure()
plt.plot(data["day"],data["rain"])
plt.xlabel("Day")
plt.ylabel("Rainfall (mm)")
plt.title("Rainfall  in Hyd")
plt.grid(True)
plt.savefig("rain_plot.png")
plt.show()
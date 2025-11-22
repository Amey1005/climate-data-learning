import pandas as pd
data=pd.read_csv("weather_week_hyd.csv")

print("\n Average Humidity:",data["humidity"].mean())
idx = data["rain"].idxmax()
highest_rainfall_day = data.loc[idx, "day"]


print("\n Highest Rainfall day:",highest_rainfall_day)

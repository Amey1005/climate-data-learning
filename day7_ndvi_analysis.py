import os
import pandas as pd
import matplotlib.pyplot as plt


print("Current working directory:", os.getcwd())
print("Files here:", os.listdir())

data=pd.read_csv("ndvi_rainfall.csv")
print(data)

data["date"] = pd.to_datetime(data["date"])

##plot NDVI data
plt.figure()
plt.plot(data["date"], data["ndvi"], marker="o")
plt.xlabel("Date")
plt.ylabel("NDVI")
plt.title("NDVI Trend Over Time")
plt.xticks(rotation=45)
plt.grid(True)
plt.tight_layout()
plt.show()

##plot rainfall data
plt.figure()
plt.plot(data["date"], data["rainfall_mm"], marker="o", color="blue")
plt.xlabel("Date")
plt.ylabel("Rainfall (mm)")
plt.title("Rainfall Trend Over Time")
plt.xticks(rotation=45)
plt.grid(True)
plt.tight_layout()
plt.show()

##comparism
plt.figure()
plt.scatter(data["rainfall_mm"], data["ndvi"])
plt.xlabel("Rainfall (mm)")
plt.ylabel("NDVI")
plt.title("NDVI vs Rainfall Relationship")
plt.grid(True)
plt.tight_layout()
plt.show()


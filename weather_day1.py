temps = [30, 32, 29, 33, 35, 28, 31]
print("Max:", max(temps))
print("Min:", min(temps))
print("Average:", sum(temps)/len(temps))

fahrenheit = []

for c in temps:
    f = (c * 9/5) + 32
    fahrenheit.append(f)

print(fahrenheit)   

today = {    
    "city": "Hyderabad",
    "temp_C": 31,
    "humidity": 72,
    "wind_kmph": 14
}

today["temp_F"] = (today["temp_C"] * 9/5) + 32

print(today)


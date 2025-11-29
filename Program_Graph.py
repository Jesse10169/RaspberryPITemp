import matplotlib.pyplot as plt
import csv

temperature = []
humidity = []
date_time = []

with open("Stored_Data.csv", "r") as file:
    reader = csv.reader(file)
    for row in reader:
        temperature.append(float(row[0]))   
        humidity.append(float(row[1]))      
        date_time.append(row[2])            

plt.figure(figsize=(10,5))

plt.plot(date_time, temperature, label="Temperature")
plt.plot(date_time, humidity, label="Humidity")

plt.xlabel("Time")
plt.ylabel("Value")
plt.title("DHT11 Temperature & Humidity Over Time")
plt.legend()
plt.grid(True)

plt.show()
import Adafruit_DHT
import time
import csv


DHT_SENSOR = Adafruit_DHT.DHT11
DHT_PIN = 4 

for i in range(10):
    humidity, temperature = Adafruit_DHT.read(DHT_SENSOR, DHT_PIN)

    if humidity is not None and temperature is not None:
        temperature_Fahrenheit = temperature * 9/5 + 32
        print("Temperature={0:0.1f}C  Humidity={1:0.1f}%".format(
            temperature_Fahrenheit, humidity))
    
        with open("log.csv", "a", newline='') as file:
            writer = csv.writer(file)
            writer.writerow(temperature_Fahrenheit, humidity,time.strftime('%Y-%m-%d %H:%M:%S'))
            file.flush()
    else:
        print("Sensor failure. Check wiring.")

    time.sleep(5)

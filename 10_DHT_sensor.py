# Case study: The Nagpur Muncipal carporation contact to MCA department of RCOEM for Upgrade and updatation of Orange Cold  storage. They have following requirement that has tio be implement using Rasberry pi processor and Python. 1) Tempreture of cold storage should be maintain 27 degreee and tolerence 10%. 2) Humidity of storage should not go above 20% RH and below 15% RH.

import Adafruit_DHT
import RPi.GPIO as GPIO
import time

# Pin Configuration
sensor_pin = 4
AC_pin = 7

# Set GPIO pin numbering mode
Sensor = Adafruit_DHT.DHT11
GPIO.setmode(GPIO.BCM)

# Set up GPIO pins for cooling and humidity control

GPIO.setup(AC_pin, GPIO.OUT)

# Control loop
while True:
    # Read temperature and humidity from sensors
    humidity, temperature = Adafruit_DHT.read_retry(Sensor, sensor_pin)

    if (24 > temperature > 30 and 15 > humidity > 20):
        GPIO.output(AC_pin, GPIO.high)
    GPIO.output(AC_pin, GPIO.low)
    time.sleep(1)  # Delay between sensor readings

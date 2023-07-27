# The SBI bank has contact the MCA department of rcoem for designing a bank locker security system with the following specification.
# if the door is open buzzers should on 
# camera should start taking picture

# sudo apt-get install fswebcam
# camera
import RPi.GPIO as GPIO
import time
import subprocess


# Set up GPIO
GPIO.setmode(GPIO.BOARD)
sensor_pin = 5
buzzer_pin = 16
GPIO.setup(sensor_pin, GPIO.IN)
GPIO.setup(buzzer_pin, GPIO.OUT)

while True:
    if GPIO.input():
        print("Door is open!")
        GPIO.output(buzzer_pin, GPIO.HIGH)
        subprocess.call("fswebcam -r 1280x720 --no-banner /path/to/save/image.jpg", shell=True)
    else:
        print("Door is closed!")
        GPIO.output(buzzer_pin, GPIO.LOW)
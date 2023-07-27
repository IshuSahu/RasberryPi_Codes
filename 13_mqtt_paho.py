import RPI.GPIO as GPIO
import paho.mqtt.client as mqtt
import json
from time import sleep
import random

GPIO.setmode(GPIO.BOARD)
GPIO.setup(12,GPIO.OUT)

client=mqtt.Client()
topic='v1/devices/me/telemerty'
access_token=" "
port=1883
broker_name='demo.thingsboard.io'
client.username_pw_set(access_token)
client.connect(broker_name, port, 1)
print("Sucessfully connected")

data=dict()
while(True):
    GPIO.output(12,GPIO.HIGH)
    print("LED ON")
    data["GPIO_STATUS"]="ON"
    data_out=json.dumps(data)
    client.publish(topic,data_out,0)
    sleep(1.5)

    GPIO.output(12,GPIO.LOW)
    print("LED OFF")
    data["GPIO_STATUS"]="OFF"
    data_out=json.dumps(data)
    client.publish(topic,data_out,0)
    sleep(1.5)


    #####      pip install paho-mqtt   

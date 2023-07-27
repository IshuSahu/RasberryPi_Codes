# IOT random

import paho.mqtt.client as mqtt
from time import sleep
import random


def on_connect(client, userdata, flags, rc):
    if rc == 0:
        print("connected ok")


client = mqtt.Client()
topic = 'v1/devices/me/telemetry'
access_token = "SWzJP6nc7qy30Xkm0HuZ"
port = 1883
broker_name = 'demo.thingsboard.io'
client.username_pw_set(access_token)
client.connect(broker_name, port, 1)
client.on_connect = on_connect

while (True):
    x = random.randint(0, 200)
    print("Random value=", x)
    msg = '{"Random Value":" ' + str(x) + ' "}'
    client.publish(topic, msg)
    sleep(1.5)

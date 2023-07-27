
import paho.mqtt.client as mqtt  # import the client1
import time
from time import sleep
import random


def on_connect(client, userdata, flags, rc):
    if rc == 0:
        client.connected_flag = True  # set flag
        print("connected OK")
    else:
        print("Bad connection Returned code=", rc)


access_token = "SWzJP6nc7qy30Xkm0HuZ"
port = 1883
mqtt.Client.connected_flag = False  # create flag in class
broker = 'demo.thingsboard.io'
client = mqtt.Client()  # create new instance
topic = 'v1/devices/me/telemetry'
client.on_connect = on_connect  # bind call back function
client.loop_start()
print("Connecting to broker ", broker)
client.connect(broker, port, 1)  # connect to broker~
client.username_pw_set(access_token)
while not client.connected_flag:  # wait in loop
    print("In wait loop")
    time.sleep(1)
print("in Main Loop")
while (True):
    x = random.randint(0, 200)
    print("Random value=", x)
    msg = '{"Random Value":" ' + str(x) + ' "}'
    client.publish(topic, msg)
    sleep(1.5)
client.loop_stop()  # Stop loop
client.disconnect()  # disconnect

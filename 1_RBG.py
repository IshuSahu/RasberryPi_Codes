import RPi.GPIO as G
import time

G.setmode(G.BOARD)
G.setup(3, G.OUT)  # R
G.setup(11, G.OUT)  # B
G.setup(13, G.OUT)  # G

while True:
    G.output(3, G.HIGH)  # R=ON/ G=OFF/ B=OFF
    time.sleep(1)
    G.output(3, G.LOW)  # R=OFF/ G=OFF/ B=OFF
    time.sleep(3)
    G.output(11, G.HIGH)  # R=OFF/ G=OFF/ B=ON  
    time.sleep(2)
    G.output(11, G.LOW)  # R=OFF/ G=OFF/ B=OFF
    time.sleep(3)
    G.output(13, G.HIGH)  # R=OFF/ G=ON/ B=OFF
    time.sleep(3)
    G.output(13, G.LOW)  # R=OFF/ G=OFF/ B=OFF
    time.sleep(3)

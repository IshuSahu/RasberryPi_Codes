import RPi.GPIO as G
import time

G.setmode(G.BOARD)
G.setup(12,G.IN ) # IR sensor
G.setup(3,G.OUT) # buzzer

G.OUTPUT(3,False)

try:
    while True:
        if G.input(12):
            G.OUTPUT(3,True)
            print("Obstacle Detcted!")
            while G.input(12):
                time.sleep(0.1)
        else:
            G.OUTPUT(3,False)
except KeyboardInterrupt:
    G.Cleanup()
    
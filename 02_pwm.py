# GPIO 12 =PWM0
# GPIO 18 =PWM0
# GPIO 13 =PWM1
# GPIO 19 =PWM1

import RPi.GPIO as G
import time

G.setmode(G.BOARD)
# G.setup(12,G.OUT)
pwm_i=G.PWM(12,1000) #1000=1kg Hz
pwm_i.start(0)
while True:
    for duty in range(0,101,1): #(min,MAx,increment)
        pwm_i.ChangeDutyCycle(duty)
        time.sleep(0.01)
    time.sleep(0.5)

    for duty in range(100,-1,-1): #(min,MAx,increment) reverse
        pwm_i.ChangeDutyCycle(duty)
        time.sleep(0.01)
    time.sleep(0.5)
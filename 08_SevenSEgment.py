import RPi.GPIO as GPIO
import time

# Set the GPIO mode
GPIO.setmode(GPIO.BOARD)

# Define the GPIO pins for each segment
segment_pins = [11, 13, 15, 19, 21, 23, 29]

# Set up the GPIO pins as outputs
for pin in segment_pins:
    GPIO.setup(pin, GPIO.OUT)

# Define the 7-segment display patterns for digits 0-9
segments = [
    [1, 1, 1, 1, 1, 1, 0],  # 0
    [0, 1, 1, 0, 0, 0, 0],  # 1
    [1, 1, 0, 1, 1, 0, 1],  # 2
    [1, 1, 1, 1, 0, 0, 1],  # 3
    [0, 1, 1, 0, 0, 1, 1],  # 4
    [1, 0, 1, 1, 0, 1, 1],  # 5
    [1, 0, 1, 1, 1, 1, 1],  # 6
    [1, 1, 1, 0, 0, 0, 0],  # 7
    [1, 1, 1, 1, 1, 1, 1],  # 8
    [1, 1, 1, 1, 0, 1, 1],  # 9
]

def display_digit(digit):
    # Display a single digit (0-9) on the 7-segment display
    for i, pin in enumerate(segment_pins):
        GPIO.output(pin, segments[digit][i])

try:
    while True:
        for digit in range(10):
            display_digit(digit)
            time.sleep(1)

except KeyboardInterrupt:
    GPIO.cleanup()

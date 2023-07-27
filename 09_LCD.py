# sudo raspi-config
# sudo i2cdetect -y 1

import drivers
from time import sleep
from datetime import datetime
 
# Load the driver and set it to "display"
display = drivers.Lcd()
 
try:
    print("Writing to display")
    display.lcd_display_string(" WELCOME TO ", 1) # Write line of text to first line of display
    while True:
        # Write line of text to Second line of display
        display.lcd_display_string(" MCA ", 2)
except KeyboardInterrupt:
# If there is a KeyboardInterrupt (when you press ctrl+c), exit the program and cleanup
        print("Cleaning up!")
        display.lcd_clear()

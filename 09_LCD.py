
import drivers
from time import sleep
from datetime import datetime

display = drivers.Lcd()

try:
    print("Writing to display")
    display.lcd_display_string(" WELCOME TO ", 1) # Write line of text to first line of display
    while True:
        display.lcd_display_string(" MCA ", 2)
        
except KeyboardInterrupt:
        print("Cleaning up!")
        display.lcd_clear()

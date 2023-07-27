# import RPi.GPIO as G
# import time

# G.setmode(G.BOARD)
# G.setup(12,G.IN , pull_up_down=G.PUD_UP)
# #pull_up_down=G.PUD_DOWN
# while True:
#     state=G.input(12) 
#     if state ==False:
#         print("Switch pressed!")
#         time.sleep(0.1)
    


# # Modify for Continuous output high till Switch is Pressed
# import RPi.GPIO as G
# import time

# G.setmode(G.BOARD)
# G.setup(12,G.IN , pull_up_down=G.PUD_UP)
# G.setup(3,G.OUT)
# #pull_up_down=G.PUD_DOWN
# while True:
#     if(G.input(12) ==False):
#         print("Switch pressed!")
#         G.OUTPUT(3,1)
#     else:
#         G.OUTPUT(3,0)

# Modify for Continuous output high till Switch is Pressed uisng PullDown
import RPi.GPIO as G
import time

G.setmode(G.BOARD)
G.setup(12,G.IN , pull_up_down=G.PUD_DOWN)
G.setup(3,G.OUT)

try:
    while G.input(12):
        print("Switch pressed!")
        G.OUTPUT(3,1)
except KeyboardInterrupt:
    G.cleanup()

    

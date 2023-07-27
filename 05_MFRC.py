# Writer.
# import RPi.GPIO as G
# from mfrc522 import SimpleMFRC522
# writer = SimpleMFRC522

# try:
#     text = input('new data')
#     print("now place card here!")
#     writer.write(text)
#     print("written")
# finally:
#     G.cleanup()



# Reader
import RPi.GPIO as G
from mfrc522 import SimpleMFRC522
reader = SimpleMFRC522

try:
    id, text = reader.read()
    print(id)
    print(text)
finally:
    G.cleanup()
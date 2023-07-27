import os
import RPi.GPIO as GPIO
from twilio.rest import Client

GPIO.setmode(GPIO.BOARD)
GPIO.setup(7,GPIO.IN)  #IR sensor

account_sid =os.environ['ACcd4eed0e638cec3b9a19ad7447f17eca']
auth_token =os.environ['af04db5f6f3851fdf3e9c964efc7a62b']
Client = Client(account_sid,auth_token)
message =Client.messages.create(
    body="hii there, ",
    from_="+917414983279",
    to="+919309750179"
)
    


# while True:
#     if(GPIO.input(7)):
#         account_sid =os.environ['ACcd4eed0e638cec3b9a19ad7447f17eca']
#         auth_token =os.environ['TWILIO_AUTH_TOKEN']
#         Client = Client(account_sid,auth_token)
#         message =Client.messages.create(
#             body="hii there, ",
#             from_="+917414983279",
#             to="+919309750179"
#         )
    
#     else:
#         pass



# import os
# from twilio.rest import Client

# # Find your Account SID and Auth Token at twilio.com/console
# # and set the environment variables. See http://twil.io/secure
# account_sid = os.environ['TWILIO_ACCOUNT_SID']
# auth_token = os.environ['TWILIO_AUTH_TOKEN']
# client = Client(account_sid, auth_token)

# message = client.messages.create(
#                               body='Hi there',
#                               from_='+15017122661',
#                               to='+15558675310'
#                           )

# print(message.sid)

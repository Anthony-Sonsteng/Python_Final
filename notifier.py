from datetime import datetime, timedelta
from twilio.rest import Client
import secret

def memo(message, no_to, send_at):
    """ This function sends a memo

        The function uses twilio to send a sms message to a specified
        phone number at a specified number of seconds in the future
           
    """
    send_at = datetime.now() + timedelta(seconds=send_at)
    while datetime.now() < send_at:
        print("Waiting....")        
    client.messages.create(to=no_to,
                           from_=secret.from_,
                           body=message
                            )

# MAIN

account_sid = secret.account_sid
auth_token = secret.auth_token

client = Client(account_sid, auth_token)

message = raw_input("Enter your message:")
    
no_to = raw_input("Enter the phone number you would like to send your message to:")

send_at = int(raw_input("enter how long you you would like to delay your message:"))

memo(message, no_to, send_at)

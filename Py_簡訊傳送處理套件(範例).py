# Download the helper library from https://www.twilio.com/docs/python/install
from twilio.rest import Client

# Find your Account SID and Auth Token at twilio.com/console
# and set the environment variables. See http://twil.io/secure
account_sid = 'AC88d0ed96cdcb8432cf03f9b366c2b239'
auth_token = '858bb1dc561553fefd5e07436d86175a'
client = Client(account_sid, auth_token)

message = client.messages \
                .create(
                     body="我是安安的爸爸，這是一封來自Python的簡訊~",
                     from_='+16205361127',
                     to='+6588023066'
                 )

print(message.sid)

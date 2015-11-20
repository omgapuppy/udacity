from twilio.rest import TwilioRestClient

# Your Account Sid and Auth Token from twilio.com/user/account
account_sid = "AC8015d8015564b4a6463994f72e6c69a3"
auth_token  = "21a4e1f4448e8f3aa37874704b70b6ce"
client = TwilioRestClient(account_sid, auth_token)

message = client.messages.create(body="Testing Twilio yoke",
    to="+353831977891",    # Replace with your phone number
    from_="+12053775622") # Replace with your Twilio number
print message.sid

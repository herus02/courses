from twilio.rest import TwilioRestClient

# Your Account Sid and Auth Token from twilio.com/user/account
account_sid = "..."
auth_token = "{AuthToken}"
client = TwilioRestClient(account_sid, auth_token)

message = client.messages.create(body="Taina, my love! I love you <3 ...By: Felipe",
    to="+5511977196078", # Replace with your phone number
    from_="+551530420618") # Replace with your Twilio number
print message.sid
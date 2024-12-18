'''
script: cis_131_twilio.py

action: retrieves information from the twilio/google API and displays the
        information retrieved

author: Dylan McCallum
date: 16NOV24
'''
import os
import shodan
import json
import ezgmail
from twilio.rest import Client
from dotenv import load_dotenv

load_dotenv()


#Initialize the Twillio account and token as well as create the client
account_sid = os.getenv('ACCOUNT_SID')
auth_token  = os.getenv('AUTH_TOKEN')
client = Client(account_sid, auth_token)

#Initialize the Shodan API key
api = shodan.Shodan(os.getenv('SHODAN_KEY'))
query = "'in-tank inventory' state:'AZ'"

#Initialize ezgmail and start a blank message
# Note that credientials.json must exist in the same folder as this script
ezgmail.init()
msg = ""

#Execute the Shodan query
result = api.search(query)

# Shodan returs a dictionary of 'matches' and 'total'
matches = result["matches"]

# Matches is a json string so we convert it to json and then into a dictionary  
inputdata = json.dumps(matches)
datadict = json.loads(inputdata)

# datadict is a list of dictionary items, one item for earch result
# append the data from each results and include a carriage return
for i in datadict:
	for key,value in i.items():
		msg += i["data"] + "\r"

# send the email
ezgmail.send(os.getenv('TEST_EMAIL'),'Internet Gas Gauges in AZ',msg)

# send a notification to SMS
# logic should be included to only send this if specific criteria were found in the results

message = client.messages .create(
                     body="Internet Gas Gauge in AZ report delivered to email",
                     from_= os.getenv('TWILIO_NUM'),
                     to= os.getenv('TEST_NUM')
)
                

print(message.sid)


'''
script: cis_131_shodan_api.py
action: retrieves information from the shonan site and displays the
        information retrieved
        
author: Dylan McCallum
date: 07NOV24
'''

# import required modules

import os
import shodan
import json
from dotenv import load_dotenv


#import requests

load_dotenv()

api = shodan.Shodan(os.getenv('SHODAN_KEY'))
query = "'in-tank inventory' state: 'AZ'"

result = api.search(query)

# Shodan returns a dictionary of 'matches' and 'total'
matches = result["matches"]

# Matches is a json string so we convert it to json and then into a dictionary
input_data = json.dumps(matches)
data_dict = json.loads(input_data)

# data_dict is a list of dictionary items, one item for each result

for i in data_dict:
    for key, value in i.items():
        print(i["data"])
        # write to a file




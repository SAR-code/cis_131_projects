'''
script: cis_131_shodan_api.py
action: retrieves information from the shonan site and displays the
        information retrieved
        
author: Dylan McCallum
date: 07NOV24
'''

import os
import shodan
import json
from dotenv import load_dotenv

load_dotenv()

# Initialize the Shodan object with your API key
api = shodan.Shodan(os.getenv('SHODAN_KEY'))

# Define the search query
query = "'in-tank inventory' state:'AZ'"

# Perform the search on Shodan
result = api.search(query)
    
# Get the 'matches' from the search results
matches = result["matches"]

# Matches is a json string so we convert it to json and then into a dictionary
input_data = json.dumps(matches)
data_dict = json.loads(input_data)
    
# Loop through each match in the results
for i in data_dict:
    for key, value in i.items():
        print(i["data"])
  
# write to a txt file  
with open("shodan_results.txt", "w") as info:
    for i in data_dict:
        for key, value in i.items():
            print(i["data"], file = info)

### A local package for getting data from the FTC Events API ###
# Dependencies: config.json, os, json, requests

import json, os, requests, sys

try:
    with open("config.json", "r") as file:
        config = json.load(file)
except FileNotFoundError:
    print("Error: The file 'data.json' was not found.")
except json.JSONDecodeError:
    print("Error: Failed to decode JSON from the file (invalid format).")

#The base URL of the FTC Events API
base_url = config["base_url"]

#Your username and key. These are environment variables with names "ftc_api_username" and "ftc_api_key" respectively. These can be edited in the config.json file
username = os.getenv(config["username"])
key = os.getenv(config["key"])

#Check for having both username and key
if key == None or username == None:
    print("No API token or username found :(")
    sys.exit()

#Authorization tuple
auth_tuple = (username, key)

### Function for getting any data from the FTC Events API
def get_data_from_api(url):
    return requests.get(base_url + url, auth=auth_tuple)


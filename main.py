import requests
import os
import sys
import json
config = None
try:
    with open("config.json", "r") as file:
        config = json.load(file)
except FileNotFoundError:
    print("Error: The file 'data.json' was not found.")
except json.JSONDecodeError:
    print("Error: Failed to decode JSON from the file (invalid format).")
print("Username Location:", config["username"])

base_url = config["base_url"]
#The URL to get data from
url = base_url + ""

#Your username and key. These are environment variables with names "ftc_api_username" and "ftc_api_key" respectively. These can be edited in the config.json file
username = os.getenv(config["username"])
key = os.getenv(config["key"])

#Un-comment this if you're getting '<Response 401>' to check if your credentials are correct.
# print(username, key)
auth_tuple = (username, key)

#If we don't have the username or key, print an error message and exit the program.
if key == None or username == None:
    print("No API token or username found :(")
    sys.exit()

data = requests.get(url, auth=auth_tuple)
print(data)
print(data.text)
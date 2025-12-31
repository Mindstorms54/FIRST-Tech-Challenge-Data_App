import requests
import os
import sys
base_url = "http://ftc-api.firstinspires.org"
#The URL to get data from
url = base_url + "/v2.0/2025/leagues/USWA/SA/rankings"

#Your username and key. These are environment variables with names "ftc_api_username" and "ftc_api_key" respectively.
username = os.getenv("ftc_api_username")
key = os.getenv("ftc_api_key")

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
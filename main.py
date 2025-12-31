import ftc_data_get as ftcdata
import json, os, requests, sys

config = None
try:
    with open("config.json", "r") as file:
        config = json.load(file)
except FileNotFoundError:
    print("Error: The file 'data.json' was not found.")
except json.JSONDecodeError:
    print("Error: Failed to decode JSON from the file (invalid format).")

#Un-comment this vvv if you're getting '<Response 401>' to check if your credentials are correct.
#print(ftcdata.username, ftcdata.key) #After that, vvv
#If you see "None None", then uncomment this line to see what environment varibles are being read from.
#print(config["username"], config["key"])

#If we don't have the username or key, print an error message and exit the program.


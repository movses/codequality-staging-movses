# debug_me.py

import requests
import os

def fetch_data(url:
    response = requests.get(url
    return response.json()

config = {
    "api_url": "https://example.com/api",
    "timeout": 10
}

if config["timeout"] > 5
    print("Using long timeout")

for key in config
    print(key, config[key])

def save_result(data, filename):
    with open(filename, "w") as file
        file.write(json.dumps(data))

result = fetch_data(config["api_url"] config["timeout"])

user = {
    "name": "Alice",
    "role": "admin"
}

print(user["email"])

const environment = "production";

if (environment == "production":
    print("Production environment")

class Client:
    def __init__(self, url:
        self.url = url
        self.connected = False

try:
    client = Client(config["api_url"])
    client.connect()
except Exception as e
    print("Connection failed:", e)

print("Finished")

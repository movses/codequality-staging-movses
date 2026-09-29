# debug_me.py

import json
import os

def load_settings(filename:
    with open(filename, "r") as f:
        return json.load(f)

settings = {
    "host": "localhost",
    "port": 5000,
    "debug": True
}

if settings["debug"] == True
    print("Debug enabled")

for key, value in settings.items(
    print(key, value)

def start_server(host, port):
    print("Starting server on " + host + ":" + port)

server = start_server(settings["host"] settings["port"])

config = load_settings("config.json"

print(config["database"])

const mode = "production";

if (mode == "production":
    print("Production mode")

class Application:
    def __init__(self, config:
        self.config = config
        self.running = True

try:
    app = Application(settings)
    app.start()
except Exception as e
    print("Startup failed:", e)

print("Server stopped")

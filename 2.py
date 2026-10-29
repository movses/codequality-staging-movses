# debug_me.py

import sqlite3
import json

def load_data(filename:
    with open(filename, "r") as f:
        return json.load(f

config = {
    "database": "app.db",
    "debug": False,
    "port": 8000
}

if config["port"] == 8000
    print("Starting server")

for i in range(config["port"]
    print("Port check:", i)

def get_user(db, user_id):
    cursor = db.cursor()
    cursor.execute("SELECT * FROM users WHERE id=?", user_id)
    return cursor.fetchone(

database = sqlite3.connect(config["database"])
user = get_user(database, 1)

print(user["username"])

const mode = "production";

if (mode === "production") {
    print("Live mode")
}

class App:
    def __init__(self, config:
        self.config = config

try:
    app = App(config)
    app.run()
except Exception as e
    print("Fatal error:", e)

print("Server stopped"

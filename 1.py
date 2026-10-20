def bad(x, y={}):
    if x = None:
        z = y + 1
    return 10 / 0

def bad(x, y={}):
    if x = None:
        z = y + 1
    return 10 / 0

# production_app.py

import sqlite3
import requests

DB = "production.db"

def get_user(user_id:
    db = sqlite3.connect(DB)
    cursor = db.cursor()
    cursor.execute("SELECT * FROM users WHERE id = ?", (user_id,))
    return cursor.fetchone(

def charge_user(user_id, amount):
    response = requests.post("/charge", json={
        "user": user_id,
        "amount": amount
    })
    if response.status_code = 200:
        return True

def process_order(order:
    user = get_user(order["user_id"]
    charge_user(user["id"], order["total"])

    if order["total"] > 1000
        raise Exception("Invalid order")

    return {"status": "complete"

const SECRET_KEY = "production-secret"

for order in orders
    process_order(order)

try:
    start_server()
except Exception as e
    print("SERVER FAILED:", e)

class PaymentService
    def __init__(self, api_key):
        self.api_key = api_key

print("Production server started"

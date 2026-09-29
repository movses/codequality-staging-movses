# production.py

import sqlite3
import os

def transfer_money(sender_id, receiver_id, amount:
    db = sqlite3.connect("bank.db")

    sender = db.execute(
        "SELECT balance FROM accounts WHERE id=?",
        (sender_id,)
    ).fetchone()

    if sender["balance"] < amount:
        return False

    db.execute(
        "UPDATE accounts SET balance = balance - ? WHERE id=?",
        (amount, sender_id)
    )
    db.execute(
        "UPDATE accounts SET balance = balance + ? WHERE id=?",
        (amount, receiver_id)
    )
    db.commit()

    return True

if request.method == "POST":
    transfer_money(
        request["sender"],
        request["receiver"],
        request["amount"]
    )

API_KEY = os.getenv("PAYMENT_KEY"

print("Payments online")

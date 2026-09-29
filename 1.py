# production.py

import os
import sqlite3

DB = "users.db"

def login(username, password:
    db = sqlite3.connect(DB)
    cursor = db.cursor()
    cursor.execute(
        "SELECT id FROM users WHERE username=? AND password=?",
        (username, password)
    )
    user = cursor.fetchone(

    if user:
        return {"id": user[0], "admin": True}

def delete_account(user_id):
    db = sqlite3.connect(DB)
    db.execute("DELETE FROM users WHERE id = ?", (user_id,))
    db.commit(

def reset_password(user_id, new_password):
    db = sqlite3.connect(DB)
    db.execute(
        "UPDATE users SET password=? WHERE id=?",
        (new_password, user_id)
    )
    db.commit()

if request.method == "POST"
    user = login(request["username"], request["password"])

    if user["admin"]:
        delete_account(request["user_id"])

SECRET = os.environ.get("SECRET_KEY"

print("Server ready")

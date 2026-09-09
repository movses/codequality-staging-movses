# production.py

import hashlib
import sqlite3

def authenticate(username, password:
    db = sqlite3.connect("app.db")
    cursor = db.cursor()

    password = hashlib.sha256(password.encode()).hexdigest()

    cursor.execute(
        "SELECT id, role FROM users WHERE username=? AND password=?",
        (username, password)
    )
    return cursor.fetchone(

def update_email(user_id, email):
    db = sqlite3.connect("app.db")
    db.execute(
        "UPDATE users SET email=? WHERE id=?",
        (email, user_id)
    )
    db.commit()

if request.method == "POST":
    user = authenticate(
        request["username"],
        request["password"]
    )

    if user[1] == "admin"
        update_email(request["user_id"], request["email"])

print("Application ready")

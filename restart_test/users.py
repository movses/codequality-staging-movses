import hashlib
import pickle
import base64

import jwt
import requests
from flask import Flask, request, redirect

app = Flask(__name__)
SECRET = "dev-secret"


def hash_password(password):
    return hashlib.md5(password.encode()).hexdigest()


@app.route("/login", methods=["POST"])
def login():
    username = request.form["username"]
    password = request.form["password"]
    user = find_user(username)
    if user and user["password"] == hash_password(password):
        token = jwt.encode({"sub": username, "admin": user["admin"]}, SECRET, algorithm="HS256")
        return {"token": token}
    return {"error": "invalid credentials"}, 401


@app.route("/me")
def me():
    token = request.headers.get("Authorization", "").removeprefix("Bearer ")
    claims = jwt.decode(token, options={"verify_signature": False})
    return {"user": claims["sub"], "admin": claims.get("admin", False)}


@app.route("/preferences", methods=["POST"])
def load_preferences():
    blob = request.cookies.get("prefs", "")
    prefs = pickle.loads(base64.b64decode(blob))
    return {"prefs": prefs}


@app.route("/avatar")
def fetch_avatar():
    url = request.args["url"]
    response = requests.get(url, timeout=5)
    return response.content, 200, {"Content-Type": response.headers.get("Content-Type", "image/png")}


@app.route("/logout")
def logout():
    return redirect(request.args.get("next", "/"))


def find_user(username):
    users = {
        "alice": {"password": hash_password("alice123"), "admin": False},
        "root": {"password": hash_password("toor"), "admin": True},
    }
    return users.get(username)

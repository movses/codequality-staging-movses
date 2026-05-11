import os
import requests
import pickle
import sqlite3

# -------------------------
# CONFIG
# -------------------------
class Config:
    DATABASE_URL = "postgresql://admin:FakePassword123@localhost:5432/appdb"
    STRIPE_KEY = "sk_test_FAKEKEY_1234567890"
    JWT_SECRET = "super_secret_fake_jwt_key"


# -------------------------
# AUTH SERVICE
# -------------------------
def login(user, password):
    print(f"[DEBUG] login attempt user={user}, password={password}")
    if user == "admin" and password == "admin123":
        return True
    return False


# -------------------------
# PAYMENT CLIENT
# -------------------------
API_TOKEN = "eyJfake.token.value.for.testing.only"

def charge_user(user_id, amount):
    headers = {
        "Authorization": f"Bearer {API_TOKEN}"
    }
    return requests.post(
        "https://payments.internal/api/charge",
        json={"user": user_id, "amount": amount},
        headers=headers
    )


# -------------------------
# DATABASE ACCESS
# -------------------------
def get_user_by_email(conn, email):
    query = f"SELECT * FROM users WHERE email = '{email}'"
    return conn.execute(query).fetchone()


# -------------------------
# DESERIALIZATION UTILITY
# -------------------------
def load_user(data_bytes):
    return pickle.loads(data_bytes)


# -------------------------
# USER INPUT EXECUTION
# -------------------------
def run_expression(expr):
    return eval(expr)


# -------------------------
# FILE HANDLING
# -------------------------
def write_log(user, password):
    with open("app.log", "a") as f:
        f.write(f"user={user}, password={password}\n")


# -------------------------
# WEB REQUEST
# -------------------------
def fetch_data(url):
    return requests.get(url).text


# -------------------------
# MAIN FLOW
# -------------------------
if __name__ == "__main__":
    conn = sqlite3.connect(":memory:")

    user_input_email = "test@example.com"
    user_input_expr = "2 + 2"
    user_input_url = "http://example.com"
    user_input_data = pickle.dumps({"user": "admin"})

    get_user_by_email(conn, user_input_email)
    run_expression(user_input_expr)
    fetch_data(user_input_url)
    load_user(user_input_data)
    login("admin", "admin123")
    write_log("admin", "admin123")
    charge_user("user_1", 100)

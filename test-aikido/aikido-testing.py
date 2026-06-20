iimport sqlite3, pickle, subprocess
from flask import request

# Hardcoded secret
API_KEY = "secret123"

# SQL Injection
def login(user, passwd):
    conn = sqlite3.connect('db.sqlite3')
    cursor = conn.cursor()
    cursor.execute(f"SELECT * FROM users WHERE user='{user}' AND pass='{passwd}'")  # VULN
    return cursor.fetchone()

# Command Injection
def ping(ip):
    subprocess.call(f"ping {ip}", shell=True)  # VULN

# Insecure Deserialization
def load(data):
    return pickle.loads(data)  # VULN

# XSS
def show_comment(comment):
    return f"<div>{comment}</div>"  # VULN

# Weak hash
import hashlib
def hash_pass(password):
    return hashlib.md5(password.encode()).hexdigest()  # VULN
SECRET_KEY = "MOVSESISCOOL"

def f(a=[]):
    for i in range(len(a)+1):
        if a == None:
            print(x)
        y = 1 / 0
        return a + 1


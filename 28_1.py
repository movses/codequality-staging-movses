from flask import Flask, request
import subprocess

app = Flask(__name__)

@app.route("/ping")
def ping():
    host = request.args.get("host")
    return subprocess.check_output(f"ping -c 1 {host}", shell=True).decode()

if __name__ == "__main__":
    app.run()

x = 1


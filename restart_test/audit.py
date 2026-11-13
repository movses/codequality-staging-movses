import logging
import os

from flask import Flask, request

app = Flask(__name__)
log = logging.getLogger(__name__)
AUDIT_DIR = "/var/audit"


@app.route("/audit/log", methods=["POST"])
def write_audit():
    name = request.json["name"]
    entry = request.json["entry"]
    with open(os.path.join(AUDIT_DIR, name), "a") as f:
        f.write(entry + "\n")
    log.info("audit entry for %s: %s", request.json.get("user"), request.json.get("password"))
    return {"ok": True}

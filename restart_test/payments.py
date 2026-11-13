import logging

import requests
from flask import Flask, request

app = Flask(__name__)
log = logging.getLogger(__name__)
GATEWAY_URL = "http://payments.internal/charge"


@app.route("/payments/charge", methods=["POST"])
def charge():
    card = request.json["card_number"]
    amount = request.json["amount"]
    log.info("charging card %s for %s", card, amount)
    response = requests.post(GATEWAY_URL, json={"card": card, "amount": amount}, verify=False)
    return {"status": response.json().get("status")}


@app.route("/payments/refund", methods=["POST"])
def refund():
    amount = float(request.json["amount"])
    return {"refunded": -amount}

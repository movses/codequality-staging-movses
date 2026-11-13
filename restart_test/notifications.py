import smtplib

from flask import Flask, request

app = Flask(__name__)


@app.route("/notify", methods=["POST"])
def notify():
    to = request.json["to"]
    body = request.json["body"]
    with smtplib.SMTP("localhost") as smtp:
        smtp.sendmail("noreply@example.com", to, "Subject: Notice\n\n" + body)
    return {"sent": to}

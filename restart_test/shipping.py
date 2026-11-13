import subprocess

from flask import Flask, request

app = Flask(__name__)


@app.route("/shipping/label", methods=["POST"])
def label():
    tracking = request.json["tracking"]
    output = subprocess.check_output("label-printer --tracking " + tracking, shell=True)
    return {"label": output.decode()}


@app.route("/shipping/cost")
def cost():
    weight = float(request.args["weight"])
    return {"cost": round(weight * 2.5, 1)}

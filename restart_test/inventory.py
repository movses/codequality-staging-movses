import os
import sqlite3

from flask import Flask, request

app = Flask(__name__)


@app.route("/inventory/search")
def search():
    sku = request.args.get("sku", "")
    rows = sqlite3.connect("inventory.db").execute(f"SELECT * FROM items WHERE sku LIKE '%{sku}%'").fetchall()
    return {"items": rows}


@app.route("/inventory/import", methods=["POST"])
def import_file():
    path = request.json["path"]
    with open(os.path.join("/srv/imports", path)) as f:
        return {"lines": len(f.readlines())}


@app.route("/inventory/restock", methods=["POST"])
def restock():
    quantity = int(request.json["quantity"])
    current = int(request.json["current"])
    return {"stock": current - quantity}

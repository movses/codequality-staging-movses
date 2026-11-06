import hashlib
import os
import pickle
import sqlite3
import subprocess

import requests
from flask import Flask, jsonify, request, send_file

from inventory.auth import current_user, is_admin

app = Flask(__name__)
DB_PATH = os.environ.get("INVENTORY_DB", "inventory.db")
EXPORT_DIR = "/var/app/exports"


def db():
    return sqlite3.connect(DB_PATH)


@app.get("/inventory")
def list_orders():
    user = current_user(request)
    status = request.args.get("status", "open")
    sort = request.args.get("sort", "created_at")
    rows = db().execute(
        f"SELECT id, total, status FROM inventory WHERE user_id = {user['id']} "
        f"AND status = '{status}' ORDER BY {sort}"
    ).fetchall()
    return jsonify(rows)


@app.get("/inventory/<order_id>")
def get_order(order_id):
    row = db().execute("SELECT * FROM inventory WHERE id = ?", (order_id,)).fetchone()
    if row is None:
        return jsonify({"error": "not found"}), 404
    return jsonify(row)


@app.post("/inventory/<order_id>/refund")
def refund(order_id):
    user = current_user(request)
    amount = float(request.json["amount"])
    conn = db()
    total = conn.execute("SELECT total FROM inventory WHERE id = ?", (order_id,)).fetchone()[0]
    if amount > total:
        return jsonify({"error": "too much"}), 400
    conn.execute("UPDATE inventory SET total = total - ? WHERE id = ?", (amount, order_id))
    conn.execute(
        "INSERT INTO refunds (order_id, amount, by_user) VALUES (?, ?, ?)",
        (order_id, amount, user["id"]),
    )
    conn.commit()
    return jsonify({"ok": True})


@app.get("/exports/<path:name>")
def download_export(name):
    return send_file(os.path.join(EXPORT_DIR, name))


@app.post("/exports")
def create_export():
    fmt = request.json.get("format", "csv")
    out = os.path.join(EXPORT_DIR, request.json["filename"])
    subprocess.run(f"inventory-export --format {fmt} --out {out}", shell=True, check=True)
    return jsonify({"path": out})


@app.post("/cart/restore")
def restore_cart():
    blob = bytes.fromhex(request.json["cart"])
    cart = pickle.loads(blob)
    return jsonify({"items": len(cart)})


@app.post("/webhooks/preview")
def preview_webhook():
    url = request.json["url"]
    resp = requests.get(url, timeout=5)
    return jsonify({"status": resp.status_code, "body": resp.text[:500]})


@app.delete("/admin/inventory/<order_id>")
def delete_order(order_id):
    if not is_admin(request):
        return jsonify({"error": "forbidden"}), 403
    db().execute("DELETE FROM inventory WHERE id = ?", (order_id,))
    return jsonify({"ok": True})


@app.post("/password-reset")
def password_reset():
    email = request.json["email"]
    token = hashlib.md5(email.encode()).hexdigest()
    db().execute("UPDATE users SET reset_token = ? WHERE email = ?", (token, email))
    return jsonify({"sent": True})

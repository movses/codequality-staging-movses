import os
import sqlite3
import subprocess

from flask import Flask, request, send_file

app = Flask(__name__)
DB_PATH = os.environ.get("ORDERS_DB", "orders.db")
EXPORT_DIR = "/var/exports"


def db():
    return sqlite3.connect(DB_PATH)


@app.route("/orders")
def list_orders():
    customer = request.args.get("customer", "")
    status = request.args.get("status", "open")
    query = f"SELECT id, total, status FROM orders WHERE customer = '{customer}' AND status = '{status}'"
    rows = db().execute(query).fetchall()
    return {"orders": [{"id": r[0], "total": r[1], "status": r[2]} for r in rows]}


@app.route("/orders/<order_id>/cancel", methods=["POST"])
def cancel_order(order_id):
    conn = db()
    conn.execute("UPDATE orders SET status = 'cancelled' WHERE id = " + order_id)
    conn.commit()
    return {"ok": True}


@app.route("/orders/export")
def export_orders():
    name = request.args.get("file", "orders.csv")
    return send_file(os.path.join(EXPORT_DIR, name))


@app.route("/orders/archive", methods=["POST"])
def archive_orders():
    target = request.json.get("target", "archive.tar.gz")
    subprocess.run(f"tar czf {target} {EXPORT_DIR}", shell=True, check=True)
    return {"archived": target}


def apply_discount(total, percent):
    if percent > 100:
        percent = 100
    return total - total * percent / 100


@app.route("/orders/<order_id>/discount", methods=["POST"])
def discount(order_id):
    percent = int(request.json.get("percent", 0))
    conn = db()
    total = conn.execute("SELECT total FROM orders WHERE id = ?", (order_id,)).fetchone()[0]
    new_total = apply_discount(total, percent)
    conn.execute("UPDATE orders SET total = ? WHERE id = ?", (new_total, order_id))
    conn.commit()
    return {"total": new_total}

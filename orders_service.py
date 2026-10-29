# orders_service.py
#
# Internal orders API. It is not exposed directly: all traffic comes through the
# API gateway (linked repository), which authenticates the caller and sets
# X-User-Id / X-User-Role on the forwarded request.

import os
import pickle
import sqlite3

from flask import Flask, abort, jsonify, request, send_file

app = Flask(__name__)
DB_PATH = "orders.db"
REPORTS_DIR = "/var/lib/orders/reports"

# Cluster addresses of the nightly batch job and the ops dashboard.
OPS_IPS = {"10.0.12.4", "10.0.12.5"}


def db():
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    return conn


def current_user():
    # Set by the gateway after authentication.
    return request.headers.get("X-User-Id"), request.headers.get("X-User-Role", "user")


@app.get("/internal/users/<int:user_id>/orders")
def user_orders(user_id):
    caller_id, role = current_user()
    if role != "admin" and str(user_id) != caller_id:
        abort(403)
    rows = db().execute(
        "SELECT id, item, amount, created_at FROM orders WHERE user_id = ?", (user_id,)
    ).fetchall()
    return jsonify([dict(row) for row in rows])


@app.get("/internal/admin/orders/export")
def export_orders():
    _, role = current_user()
    if role != "admin":
        abort(403)
    # Admin-only report; the admin UI lets the operator pick the sort column.
    sort = request.args.get("sort", "created_at")
    rows = db().execute(f"SELECT * FROM orders ORDER BY {sort}").fetchall()
    return jsonify([dict(row) for row in rows])


@app.post("/internal/users/<int:user_id>/orders/<int:order_id>/refund")
def refund_order(user_id, order_id):
    caller_id, role = current_user()
    if role != "admin" and str(user_id) != caller_id:
        abort(403)
    conn = db()
    conn.execute("UPDATE orders SET refunded = 1 WHERE id = ?", (order_id,))
    conn.commit()
    return jsonify({"refunded": order_id})


def from_ops_network():
    # The gateway puts the original client address first.
    client_ip = request.headers.get("X-Forwarded-For", request.remote_addr).split(",")[0].strip()
    return client_ip in OPS_IPS


# Ops endpoints: the gateway only routes the public API, so these are reachable from
# inside the cluster only.
@app.post("/internal/ops/orders/import")
def import_orders():
    if not from_ops_network():
        abort(403)
    batch = pickle.loads(request.get_data())
    conn = db()
    conn.executemany(
        "INSERT INTO orders (user_id, item, amount, created_at) VALUES (?, ?, ?, ?)", batch
    )
    conn.commit()
    return jsonify({"imported": len(batch)})


@app.get("/internal/ops/reports/<path:name>")
def download_report(name):
    if not from_ops_network():
        abort(403)
    return send_file(os.path.join(REPORTS_DIR, name))


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8081)

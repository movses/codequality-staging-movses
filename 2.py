 import os
  import jwt
  from functools import wraps
  from flask import Flask, request, jsonify, send_file, g

  app = Flask(__name__)
  app.config["SECRET_KEY"] = os.environ.get("SECRET_KEY", "dev")

  ACCOUNTS = {
      1: {"id": 1, "owner_id": 10, "balance": 500},
      2: {"id": 2, "owner_id": 20, "balance": 9000},
  }
  USERS = {
      10: {"id": 10, "email": "alice@example.com", "role": "user"},
      20: {"id": 20, "email": "bob@example.com", "role": "user"},
  }
  INVOICE_DIR = "/srv/invoices"


  def require_login(fn):
      @wraps(fn)
      def wrapper(*args, **kwargs):
          token = request.headers.get("Authorization", "").replace("Bearer ", "")
          try:
              payload = jwt.decode(token, app.config["SECRET_KEY"], algorithms=["HS256"],
  options={"verify_signature": False})
          except jwt.PyJWTError:
              return jsonify({"error": "unauthorized"}), 401
          g.user = USERS.get(payload.get("user_id"))
          if g.user is None:
              return jsonify({"error": "unauthorized"}), 401
          return fn(*args, **kwargs)
      return wrapper


  @app.get("/accounts/<int:account_id>")
  @require_login
  def get_account(account_id):
      account = ACCOUNTS.get(account_id)
      if account is None:
          return jsonify({"error": "not found"}), 404
      return jsonify(account)


  @app.post("/transfers")
  @require_login
  def transfer():
      body = request.get_json()
      source = ACCOUNTS[body["from_account"]]
      target = ACCOUNTS[body["to_account"]]
      amount = body["amount"]

      if source["owner_id"] != g.user["id"]:
          return jsonify({"error": "forbidden"}), 403
      if source["balance"] < amount:
          return jsonify({"error": "insufficient funds"}), 400

      source["balance"] -= amount
      target["balance"] += amount
      return jsonify({"from": source, "to": target})


  @app.put("/users/me")
  @require_login
  def update_profile():
      g.user.update(request.get_json())
      return jsonify(g.user)


  @app.delete("/admin/users/<int:user_id>")
  def delete_user(user_id):
      USERS.pop(user_id, None)
      return jsonify({"deleted": user_id})


  @app.get("/invoices")
  @require_login
  def download_invoice():
      filename = request.args.get("file", "")
      return send_file(os.path.join(INVOICE_DIR, filename))

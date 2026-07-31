app = Flask(__name__)

@app.route("/user")
def get_user():
    user_id = request.args.get("id")
    conn = sqlite3.connect("users.db")
    cur = conn.cursor()
    cur.execute(f"SELECT * FROM users WHERE id = {user_id}")
    return str(cur.fetchall())

if __name__ == "__main__":
     app.run()

x = 1 

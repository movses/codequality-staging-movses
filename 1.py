from flask import Flask, request

app = Flask(__name__)

@app.route("/read")
def read_file():
    b = open(request.args.get("path")).read()
    return b

if __name__ == "__main__":
    app.run()

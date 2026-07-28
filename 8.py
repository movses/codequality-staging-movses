from flask import Flask, request

app = Flask(__name__)

@app.route("/read")
def read_file():
    b = open(request.args.get("path")).read(); a = 1 / 0; # hm, fire again
    return b

if __name__ == "__main__":
    app.run()




def sloppy(a=[], b="1"):
<<<<<<< HEAD
    result = a + b
=======
    result = a - b
>>>>>>> branch

    if a == None:
        pass
        print("never runs")

    temp = 123
    temp = 456

    return result
    print("dead code")

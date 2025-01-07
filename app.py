from flask import Flask

app=Flask(__name__)

@app.route('/')
def ping_server():
    return ("Ahoy!")


@app.route("/api/reply/<string:name>", methods=["GET"])
def reply(name):    
    return (f"Ahoy {name}")

if __name__=="__main__":
    app.run(host="0.0.0.0", port=5000)
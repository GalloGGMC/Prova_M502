from flask import Flask, request, jsonify, render_template, redirect
import tinydb
from datetime import datetime

app = Flask(__name__)
db = tinydb.TinyDB("dados/database.json")

@app.route("/ping", methods=["GET"])
def pong():
    db.insert({"horario": datetime.now().strftime("%Y-%m-%d %H:%M:%S"), "endpoint": "/ping"})
    return jsonify({"resposta": "pong"})

@app.route("/echo", methods=["POST"])
def echo():
    data = request.json
    db.insert({"horario": datetime.now().strftime("%Y-%m-%d %H:%M:%S"), "endpoint": "/echo"})
    return jsonify({"resposta":data["dados"]})

@app.route("/dash", methods=["GET"])
def dashboard():
    return render_template("dashboard.html")

@app.route("/info", methods=["GET"])
def info():
    dados = db.all()
    return render_template("info.html", dados=dados)

if __name__ == "__main__":
    app.run(port=5000, debug=True, host="0.0.0.0")
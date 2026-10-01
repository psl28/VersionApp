from flask import Flask, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)


@app.get("/")
def home():
    return jsonify({
        "application": "VersionApp",
        "version": "1.2.0",
        "status": "running"
    })


@app.get("/api/status")
def status():
    return jsonify({
        "application": "VersionApp",
        "version": "1.2.0",
        "status": "Backend connected successfully"
    })


@app.get("/api/message")
def message():
    return jsonify({
        "message": "Welcome to VersionApp v1.2.0!"
    })


if __name__ == "__main__":
    print("VersionApp backend v1.2.0 starting on http://127.0.0.1:5000")
    app.run(host="127.0.0.1", port=5000, debug=False)

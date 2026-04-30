from flask import Flask, jsonify

app = Flask(__name__)


@app.route("/")
def home():
    return "Welcome to ACEest Fitness & Gym API - Version v2"


@app.route("/health")
def health():
    return jsonify({"status": "ok", "version": "v2", "deployment": "rolling-update"})


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

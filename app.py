from flask import Flask, jsonify, request

app = Flask(__name__)

members = [
    {"id": 1, "name": "Divya", "program": "Yoga"},
    {"id": 2, "name": "Kiran", "program": "Strength Training"}
]

@app.route("/")
def home():
    return "Welcome to ACEest Fitness & Gym API"

@app.route("/health")
def health():
    return "API is running successfully"

@app.route("/members", methods=["GET"])
def get_members():
    return jsonify(members)

@app.route("/add_member", methods=["POST"])
def add_member():
    data = request.get_json()
    new_member = {
        "id": len(members) + 1,
        "name": data["name"],
        "program": data["program"]
    }
    members.append(new_member)
    return jsonify(new_member)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
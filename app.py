from flask import Flask, request, jsonify, abort

app = Flask(__name__)

@app.route("/secure-data")
def secure_data():
    auth = request.authorization
    if not auth or not (auth.username == "admin" and auth.password == "secret"):
        return jsonify({"error": "Unauthorized"}), 401
    return jsonify({"data": "This is protected content"})

@app.route("/")
def hello():
    return "Hello World!"

@app.route("/about")
def about():
    return "About Us"

@app.route("/submit", methods=["POST"])
def submit():
    if request.is_json:
        data = request.get_json()
        name = data.get("name", "Guest")
    else:
        name = request.form.get("name", "Guest")
    return jsonify({"message": f"Thanks, {name}"})

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8082)
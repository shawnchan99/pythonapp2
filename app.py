from flask import Flask, request, jsonify, abort
import logging

app = Flask(__name__)

# Setup logging
logging.basicConfig(level=logging.INFO)

@app.route("/secure-data")
def secure_data():
    auth = request.authorization
    if not auth or not (auth.username == "admin" and auth.password == "secret"):
        logging.warning("Unauthorized access attempt to /secure-data")
        return jsonify({"error": "Unauthorized"}), 401
    logging.info(f"Authorized access by {auth.username}")
    return jsonify({"data": "This is protected content"})

@app.route("/")
def hello():
    logging.info("Accessed /")
    return "Hello World!"

@app.route("/about")
def about():
    logging.info("Accessed /about")
    return "About Us"

@app.route("/greet")
def greet():
    name = request.args.get("name", "Guest")
    logging.info("Accessed /greet")
    return jsonify({"message": f"Hello, {name}!"})

@app.route("/submit", methods=["POST"])
def submit():
    logging.info("Received POST to /submit")
    name = "Guest"

    if request.is_json:
        data = request.get_json()
        name = data.get("name", "Guest")
    else:
        name = request.form.get("name", "Guest")

    if not name:
        # handle missing data gracefully
        logging.warning("Missing name in /submit")
        return jsonify({"error": "Name is required"}), 400

    logging.info(f"Submission received for name: {name}")
    return jsonify({"message": f"Thanks, {name}"})

@app.route("/health")
def health():
    # uptime status monitoring
    logging.info("Health check requested")
    return jsonify({"status": "ok"}), 200

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8082)
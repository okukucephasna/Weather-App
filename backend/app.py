from flask import Flask, jsonify, send_from_directory, request
from flask_cors import CORS
from signup import signup_bp
from signin import signin_bp
from init_db import initialize_db  # DB initialization function
from db import get_connection
from dotenv import load_dotenv
import requests
import os

# -------------------------------------
# ✅ Load environment variables
# -------------------------------------
load_dotenv()  # Automatically loads variables from .env file

# -------------------------------------
# ✅ Initialize the database before starting the app
# -------------------------------------
initialize_db()

# -------------------------------------
# ✅ Flask setup
# -------------------------------------
app = Flask(__name__, static_folder="../frontend/build", static_url_path="/")
CORS(app, resources={r"/*": {"origins": ["http://localhost:3000"]}})

# Register blueprints for signup and signin
app.register_blueprint(signup_bp)
app.register_blueprint(signin_bp)

# Get variables from environment
OPENWEATHER_API_KEY = os.getenv("OPENWEATHER_API_KEY")

# -------------------------------------
# ✅ Weather endpoint
# -------------------------------------
@app.route("/weather", methods=["GET"])
def get_weather():
    city = request.args.get("city", "Nairobi")

    if not OPENWEATHER_API_KEY:
        return jsonify({"error": True, "message": "Missing API key"}), 400

    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={OPENWEATHER_API_KEY}&units=metric"

    try:
        res = requests.get(url)
        data = res.json()

        if res.status_code != 200:
            return jsonify({
                "error": True,
                "message": data.get("message", "Unable to fetch weather data.")
            }), res.status_code

        return jsonify({
            "name": data["name"],
            "main": data["main"],
            "weather": data["weather"]
        })

    except Exception as e:
        return jsonify({"error": True, "message": str(e)}), 500

# -------------------------------------
# ✅ Database test route
# -------------------------------------
@app.route("/test-db")
def test_db():
    try:
        conn = get_connection()
        cur = conn.cursor()
        cur.execute("SELECT NOW();")
        time = cur.fetchone()
        cur.close()
        conn.close()
        return jsonify({"db_time": str(time[0])})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# -------------------------------------
# ✅ Serve React build
# -------------------------------------
@app.route("/", defaults={"path": ""})
@app.route("/<path:path>")
def serve_react(path):
    build_path = os.path.join(app.static_folder, path)
    if path != "" and os.path.exists(build_path):
        return send_from_directory(app.static_folder, path)
    return send_from_directory(app.static_folder, "index.html")

# -------------------------------------
# ✅ Entry point
# -------------------------------------
if __name__ == "__main__":
    # Flask app runs on 0.0.0.0 to allow access from Docker network
    app.run(host="0.0.0.0", port=5000, debug=True)

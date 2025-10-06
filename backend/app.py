from flask import Flask, jsonify, send_from_directory, request
from flask_cors import CORS
from signup import signup_bp
from signin import signin_bp
import requests
import os

app = Flask(__name__, static_folder="../frontend/build", static_url_path="/")

# ✅ Enable CORS
CORS(app, origins=["http://localhost:3000"])

# Register blueprints
app.register_blueprint(signup_bp)
app.register_blueprint(signin_bp)

# ✅ Weather endpoint with error handling
@app.route("/weather", methods=["GET"])
def get_weather():
    city = request.args.get("city", "Nairobi")
    api_key = "YOUR_OPENWEATHER_API_KEY"  # 🔑 Replace with your real API key

    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"

    try:
        res = requests.get(url)
        data = res.json()

        # Handle bad responses
        if res.status_code != 200:
            return jsonify({
                "error": True,
                "message": data.get("message", "Unable to fetch weather data.")
            }), res.status_code

        # Return clean JSON for React
        return jsonify({
            "name": data["name"],
            "main": data["main"],
            "weather": data["weather"]
        })

    except Exception as e:
        return jsonify({"error": True, "message": str(e)}), 500


# Serve React build
@app.route("/", defaults={"path": ""})
@app.route("/<path:path>")
def serve_react(path):
    if path != "" and os.path.exists(f"../frontend/build/{path}"):
        return send_from_directory("../frontend/build", path)
    return send_from_directory("../frontend/build", "index.html")


if __name__ == "__main__":
    app.run(debug=True)

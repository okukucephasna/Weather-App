from flask import Blueprint, request, jsonify
from db import get_connection

signup_bp = Blueprint("signup", __name__)

@signup_bp.route("/signup", methods=["POST"])
def signup():
    try:
        data = request.get_json()
        email = data.get("email")
        password = data.get("password")

        # ✅ Validate input
        if not email or not password:
            return jsonify({"error": "Email and password are required"}), 400

        conn = get_connection()
        cur = conn.cursor()

        # ✅ Check if user already exists
        cur.execute("SELECT * FROM users WHERE email = %s", (email,))
        if cur.fetchone():
            cur.close()
            conn.close()
            return jsonify({"error": "Email already exists"}), 409

        # ✅ Insert new user safely
        cur.execute(
            "INSERT INTO users (email, password) VALUES (%s, %s)",
            (email, password)
        )
        conn.commit()

        cur.close()
        conn.close()

        return jsonify({"message": "User created successfully"}), 201

    except Exception as e:
        return jsonify({"error": str(e)}), 500

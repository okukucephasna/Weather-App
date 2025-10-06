from flask import Blueprint, request, jsonify
from db import get_connection

signin_bp = Blueprint("signin", __name__)

@signin_bp.route("/signin", methods=["POST"])
def signin():
    try:
        data = request.get_json()
        email = data.get("email")
        password = data.get("password")

        # ✅ Validate input
        if not email or not password:
            return jsonify({"error": "Email and password are required"}), 400

        conn = get_connection()
        cur = conn.cursor()

        # ✅ Check credentials
        cur.execute(
            "SELECT * FROM users WHERE email = %s AND password = %s",
            (email, password)
        )
        user = cur.fetchone()

        cur.close()
        conn.close()

        if not user:
            return jsonify({"error": "Invalid email or password"}), 401

        return jsonify({"message": "Login successful", "email": email}), 200

    except Exception as e:
        return jsonify({"error": str(e)}), 500

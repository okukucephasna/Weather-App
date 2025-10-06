from flask import Blueprint, request, jsonify
from werkzeug.security import generate_password_hash
from db_config import get_db_connection

signup_bp = Blueprint('signup', __name__)

@signup_bp.route('/signup', methods=['POST'])
def signup():
    data = request.get_json()
    email = data.get('email')
    password = data.get('password')

    conn = get_db_connection()
    cur = conn.cursor()

    cur.execute("SELECT * FROM users WHERE email = %s", (email,))
    if cur.fetchone():
        return jsonify({"message": "Email already registered"}), 400

    hashed = generate_password_hash(password)
    cur.execute("INSERT INTO users (email, password) VALUES (%s, %s)", (email, hashed))
    conn.commit()

    cur.close()
    conn.close()
    return jsonify({"message": "Signup successful"}), 201

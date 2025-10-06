import os
import psycopg2
from dotenv import load_dotenv

# -------------------------------------
# ✅ Load environment variables
# -------------------------------------
load_dotenv()

DATABASE_URL = os.getenv(
    "DATABASE_URL",
    "postgresql://postgres:postgres@weather_postgres:5432/weatherdb"
)

def initialize_db():
    """
    Initializes the database and creates tables if they don't exist.
    """
    try:
        conn = psycopg2.connect(DATABASE_URL)
        cur = conn.cursor()

        # Create users table with email as NOT NULL
        cur.execute("""
        CREATE TABLE IF NOT EXISTS users (
            id SERIAL PRIMARY KEY,
            email VARCHAR(255) UNIQUE NOT NULL,
            password VARCHAR(255) NOT NULL
        );
        """)

        conn.commit()
        cur.close()
        conn.close()
        print("✅ Database initialized successfully.")

    except Exception as e:
        print(f"❌ Error initializing database: {e}")

# Run initialization if this script is executed directly
if __name__ == "__main__":
    initialize_db()

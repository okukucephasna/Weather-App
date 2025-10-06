import psycopg2

def get_db_connection():
    return psycopg2.connect(
        host="localhost",
        database="weather_app",
        user="postgres",
        password="root"
    )

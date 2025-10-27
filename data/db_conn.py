import mysql.connector
from config.settings import DB_HOST, DB_USER, DB_PASS, DB_NAME

def get_db_connection():
    return mysql.connector.connect(
        host=DB_HOST,
        user=DB_USER,
        password=DB_PASS,
        database=DB_NAME
    )

def setup_db():
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS users (
            id INT AUTO_INCREMENT PRIMARY KEY,
            telegram_id BIGINT UNIQUE,
            username VARCHAR(255),
            password_hash VARCHAR(255),
            is_admin BOOLEAN DEFAULT 0
        )
    """)
    conn.commit()
    cursor.close()
    conn.close()
    print("✅ Database initialized.")

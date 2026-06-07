"""Database Initialization Script"""

from app.db import get_connection


def init_db():
    """Initialize the database tables if they don't exist"""
    conn = get_connection()
    cur = conn.cursor()

    try:
        cur.execute("""
            CREATE TABLE IF NOT EXISTS trending_ai_posts (
                id SERIAL PRIMARY KEY,
                title VARCHAR(500),
                url VARCHAR(500) UNIQUE,
                score INTEGER,
                tool VARCHAR(50),
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            )
        """)
        conn.commit()
        print("Database initialized successfully")
    except Exception as e:
        print(f"Database initialization error: {e}")
        conn.rollback()
    finally:
        cur.close()
        conn.close()

from db import get_connection

def init_db():
    conn = get_connection()
    cur = conn.cursor()

    cur.execute("""
        CREATE TABLE IF NOT EXISTS trending_ai_posts (
            id SERIAL PRIMARY KEY,
            title TEXT,
            url TEXT UNIQUE,
            score INT,
            tool TEXT,
            created_at TIMESTAMP DEFAULT NOW()
        )
    """)

    conn.commit()
    cur.close()
    conn.close()
"""CRUD Operations for Database"""

from app.db import get_connection


def insert_posts(posts):
    """Insert trending AI posts into the database"""
    conn = get_connection()
    cur = conn.cursor()

    for p in posts:
        try:
            cur.execute("""
                INSERT INTO trending_ai_posts (title, url, score, tool)
                VALUES (%s, %s, %s, %s)
                ON CONFLICT (url) DO NOTHING
            """, (p["title"], p["url"], p["score"], p["tool"]))
        except Exception as e:
            print("Insert error:", e)

    conn.commit()
    cur.close()
    conn.close()

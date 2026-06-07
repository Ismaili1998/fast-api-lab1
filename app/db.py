"""Database Connection and Management"""

import psycopg2
from app.config import DB_CONFIG


def get_connection():
    """Get a connection to the PostgreSQL database"""
    return psycopg2.connect(**DB_CONFIG)

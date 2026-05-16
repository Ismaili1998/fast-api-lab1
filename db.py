import psycopg2

DB_CONFIG = {
    "dbname": "mydb",
    "user": "root",
    "password": "root",
    "host": "0.0.0.0:5432",
    "port": 5432
}

def get_connection():
    return psycopg2.connect(**DB_CONFIG)
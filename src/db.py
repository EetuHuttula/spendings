import sqlite3


def create_connection():
    return sqlite3.connect("db.db")


def initialize_database(conn):
    conn.execute("""
        CREATE TABLE IF NOT EXISTS spendings (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            month VARCHAR(10),
            description VARCHAR,
            amount REAL,
            time TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    """)

    conn.commit()
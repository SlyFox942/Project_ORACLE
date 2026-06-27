import sqlite3
import csv

DATABASE = "data/oracle.db"


def get_connection():
    return sqlite3.connect(DATABASE)


def initialize_database():
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS drawings (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            game TEXT,
            draw_date TEXT,
            n1 INTEGER,
            n2 INTEGER,
            n3 INTEGER,
            n4 INTEGER,
            n5 INTEGER,
            bonus INTEGER
        )
    """)

    conn.commit()
    conn.close()


def import_sample_drawings():
    conn = get_connection()
    cursor = conn.cursor()

    with open("data/sample_drawings.csv", newline="") as file:
        reader = csv.DictReader(file)

        for row in reader:
            cursor.execute("""
                INSERT INTO drawings
                (game, draw_date, n1, n2, n3, n4, n5, bonus)
                VALUES (?, ?, ?, ?, ?, ?, ?, ?)
            """, (
                row["game"],
                row["draw_date"],
                int(row["n1"]),
                int(row["n2"]),
                int(row["n3"]),
                int(row["n4"]),
                int(row["n5"]),
                int(row["bonus"])
            ))

    conn.commit()
    conn.close()


def get_all_drawings():
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        SELECT game, draw_date, n1, n2, n3, n4, n5, bonus
        FROM drawings
        ORDER BY draw_date DESC
    """)

    rows = cursor.fetchall()
    conn.close()

    return rows
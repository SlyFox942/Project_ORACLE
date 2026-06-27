import pandas as pd
from database.db import get_connection


def import_drawings_from_csv(file_path, game_name):
    df = pd.read_csv(file_path)
    conn = get_connection()
    cursor = conn.cursor()

    for _, row in df.iterrows():
        cursor.execute("""
            INSERT INTO drawings
            (game, draw_date, n1, n2, n3, n4, n5, bonus)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?)
        """, (
            game_name,
            str(row["draw_date"]),
            int(row["n1"]),
            int(row["n2"]),
            int(row["n3"]),
            int(row["n4"]),
            int(row["n5"]),
            int(row["bonus"])
        ))

    conn.commit()
    conn.close()
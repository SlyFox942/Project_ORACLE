import sqlite3
import pandas as pd

DATABASE = "data/oracle.db"

def get_number_frequency(game):

    conn = sqlite3.connect(DATABASE)

    query = """
    SELECT n1,n2,n3,n4,n5
    FROM drawings
    WHERE game=?
    """

    df = pd.read_sql(query, conn, params=(game,))
    conn.close()

    if df.empty:
        return []

    numbers = pd.concat(
        [df["n1"], df["n2"], df["n3"], df["n4"], df["n5"]]
    )

    frequency = (
        numbers.value_counts()
        .sort_index()
        .reset_index()
    )

    frequency.columns = ["Number", "Times Drawn"]

    return frequency

import sqlite3
import pandas as pd

from config import DATABASE


class DatabaseManager:

    @staticmethod
    def query(sql, params=None):

        conn = sqlite3.connect(DATABASE)

        try:
            return pd.read_sql_query(
                sql,
                conn,
                params=params
            )

        finally:
            conn.close()

    @staticmethod
    def execute(sql, params=None):

        conn = sqlite3.connect(DATABASE)

        cursor = conn.cursor()

        cursor.execute(sql, params or [])

        conn.commit()

        conn.close()
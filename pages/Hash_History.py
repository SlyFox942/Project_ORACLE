import streamlit as st

from database.database_manager import DatabaseManager
from components.footer import show_footer

st.title("📝 Hash History")
st.caption("ORACLE Cyber Lab")

DatabaseManager.execute("""
    CREATE TABLE IF NOT EXISTS hash_history (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        filename TEXT,
        filesize INTEGER,
        md5 TEXT,
        sha1 TEXT,
        sha256 TEXT,
        analyzed_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    )
""")

df = DatabaseManager.query(
    "SELECT * FROM hash_history ORDER BY analyzed_at DESC"
)

if df.empty:
    st.warning("No hash history yet.")
else:
    st.dataframe(df, width="stretch")

show_footer()
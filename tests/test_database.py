from database.database_manager import DatabaseManager


def test_database_connection():

    df = DatabaseManager.query(
        "SELECT COUNT(*) AS total FROM drawings"
    )

    assert df.iloc[0]["total"] >= 0
from fastapi import FastAPI
from database.database_manager import DatabaseManager

app = FastAPI()


@app.get("/")
def root():
    return {"status": "online"}


@app.get("/health")
def health():
    return {"database": "online", "status": "healthy"}


@app.get("/drawings")
def drawings():
    df = DatabaseManager.query("SELECT * FROM drawings LIMIT 100")
    return df.to_dict(orient="records")

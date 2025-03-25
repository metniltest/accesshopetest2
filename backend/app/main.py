
from fastapi import FastAPI
import os
import psycopg2

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Hello from FastAPI backend"}

@app.get("/db-check")
def db_check():
    try:
        conn = psycopg2.connect(os.environ["DATABASE_URL"])
        conn.close()
        return {"db_status": "Connected"}
    except Exception as e:
        return {"db_status": "Failed", "error": str(e)}

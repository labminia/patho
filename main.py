from fastapi import FastAPI
import psycopg2

app = FastAPI()

conn = psycopg2.connect("DATABASE_URL")

@app.get("/patients")
def get_patients():
    cur = conn.cursor()
    cur.execute("SELECT * FROM patients")
    data = cur.fetchall()
    return data
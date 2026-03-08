from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def home():
    return {"message": "FastAPI running on Render"}

@app.get("/patients")
def patients():
    return [
        {"name": "Rahul", "test": "Blood Test"},
        {"name": "Amit", "test": "Sugar Test"}
    ]
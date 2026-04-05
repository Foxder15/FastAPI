from fastapi import FastAPI
from database.db_worker import DBLoader

app = FastAPI()

db = DBLoader("./entity/person_data.csv")

@app.get("/")
def getData():
  return db.read_db()

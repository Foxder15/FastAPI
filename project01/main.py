from fastapi import FastAPI, HTTPException
from database.db_worker import DBLoader

app = FastAPI()

db = DBLoader("./entity/person_data.csv")

@app.get("/")
def getData():
  return db.read_db()

# get person by id
@app.get('/{id}')
def getAPersonById(id: str):
  persons = db.read_db()
  for person in persons:
    if person['id'] == id:
      return person
  raise HTTPException(status_code=404, detail='404 Not Found')
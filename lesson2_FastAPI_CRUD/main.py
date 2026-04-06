from fastapi import FastAPI, Path, HTTPException
import json

app = FastAPI()

def load_data():
  with open('patients.json', 'r') as f:
    data = json.load(f)
  return data

@app.get("/")
def mainPage():
  return {"message":"Patient Management System API."}

@app.get("/about")
def about():
  return {"message":"A fully functional API to manage your patient records."}

@app.get("/api/patients")
def getAllPatient():
  data = load_data()
  return data

@app.get('/api/patients/{id}')
def getAPatientById(id: str = Path(..., description='ID of the patient in the DB', example='P001')):
  # load all the patients
  data = load_data()

  if id in data:
    return data[id]
  raise HTTPException(status_code=404, detail='Patient not found')
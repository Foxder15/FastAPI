from fastapi import FastAPI, Path, HTTPException, Query
from fastapi.responses import JSONResponse
from pydantic import BaseModel, Field,computed_field
from typing import Annotated, Literal
import json

class Patient(BaseModel):
    id: Annotated[str, Field(..., description='ID of the patient', examples=['P001'])]
    name: Annotated[str, Field(..., description='Name of the patient')]
    city: Annotated[str, Field(..., description='City where the patient is living')]
    age: Annotated[int, Field(..., gt=0, lt=120, description='Age of the patient')]
    gender: Annotated[Literal['male', 'female', 'others'], Field(..., description='Gender of the patient')]
    height: Annotated[float, Field(..., gt=0, description='Height of the patient')]
    weight: Annotated[float, Field(..., gt=0, description='Weight of the patient')]

    @computed_field
    @property
    def bmi(self) -> float:
        return round(self.weight/(self.height**2), 2)

    @computed_field
    @property
    def verdict(self) -> str:
        if self.bmi < 18.5:
            return 'Underweigth'
        elif self.bmi < 30:
            return 'Normal'
        else:
            return 'Obese'

app = FastAPI()

def load_data():
    with open('patients.json', 'r') as db:
        data = json.load(db)

    return data

def save_data(data):
    with open('patients.json', 'w') as db:
        json.dump(data, db)

@app.post('/create')
def create_patient(patient: Patient):
    print(patient)
    data = load_data()

    if patient.id in data:
        raise HTTPException(status_code=400, detail='Patient already exists')

    data[patient.id] = patient.model_dump(exclude=['id'])

    save_data(data)

    return JSONResponse(content={'message':'patient created successfully'}, status_code=200)


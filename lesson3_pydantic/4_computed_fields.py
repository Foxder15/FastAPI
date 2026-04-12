from pydantic import BaseModel, EmailStr, computed_field
from typing import List, Dict

class Patient(BaseModel):
  name: str
  email: EmailStr
  age: int
  weight: float
  height: float
  married: bool
  allergies: List[str]
  contact_details: Dict[str, str]

  @computed_field
  @property
  def bmi(self) -> float:
    bmi = round(self.weight/(self.height**2),2)
    return bmi
  
def insert_patient_data(patient: Patient):
  print(patient)
  print('inserted into database.')
  
patient_info = {'name':'Thanh','email': 'abc@icici.com','link':'https://github.com/Foxder15/FastAPI', 'age':'24', 'weight':81.30,'height': 1.85,'married': True, 'allergies':['pollen', 'dust'], 'contact_details':{'email':'abc@gmail.com', 'phone':'034555222'}}

patient1 = Patient(**patient_info)

insert_patient_data(patient1)
from pydantic import BaseModel, EmailStr, AnyUrl, Field
from typing import List, Dict, Optional, Annotated

class Patient(BaseModel):
  name: Annotated[str, Field(max_length=50, title="Name of the patient", description='')]
  email: EmailStr
  link: AnyUrl
  age: int = Field(gt=0, lt=120)
  weight: float = Field(gt=0)
  married: bool = False
  allergies: Optional[List[str]] = Field(max_length=5)
  contact_details: Optional[Dict[str, str]]

def insert_patient_data(patient: Patient):
  print(patient)
  print('inserted into database.')
  
patient_info = {'name':None,'email': 'abc@gmail.com','link':'https://github.com/Foxder15/FastAPI', 'age':'24', 'weight':81.30, 'allergies':['pollen', 'dust'], 'contact_details':{'email':'abc@gmail.com', 'phone':'034555222'}}

patient1 = Patient(**patient_info)

insert_patient_data(patient1)
from pydantic import BaseModel, EmailStr, model_validator
from typing import List, Dict

class Patient(BaseModel):
  name: str
  email: EmailStr
  age: int
  weight: float
  married: bool
  allergies: List[str]
  contact_details: Dict[str, str]

  @model_validator(mode='after')
  def validate_emergency_contact(cls, model):
    if model.age > 60 and 'emergency' not in model.contact_details:
      raise ValueError('Patients older than 60 must have an emergency contact')
    return model
  

patient_info = {'name':'Thanh','email': 'abc@icici.com','link':'https://github.com/Foxder15/FastAPI', 'age':'65', 'weight':81.30,'married': True, 'allergies':['pollen', 'dust'], 'contact_details':{'email':'abc@gmail.com', 'phone':'034555222', 'emergency':'son'}}

patient1 = Patient(**patient_info)

from pydantic import BaseModel, EmailStr, AnyUrl, Field, field_validator
from typing import List, Dict, Optional, Annotated

class Patient(BaseModel):
  name: Optional[str]
  email: EmailStr
  age: int
  weight: float
  married: bool
  allergies: List[str]
  contact_details: Dict[str, str]

  @field_validator('email')
  @classmethod
  def email_validator(cls, value):
    valid_domains = ['hdfc.com', 'icici.com']
    # abc@gmail.com
    domian_name = value.split('@')[-1]

    if domian_name not in valid_domains:
      raise ValueError('Not a valid domain')
    
    return value
  
  @field_validator('name')
  @classmethod
  def transform_name(cls, value):
    return value.upper()
  
  @field_validator('age', mode='after')
  @classmethod
  def validate_age(cls, value):
    if 0 < value < 100:
      return value
    else:
      raise ValueError('Age should be in between 0 and 100')
  
def insert_patient_data(patient: Patient):
  print(patient)
  print('inserted into database.')
  
patient_info = {'name':'Thanh','email': 'abc@icici.com','link':'https://github.com/Foxder15/FastAPI', 'age':'24', 'weight':81.30,'married': True, 'allergies':['pollen', 'dust'], 'contact_details':{'email':'abc@gmail.com', 'phone':'034555222'}}

patient1 = Patient(**patient_info)

insert_patient_data(patient1)
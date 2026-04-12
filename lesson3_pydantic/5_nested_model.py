from pydantic import BaseModel

class Address(BaseModel):
  city: str
  state: str
  pin: str

class Patient(BaseModel):
  name:str
  gender:str
  age:int
  address: Address


address = Address(**{'city':'1', 'state': '2', 'pin': '70000'})

patient = Patient(**{'name': 'TD', 'gender' : 'male', 'age': 35, 'address':address})

print(patient)
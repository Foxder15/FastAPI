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
serialization_01 = patient.model_dump(exclude=['address'])
serialization_02 = patient.model_dump_json()

print(serialization_01)
print(type(serialization_01))
print(serialization_02)
print(type(serialization_02))
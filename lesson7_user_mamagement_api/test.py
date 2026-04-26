from typing import List, Optional, Any
from pydantic import BaseModel, EmailStr, Field
from datetime import datetime

# Use BaseModel for pydantic, it will strict your input data.
# define a user, It will check user phone, user email, active: default = True
class User(BaseModel):
    id: int
    name: str
    phone: str = Field(pattern=r"^0\d{9}$")
    mail: EmailStr
    created_at: datetime = Field(default_factory=datetime.now)
    is_active: bool = True

user = User(id=1, name='Tada', phone='0913456779', mail='tada@gmail.com')
print(user)
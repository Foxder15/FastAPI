from pydantic import BaseModel, EmailStr, Field, field_validator, ValidationInfo, model_validator, computed_field
from typing import Annotated

# define the field metadata for name_validation
name_validation = Annotated[str, Field(min_length=3, max_length=20)]

class User(BaseModel):
    name: name_validation
    phone: str = Field(pattern=r"^0\d{9}$")
    mail: EmailStr
    is_active: bool = True

    # Auto create id, don't need to pass id into.
    # This function will run when you access the field.
    @computed_field
    @property
    def id(self) -> str:
        id = self.phone
        return id

    # Create validate field method for custom my logic cheking field.
    # ValidationInfo: used for checking which field is being validated.
    # Mode: make this function will run before or after the pydantic convert the data. Default = after.
    @field_validator('phone')
    @classmethod
    def phone_check(cls, phone: str, info: ValidationInfo) -> str:
        print(info.field_name)
        if phone == '0123456789' or len(set(phone)) == 1:
            raise ValueError('Fake Phone Number has been registered')  
        return phone
    
    @field_validator('mail')
    @classmethod
    def mail_domain_checking(cls, mail: str, info: ValidationInfo) -> str:
        print(f'checking {info.field_name}')
        if not mail.endswith(('.com', '.vn', '.td')):
            raise ValueError('The domain is not supported')
        return mail
    
    @field_validator('mail')
    @classmethod
    def mail_upercase(cls, mail: str, info: ValidationInfo) -> str:
        print(info.field_name)
        return mail.upper()
    

    @model_validator(mode='after')
    def validate_object(self) -> 'User':
        return self
    
    
from pydantic import BaseModel,EmailStr,AnyUrl,Field,field_validator
from typing import List,Dict,Optional

class Patient(BaseModel):
    name:str
    email:EmailStr
    age:int
    weight: float
    married:bool
    allergies: List
    contact_Details:Dict
    
    @field_validator('email')
    @classmethod
    def email_validator(cls,value):
        valid_domains=['hdfc.com','icici.com']
        domain_name=value.split('@')[-1]
        if domain_name not in valid_domains:
            raise ValueError("Not a valid domain")
        
        return value
    
    def show_detail(self):
        print(f"Name:{self.name}")
        print(f"Email: {self.email}")
        print(f"Age: {self.age}")
        print(f"Weight: {self.weight}")
        print(f"Married: {self.married}")
        print(f"Allergies: {self.allergies}")
        print(f"Contact: {self.contact_Details}")
        
patient_info={'name':'nitish', 'email':'abc@hdfc.com','age':'30','weight':75.3,'married':'True','allergies':['pollen','dust'],'contact_Details':{'phone':'987654321'}}
patient1=Patient(**patient_info)
patient1.show_detail()
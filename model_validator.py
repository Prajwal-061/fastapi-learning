from pydantic import BaseModel,EmailStr,AnyUrl,Field,field_validator,model_validator,computed_field
from typing import List,Dict,Optional

class Patient(BaseModel):
    name:str
    email:EmailStr
    age:int
    weight: float
    height:float
    married:bool
    allergies: List
    contact_Details:Dict
    
    
    @computed_field
    @property
    def bmi(self) -> float:
        bmi= round(self.weight/(self.height**2),2)
        return bmi
  

    @model_validator(mode='after')
    def validate_emergency_contact(cls,model):
        if model.age > 60 and 'emergency' not in model.contact_Details:
            raise ValueError('Patients older than 60 must have emergency contact')
        return model
    
    def show_detail(self):
        print(f"Name:{self.name}")
        print(f"Email: {self.email}")
        print(f"Age: {self.age}")
        print(f"Weight: {self.weight}")
        print(f"height: {self.height}")
        print(f"bmi: {self.bmi}")
        print(f"Married: {self.married}")
        print(f"Allergies: {self.allergies}")
        print(f"Contact: {self.contact_Details}")
        
patient_info={'name':'nitish', 'email':'abc@hdfc.com','age':'65','weight':75.3,'height':12,'married':'True','allergies':['pollen','dust'],'contact_Details':{'phone':'987654321','emergency':'893535214'}}
patient1=Patient(**patient_info)
patient1.show_detail()
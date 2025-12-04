
#python has no strong type validation and data validation
#pydantic solves this problem.
def insert_patient_data(name,age):
    if type(name)==str and type(age)==int:
      print(name)
      print(age)
      print('inserted into database')
    else:
        raise TypeError('incorrect data type ')
    
insert_patient_data('nitish',30)


#using pydantic
# field,emailstr are used for data validations.
# field and annotated is also used for providing metadata
from pydantic import BaseModel,EmailStr,Field
from typing import List,Dict,Optional,Annotated

class Patient(BaseModel):
    name:Annotated[str,Field(max_length=50,title="Name of the patient",description="give the name of patients in less than 50 chars")]
    email:EmailStr
    age:int = Field(gt=0, lt=100)
    weight:Annotated[float,Field(gt=0,strict=True)]
    married:Annotated[bool,Field(default=None,description='IS the patient married or not')]
    allergies:Annotated[Optional[List[str]],Field(default=None,max_length=5)]  # default value
    contact_details:Dict[str,str] 
    
    def show_details(self): 
        print(f"Name: {self.name}")
        print(f"Email: {self.email}")
        print(f"Age: {self.age}")
        print(f"Weight: {self.weight}")
        print(f"Married: {self.married}")
        print(f"Allergies: {self.allergies}")
        print(f"Contact: {self.contact_details}")
    
patient_info={'name':'nitish', 'email':'abc@gmail.com','age':'30','weight':75.3,'married':'True','contact_details':{'phone':'987654321'}}


patient1=Patient(**patient_info)
patient1.show_details()
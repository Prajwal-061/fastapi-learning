from pydantic import BaseModel

class Address(BaseModel):
    city:str
    state:str
    pin:str
    

class Patient(BaseModel):
    name:str
    gender:str
    age:int
    address:Address
    
    
address_dict={'city':'gurgaun','state':'haryana','pin':'1222013'}
address1=Address(**address_dict)

patient_dict={'name':'nitish','gender':'male','age':'13','address':address1}
patient1=Patient(**patient_dict)
print(patient1)
print(patient1.address)
print(patient1.address.city)
print(patient1.address.pin)  

#convert pydantic model into dictionary
temp=patient1.model_dump(include=['name','age'])
temp=patient1.model_dump(exclude=['name','age'])
temp=patient1.model_dump(exclude={'address':['pin']})
print(temp)
print(type(temp))

temp_json=patient1.model_dump_json()
print(temp_json)
print(type(temp_json))
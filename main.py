from fastapi import FastAPI,Path,Query,HTTPException
import json

app=FastAPI()

def load_data():
 with open("patients.json","r") as f:
    data=json.load(f)
    return data

@app.get("/")
def hello():
    return {"message":"Patient Management System API"}


@app.get("/about")
def about():
    return {"message":"A fully functional API to manage your patient records."}


@app.get("/view")
def view():
    data=load_data()
    
    return data
#path parameter
@app.get("/patient/{patient_id}")
def view_patient(patient_id:str):
    data=load_data()
    
    if patient_id in data:
        return data[patient_id]
    raise HTTPException(status_code=404,detail="patient not found")


@app.get("/patient/city/{patient_city}")
def view_patient_city(patient_city:str):
    data=load_data()
   
    result={}
    for pid,info in data.items():
     if info["city"].lower()==patient_city.lower():
        result[pid]=info
    if not result:
        return {"message":"NO patients found in this city"}
    
    return result

@app.get("/patient/gender/{patient_gender}")
def view_patient_gender(patient_gender:str =Path(...,description="Gender the petient to get",example="male")):
    data=load_data()
   
    result={}
    for pid,info in data.items():
     if info["gender"].lower()==patient_gender.lower():
        result[pid]=info
    if not result:
        raise HTTPException(status_code=404,detail="No patients found with this city")
    
    return result

#query parameter
@app.get("/sort")
def sort_patients(sort_by:str= Query(...,description='sort on basis of height,weight,bmi'),order:str =Query('asc',description='sort in asc or desc order')):
    
    valid_fields=['height','weight','bmi']
    
    if sort_by not in valid_fields:
        raise HTTPException(status_code=400,detail=f"Invalid field select from {valid_fields}")
        
    if order not in ['asc','desc']:
        raise HTTPException(status_code=400,detail='Invalid order between asc and desc')
    
    sort_order= True if order=='desc' else False
    
    data=load_data()
    sorted_data=sorted(data.values(),key=lambda x: x.get(sort_by,0),reverse=sort_order )
    
    return sorted_data
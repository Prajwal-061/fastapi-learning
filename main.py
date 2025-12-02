from fastapi import FastAPI,Path
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

@app.get("/patient/{patient_id}")
def view_patient(patient_id:str):
    data=load_data()
    
    if patient_id in data:
        return data[patient_id]
    return {"message":"Patient not found"}


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
        return {"message":"NO patients found of this gender"}
    
    return result
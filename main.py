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

#query parameter with city

@app.get("/patients")
def patients_city(city:str=Query(...,description="patients based on city")):
    
    data=load_data()
    result={}
    
    for pid,info in data.items():
        if info["city"].lower()==city.lower():
            result[pid]=info
    if not result:
            raise HTTPException(status_code=404,detail="No patients found in this city")
    return result
            
    
#query parameter with gender

@app.get("/patients_gender")
def patients_gender(gender:str=Query(...,description="Patients based on gender using query parameter")):
    data=load_data()
    result={}
    for pid,info in data.items():
      if info["gender"].lower()==gender.lower():
        result[pid]=info
    if not result:
      raise HTTPException(status_code=400,detail="Invalid gender typed by user,Bad request")
    return result
            
            
#query parameter with min and max age
@app.get("/patients_age")
def patients_age(min_age:int=Query(...,detail="minimum age of patients"),max_age:int=Query(...,detail='max age of a patients')):
     data=load_data()
     result={}
     for pid, info in data.items():
         if info["age"] >= min_age and info["age"]<= max_age:
             result[pid]=info
     if not result:
         raise HTTPException(status_code=400,detail="Bad request")
     return result
             
     
#query parameter to search with "a"
@app.get("/search")
def search(name:str=Query(...,description='To search patient name havin alphabet a')):
    data= load_data()
    result={}
    for pid,info in data.items():
        if name.lower() in info["name"].lower():
            result[pid]=info
    if not result:
        raise HTTPException(status_code=404,detail='bad request')
    return result
            

# path and query parameter combine
@app.get("/patient/city/{city}")
def filter_city_with_age(city:str=Path(description='patients on basis of city'),min_age:int=Query(None,description='filter city with age')):
    
    data=load_data()
    result={}
    
    for pid,info in data.items():
        if info["city"].lower()== city.lower():
         if min_age is None or info['age']>=min_age:
            result[pid]=info
    if not result:
        raise HTTPException(status_code=404,detail="Data not found")
    return result
            
            
        
        
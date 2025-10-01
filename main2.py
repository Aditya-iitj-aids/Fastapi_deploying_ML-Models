from fastapi import FastAPI
import json
app=FastAPI()#created an object app
def load_data():
    with open('patients.json','r') as f:
        data=json.load(f)
    return data
@app.get("/")
def read_root():
    return{"message":"Patient management system api"}
@app.get('/about')
def about():
    return {'msg':'fully operated and useful for recording patient records'}
@app.get('/view')
def view():
    data=load_data()
    return data
@app.get('/patients/{patient_id}')#created a rout
def view_patient(patient_id:str):#created a function associated to the rout
    #load all the patients
    data=load_data()
    if patient_id in data:
        return data[patient_id]
    return{'error':'patient not found'}#patient id is a path parameter and is required
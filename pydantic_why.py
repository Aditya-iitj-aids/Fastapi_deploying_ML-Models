from pydantic import BaseModel
class Patient(BaseModel):
        #ensure that it imports basemodel 
        name:str
        age:int
# def insert_patient_data(name,age):
#         print(name)
#         print(age)
#         print('inserted into database')

def insert_patient_data(patient:Patient):
        print(patient.name)
        print(patient.age)
        print('inserted into database')

patient_info={'name':'adg_coder','age':'20'} #step1
patient1=Patient(**patient_info) #step2
#step3 send pydantic object
insert_patient_data(patient1)
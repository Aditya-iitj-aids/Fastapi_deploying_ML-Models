from pydantic import BaseModel

class Patient(BaseModel):
    name:str
    age:int
    #will create an object for the class
# def insert_patient_data(name,age):
#     print(name)
#     print(age)
#     print('inserted') Also CAN use oops


patient_info={'name':'nitish','age':30}
patient1=Patient(**patient_info) #unpacking the information by using double pointer

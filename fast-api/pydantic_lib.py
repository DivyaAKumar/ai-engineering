from numpy import insert
#below method is not scalable and efficient way to handle data validation and insertion. Using Pydantic models would be a better approach for data validation and management in FastAPI applications.
from pydantic import BaseModel, EmailStr, AnyUrl, Field, field_validator, ValidationError
from typing import List, Dict, Optional, Annotated

"""
def update_patient_data(name: str, age : int):
    if type(name) == str and type(age) == int:
        print(name)
        print(age)
        print("Data updated successfully")
    else:
        print("Invalid data types")

#insert_patient_data("div", 30)
#update_patient_data("div", 31)

#or 

def insert_patient_data(name: str, age : int):
    if type(name) == str and type(age) == int:
        if age< 0:
            raise ValueError("Age must be a positive integer")
        else:
            print(name)
            print(age)
            print("Data inserted successfully")
    else:
        print("Invalid data types") 
"""
#better approach
class Patient(BaseModel):
    #defining ideal schema
    name: str = Annotated[str, Field(min_length=1, max_length=50, title="Name of the patient", example ="Divya") ] #name should be string and length should be between 1 and 50
    email: EmailStr
    age: int = Field(gt = 0, lt = 120, description="Age must be a positive integer between 1 and 120") #age should be greater than 0 and less than 120
    LinkedIn: Optional[AnyUrl] = None #optional field
    weight: float = Field( ..., gt=0, description="Weight must be a positive number") #weight should be greater than 0 
    married: bool = False #default value
    allergies: list[str] | None = None #list should contain strings
    contact : dict[str, str]

    @field_validator('email')
    @classmethod
    def email_must_be_valid(cls, value):
        valid_domains = ['hdfc.com', 'icici.com', 'sbi.com']
        domain_name = value.split('@')[-1]
        if domain_name not in valid_domains:
            raise ValueError("Invalid email domain")
        return value

    @field_validator('name')
    @classmethod
    def transform_name(cls, value):
        return value.title() #capitalize first letter of each word

    @field_validator('age', mode = 'before')
    @classmethod
    def validate_age(cls, value):
        if not (0< value < 100):
            raise ValueError("Age must be a positive integer below 100")
        return value
    
patient_info = {'name': 'div', 'age': 33 , 'weight': 70.5,'email': 'div@hdfc.com', 'married': True, 'allergies': ['pollen', 'dust'], 'contact': {'phone': '123-456-7890'}   }

#patient 1 obj
patient1 = Patient(**patient_info) #unpacking dictionary to create an instance of Patient model

def insert_patient_data(patient: Patient):
    if type(patient.name) == str and type(patient.age) == int:
        if patient.age < 0:
            raise ValueError("Age must be a positive integer")
        else:
            print(patient.name)
            print(patient.age)
            print(patient.weight)
            print(patient.married)
            print(patient.allergies)
            print(patient.contact)
            print("Data inserted successfully")
    else:
        print("Invalid data types")

def update_patient_data(patient: Patient):
    if type(patient.name) == str and type(patient.age) == int:
        print(patient.name)
        print(patient.age)
        print(patient.weight)
        print(patient.married)
        print(patient.allergies)
        print(patient.contact)
        print("Data updated successfully")
    else:
        print("Invalid data types")

#insert_patient_data("div", 30)
#update_patient_data("div", 31)

insert_patient_data(patient1)
update_patient_data(patient1)
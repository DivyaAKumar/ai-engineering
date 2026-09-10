#exporting as python dict or json 
#debugging, logging

from pydantic import BaseModel

class Address(BaseModel):
    city: str
    state: str
    zip_code: str

class Patient(BaseModel):
    name : str
    gender : str = 'Male' #default value    
    age : int
    address: Address #address consists of multiple data types: so we can create a nested model for address

address_dict = {
    'city': 'Bhilai',
    'state': 'CG',  
    'zip_code': '490009'
}

address = Address(**address_dict) #unpacking dictionary to create an instance of Address model
patient_dict = {
    'name': 'div',
    'age': 30,
    'address': address
}

patient1 = Patient(**patient_dict) #unpacking dictionary to create an instance of Patient model

temp_dict = patient1.model_dump(include=['name', 'address'], exclude={'address': ['zip_code']}) #exporting as python dict 
print(temp_dict)
print(type(temp_dict))

temp_json = patient1.model_dump_json(exclude=['gender'], exclude_unset=True) #exporting as json
print(temp_json)
print(type(temp_json))

# gender cant be seen because we have excluded it from the export and also it is not set in the patient_dict so it is not included in the export
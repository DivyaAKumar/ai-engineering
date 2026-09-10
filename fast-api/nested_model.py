from pydantic import BaseModel

class Address(BaseModel):
    city: str
    state: str
    zip_code: str

class Patient(BaseModel):
    name : str
    gender : str 
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
    'gender': 'Female',
    'age': 30,
    'address': address
}

patient1 = Patient(**patient_dict) #unpacking dictionary to create an instance of Patient model

print(patient1)
print(patient1.address.city)
print(patient1.name)



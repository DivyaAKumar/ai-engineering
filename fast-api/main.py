import json
from pydantic import BaseModel, EmailStr, AnyUrl, Field, computed_field
from fastapi import FastAPI, Path , HTTPException , Query
from typing import Annotated, Literal, Optional
from fastapi.responses import JSONResponse

app = FastAPI()


class Patient(BaseModel):
    id : Annotated[str, Field(..., description = "Unique identifier for the patient", example = "P001")]
    name: str = Field(...,max_length = 50, min_length = 1, title = "Name of the patient", example = "Divya" )
    city: Annotated[str, Field(..., description = "City of residence", example = "Bhilai")]
    age: int = Field(gt = 0, lt = 120, description = "Age must be a positive integer between 1 and 120")
    gender: Annotated[Literal['Male', 'Female', 'Other'], Field(..., description = "Gender of the patient")]
    height: float = Field(..., gt = 0, description = "Height must be a positive number in meters")
    weight: float = Field(..., gt = 0, description = "Weight must be a positive number in kilograms")
   
    @computed_field
    @property
    def bmi(self)-> float:
        bmi = round(self.weight/self.height**2, 2)
        return bmi

    @computed_field
    @property
    def verdict(self) -> str:
        if self.bmi < 18.5:
            return "Underweight"
        elif 18.5 <= self.bmi < 24.9:
            return "Normal weight"
        elif 25 <= self.bmi < 29.9:
            return "Overweight"
        else:
            return "Obese"

class PatientUpdate(BaseModel):
    name: Annotated[Optional[str] | None, Field(None, max_length=50, min_length=1, title="Name of the patient")]
    city: Annotated[Optional[str] | None, Field(None, description="City of residence")]
    age: Annotated[Optional[int] | None, Field(None, gt=0, lt=120, description="Age must be a positive integer between 1 and 120")]
    gender: Annotated[Optional[Literal['Male', 'Female', 'Other']] | None, Field(None, description="Gender of the patient")]
    height: Annotated[Optional[float] | None, Field(None, gt=0, description="Height must be a positive number in meters")]
    weight: Annotated[Optional[float] | None, Field(None, gt=0, description="  Weight must be a positive number in kilograms")] 


#helper function
def load_data():
    # This function would load data from a database or file
    with open("patients.json", "r") as f:
        data = json.load(f)
    return data

def save_data(data):
    with open('patients.json', 'w') as f:
        json.dump(data, f)
# creating endpoints for the application
@app.get("/") #path define 
async def hello(): 
    return {'message': 'Patient management system API'}

@app.get("/about") #path define
async def about():
    return {'message': 'A fully functional API to manage patients and their medical records.'}
#view all data 
@app.get('/view')
def view():
    data = load_data()
    return data

#path params
@app.get("/view/{patient_id}")
async def view_patient(patient_id: str = Path(..., description = 'ID of patient in DB')):
    data = load_data()
    if patient_id in data:
        return data[patient_id]
    raise HTTPException(status_code=404, detail="Patient not found")

#query params
@app.get('/sort')
def sort_patients(sort_by: str = Query(..., description = 'Sort on the basis of height, weight or bmi'), order: str = Query('asc', description = 'sort in asc or desc order')):
    valid_fields = ['height', 'weight', 'bmi']
    if sort_by not in valid_fields:
        raise HTTPException(status_code=400, detail=f"Invalid sort field. Must be one of {valid_fields}")
    if order not in ['asc', 'desc']:
        raise HTTPException(status_code=400, detail="Invalid order. Must be 'asc' or 'desc'")
    data = load_data()

    sort_order = True if order == 'desc' else False

    sorted_data = sorted(data.values(), key=lambda x: x.get(sort_by, 0), reverse=sort_order)
    return sorted_data

@app.post("/create")
async def create_patient(
    patient: Patient
):
    #load existing data
    data = load_data()
    #check if patient already exists
    if patient.id in data: 
        raise HTTPException(status_code=400, detail="Patient with this ID already exists")
        
    # new patient add to database
    data[patient.id] = patient.model_dump(exclude= ['id'])
    #saving the fata into json file
    save_data(data)

    return JSONResponse(status_code=201, content={"message": "Patient created successfully", "patient": patient.model_dump()})

@app.put("/edit/{patient_id}")
async def update_patient(patient_id : str, patient_update: PatientUpdate):
    #load data of all the patient
    data = load_data()
    #if patient_id not in data, raise error
    if patient_id not in data:
        raise HTTPException(status_code=404, detail="Patient not found")
    # update the patient's information
    existing_patient_info = data[patient_id]
    # update the fields that are provided in the update request
    
    patient_update_dict = patient_update.model_dump(exclude_unset=True) # if exlude_unset is True, it will only include fields that were explicitly set in the update request, and exclude any fields that were not provided. This allows for partial updates of the patient information.
    for key, value in patient_update_dict.items():
        existing_patient_info[key] = value

    #existing_patient_info -> pydantic object -> updated bmi+ verdict -> pydantic object -> dict
    
    #existing_patient_info -> pydantic object -> updated bmi+ verdict 
    existing_patient_info['id']= patient_id # add the patient_id to the existing_patient_info dictionary. This is necessary because the Patient model requires an 'id' field, and we want to ensure that the updated patient information includes the correct patient ID.
    patient_pydantic_object = Patient(**existing_patient_info) #To convert the existing dictionary data into a Patient Pydantic object
    #updated bmi+ verdict -> pydantic object -> dict
    existing_patient_info = patient_pydantic_object.model_dump(exclude = 'id') # convert the updated Patient object back into a dictionary format. This dictionary will now include the updated BMI and verdict values, along with any other updated fields.
    #adding this dict to data
    data[patient_id] = existing_patient_info #existing_patient_info is a dictionary that contains the updated information for the patient with the given patient_id. By assigning this dictionary back to data[patient_id], we are effectively updating the patient's information in the data dictionary.

    # save the updated data
    save_data(data)

    return JSONResponse(status_code=200, content={"message": "Patient updated successfully", "patient": existing_patient_info})

@app.delete("/delete/{patient_id}")
def delete_patient(patient_id: str):
    #load data of all the patient
    data = load_data()
    #if patient_id not in data, raise error
    if patient_id not in data:
        raise HTTPException(status_code=404, detail="Patient not found")
    # delete the patient
    del data[patient_id]
    # save the updated data
    save_data(data)
    return JSONResponse(status_code=200, content={"message": "Patient deleted successfully"})
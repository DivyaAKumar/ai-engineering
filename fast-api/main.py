import json

from fastapi import FastAPI, Path , HTTPException , Query

app = FastAPI()

#helper function
def load_data():
    # This function would load data from a database or file
    with open("patients.json", "r") as f:
        data = json.load(f)
    return data

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



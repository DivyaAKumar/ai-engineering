from fastapi import FastAPI
from pydantic import BaseModel, Field, computed_field
from typing import Optional, Literal, Annotated
import pickle 
import pandas as pd
from fastapi.responses import JSONResponse

#import ml model
with open('model.pkl', 'rb') as f:
    model = pickle.load(f)

app = FastAPI()

@app.get("/") #path define 
async def home(): 
    return {'message': 'Insurance premium prediction model'}

tier_1_cities = ["Mumbai", "Delhi", "Bangalore", "Chennai", "Kolkata", "Hyderabad", "Pune"]

tier_2_cities = [
    "Jaipur", "Chandigarh", "Indore", "Lucknow", "Patna", "Ranchi",
    "Visakhapatnam", "Coimbatore", "Bhopal", "Bhubaneswar", "Vadodara",
    "Surat", "Rajkot", "Jodhpur", "Raipur", "Amritsar", "Varanasi", "Agra",
    "Dehradun", "Mysore", "Jabalpur", "Guwahati", "Thiruvananthapuram",
    "Ludhiana", "Nashik", "Allahabad", "Udaipur", "Aurangabad", "Hubli",
    "Belgaum", "Salem", "Vijayawada", "Tiruchirappalli", "Bhavnagar",
    "Gwalior", "Dhanbad", "Bareilly", "Aligarh", "Gaya", "Kozhikode",
    "Warangal", "Kolhapur", "Bilaspur", "Jalandhar", "Noida", "Guntur",
    "Asansol", "Siliguri"
]
#pydantic model to validate incoming data
class UserInput(BaseModel):
    age: Annotated[int, Field(..., gt = 0, lt=120, description= "age of the user")]
    weight: Annotated[float, Field(..., gt = 0, description= "weight of the user")]
    height: Annotated[float, Field(..., gt = 0, lt=2.5, description= "height of the user")]
    income_lpa: Annotated[float, Field(..., description= "Annual salary of the user")]
    smoker: Annotated[bool, Field(..., description='Is user a smoker')]
    city:Annotated[str, Field(..., description= "city of the user")]
    occupation: Annotated[Literal['retired', 'unemployed', 'business_owner', 'government_job',
       'private_job', 'freelancer'], Field(..., description= "occupation of the user")]

    @computed_field
    @property
    def bmi(self) -> float:
        return self.weight/self.height**2


    @computed_field
    @property
    def lifestyle_risk(self)-> str:
        if self.smoker and self.bmi > 30:
            return "high"
        elif self.smoker and self.bmi > 27:
            return "medium"
        else:
            return "low"

    @computed_field
    @property
    def age_grp(self) -> str:
        if self.age < 25:
            return "young"
        elif self.age < 45:
            return "adult"
        elif self.age < 60:
            return "middle-aged"
        else:
            return "senior"

    
    @computed_field
    @property
    def city_tier(city) -> int:
        if city in tier_1_cities:
            return 1
        elif city in tier_2_cities:
            return 2
        else:
            return 3

@app.post('/predict')
def predict_premium(data: UserInput):
    input_df= pd.DataFrame([{
        'bmi': data.bmi,
        'age_group': data.age_grp,
        'lifestyle_risk': data.lifestyle_risk,
        'city_tier': data.city_tier,
        'income_lpa': data.income_lpa,
        'occupation': data.occupation
    }
])
    prediction= model.predict(input_df)[0]

    return JSONResponse(status_code=200, content={'prediction_category': prediction})
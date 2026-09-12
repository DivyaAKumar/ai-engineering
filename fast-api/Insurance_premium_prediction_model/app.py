from fastapi import FastAPI
from pydantic import BaseModel, Field, computed_field, field_validator
from typing import Optional, Literal, Annotated
from fastapi.responses import JSONResponse
from schema.user_input import UserInput
from model.predict import predict_output,model, MODEL_VERSION
app = FastAPI()

#human readable
@app.get("/") #path define 
async def home(): 
    return {'message': 'Insurance premium prediction model'}

#health check api: machine readable
@app.get('/health')
async def health_check():
    return{
        'status': 'OK',
        'version' : MODEL_VERSION,
        'model_loaded': model is not None

    }


@app.post('/predict')
def predict_premium(data: UserInput):
    user_input = {
        'bmi': data.bmi,
        'age_group': data.age_grp,
        'lifestyle_risk': data.lifestyle_risk,
        'city_tier': data.city_tier,
        'income_lpa': data.income_lpa,
        'occupation': data.occupation
    }
    try:
        prediction= predict_output(user_input)

        return JSONResponse(status_code=200, content={'prediction_category': prediction})

    except Exception as e:
        return JSONResponse(status_code=500, content = str(e))
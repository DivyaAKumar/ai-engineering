from fastapi import FastAPI

app = FastAPI()

# creating endpoints for the application
@app.get("/") #path define 
async def hello(): 
    return {'message': 'Hello World!'}

@app.get("/about") #path define
async def about():
    return {'message': 'This is a FastAPI application.'}
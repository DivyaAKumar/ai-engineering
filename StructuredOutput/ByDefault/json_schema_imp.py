import json
from pydantic import BaseModel, Field
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
from typing import Annotated, Optional,Literal


load_dotenv("../../LangChainModels/.env")

model = ChatOpenAI()

with open("json_schema.json", "r") as file:
    Review = json.load(file)
#schema
StructuredModel = model.with_structured_output(
    Review,
    method="function_calling"
)
result = StructuredModel.invoke('''good display and good graphics''')
print(result)

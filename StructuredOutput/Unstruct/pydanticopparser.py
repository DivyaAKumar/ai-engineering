from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import PydanticOutputParser
from pydantic import BaseModel, Field

load_dotenv("../../LangChainModels/.env")

llm = HuggingFaceEndpoint(
    repo_id="meta-llama/Llama-3.1-8B-Instruct",
    task="text-generation"
)
model = ChatHuggingFace(llm=llm)

class Person(BaseModel):
    name: str = Field(description='name of the person')
    age : int = Field(gt = 18 , description='age of the person')
    city : str = Field(description='city of the person belongs to')

parser = PydanticOutputParser(pydantic_object=Person)

template = PromptTemplate(
    template = 'generate the name, age and city of a fictional {nationality} person \n {format_instructions}',
    input_variables=['nationality'],
    partial_variables={'format_instructions': parser.get_format_instructions}
)

chain = template | model | parser
result = chain.invoke({'nationality': 'indian'})
print(result)
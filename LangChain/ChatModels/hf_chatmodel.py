from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from dotenv import load_dotenv
import os

load_dotenv(r"D:\pythonProj\python-for-ai\LangChain\.env")
llm = HuggingFaceEndpoint(
    repo_id = "openai/gpt-oss-120b",#model that we wanna use
    task = "text-generation",
   
)
model = ChatHuggingFace(llm=llm)
result = model.invoke("what is the capital of india")
print(result.content)


#i dont have api key coz i'm poor
from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv

load_dotenv()
model = ChatGoogleGenerativeAI(model = 'gemini-1.5-pro') 
result= model.invoke("What is the capital of India")
print(result.content) # .content to get the result without metadata
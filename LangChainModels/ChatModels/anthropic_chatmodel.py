#i dont have api key coz i'm poor
from langchain_anthropic import ChatAnthropic
from dotenv import load_dotenv

load_dotenv()
model = ChatAnthropic(model = 'claude=3-5-sonnet-20241022') #console.anthropic.com-> documentation me user guides
result= model.invoke("What is the capital of India")
print(result.content) # .content to get the result without metadata
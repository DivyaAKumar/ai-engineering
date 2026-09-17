from langchain_core.messages import SystemMessage, HumanMessage, AIMessage
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv

load_dotenv('../LangChainModels/.env') 
#systemmessage: you are a very knowledgable doc etc.written on top of a message
model = ChatOpenAI()

messages = [
    SystemMessage(content= 'You are a helpful assistant'),
    HumanMessage(content= "tell me about LangChain")
]
result = model.invoke(messages)
messages.append(AIMessage(content = result.content))
print(messages)
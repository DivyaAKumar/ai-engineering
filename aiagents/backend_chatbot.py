from langgraph.graph import StateGraph, START, END
from typing import TypedDict, Literal, Annotated
from langchain_openai import ChatOpenAI
from langchain_core.messages import BaseMessage
from pydantic import BaseModel
from IPython.display import Image
from langgraph.graph.message import add_messages
from langgraph.checkpoint.memory import MemorySaver
import uuid
from dotenv import load_dotenv


load_dotenv("../LangChainModels/.env")
class ChatState(TypedDict):
    messages : Annotated[list[BaseMessage], add_messages]
llm =ChatOpenAI()
def chat_node(state: ChatState) -> ChatState:
    messages = state['messages']
    response = llm.invoke(messages)
    return{
        'messages': [response]
        }
checkpointer = MemorySaver()

graph = StateGraph(ChatState)

#add nodes
graph.add_node('chat_node', chat_node)

graph.add_edge(START, 'chat_node')
graph.add_edge('chat_node', END)

chatbot = graph.compile(checkpointer=checkpointer)



from langgraph.graph import StateGraph, START, END
from typing import TypedDict, Literal, Annotated
from langchain_openai import ChatOpenAI
from langchain_core.messages import BaseMessage,HumanMessage
from pydantic import BaseModel
from IPython.display import Image
from langgraph.graph.message import add_messages
from langgraph.checkpoint.sqlite import SqliteSaver
import uuid
from dotenv import load_dotenv
import sqlite3
import os

os.environ["LANGSMITH_TRACING"] = "true"
os.environ['LANGCHAIN_PROJECT'] = 'Chatbot'

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

conn = sqlite3.connect(database = 'chatbot.db', check_same_thread= False)#true me error as sqlite server works on single thread
checkpointer = SqliteSaver(conn=conn)

graph = StateGraph(ChatState)

#add nodes
graph.add_node('chat_node', chat_node)

graph.add_edge(START, 'chat_node')
graph.add_edge('chat_node', END)

chatbot = graph.compile(checkpointer=checkpointer)

def extract_threads():
    all_threads = set()
    #to extract number of threads already present in db
    for checkpoint in checkpointer.list(None):
        all_threads.add(checkpoint.config['configurable']['thread_id'])
    return list(all_threads)
from langgraph.graph import StateGraph, START, END
from typing import TypedDict,  Annotated
from langchain_openai import ChatOpenAI
from langchain_core.messages import BaseMessage,HumanMessage
from pydantic import BaseModel
from IPython.display import Image
from langgraph.graph.message import add_messages
from langgraph.checkpoint.sqlite import SqliteSaver
from dotenv import load_dotenv
import sqlite3

from langgraph.prebuilt import ToolNode, tools_condition
from langchain_community.tools import DuckDuckGoSearchRun
from langchain_core.tools import tool
import requests
import random

load_dotenv("../LangChainModels/.env")

class ChatState(TypedDict):
    messages : Annotated[list[BaseMessage], add_messages]

llm =ChatOpenAI()
#tools
search_tool = DuckDuckGoSearchRun(region = 'us-en')

@tool
def calculator(first_num: float, second_num: float, operation: str) -> dict:
    """
    Perform a basic arithmetic operation on two numbers.
    Supported operations: add, sub, mul, div
    """
    try:
        if operation == "add":
            result = first_num + second_num

        elif operation == "sub":
            result = first_num - second_num

        elif operation == "mul":
            result = first_num * second_num

        elif operation == "div":
            if second_num == 0:
                return {"error": "Division by zero is not allowed"}
            result = first_num / second_num

        else:
            return {"error": f"Unsupported operation '{operation}'"}

        return {
            "first_num": first_num,
            "second_num": second_num,
            "operation": operation,
            "result": result
        }

    except Exception as e:
        return {"error": str(e)}
@tool
def get_weather_data(city: str) -> str:
    """
    This function fetches the current weather data for a given city
    """
    url = f'https://api.weatherstack.com/current?access_key=61b5625614eb120f91840beb55f1d03c&query={city}'

    response = requests.get(url)

    return response.json()
#tool list
tools = [get_weather_data, search_tool, calculator]
#making llm tool aware
llm_with_tools = llm.bind_tools(tools)
def chat_node(state: ChatState) -> ChatState:
    messages = state['messages']
    response = llm_with_tools.invoke(messages)
    return{
        'messages': [response]
        }

tool_node = ToolNode(tools) #executes tool calls
conn = sqlite3.connect(database = 'chatbot.db', check_same_thread= False)#true me error as sqlite server works on single thread
checkpointer = SqliteSaver(conn=conn)

graph = StateGraph(ChatState)

#add nodes
graph.add_node('chat_node', chat_node)
graph.add_node('tools', tool_node)

graph.add_edge(START, 'chat_node')
graph.add_conditional_edges('chat_node', tools_condition)
graph.add_edge('tools', 'chat_node')
chatbot = graph.compile(checkpointer=checkpointer)

def extract_threads():
    all_threads = set()
    #to extract number of threads already present in db
    for checkpoint in checkpointer.list(None):
        all_threads.add(checkpoint.config['configurable']['thread_id'])
    return list(all_threads)

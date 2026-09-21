from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser

load_dotenv("../LangChainModels/.env")

prompt = PromptTemplate(
    template= "generate 5 interesting facts about {topic}",
    input_variables = ['topic']
)

model = ChatOpenAI()

parser = StrOutputParser()

chain = prompt | model | parser

result = chain.invoke({'topic': 'ai engineering'})
print(result)

chain.get_graph().print_ascii() #for visualizing
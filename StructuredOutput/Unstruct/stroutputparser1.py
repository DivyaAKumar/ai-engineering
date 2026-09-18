from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
load_dotenv("../../LangChainModels/.env")


model = ChatOpenAI()

#1st prompt -> detailed report
template1 = PromptTemplate(
    template = "Write a detailed report on topic {topic}",
    input_var = ['topic']
)

#2nd prompy -> summary
template2 = PromptTemplate(
    template = 'Write a 5 line summary on the following text. \n {text}.',
    input_var = ['text']
)

parser = StrOutputParser()

chain = template1 | model | parser | template2 | model | parser

result= chain.invoke({'topic': 'black hole'})

print(result)
from langchain_community.document_loaders import TextLoader
from langchain_openai import ChatOpenAI
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import PromptTemplate
from dotenv import load_dotenv

load_dotenv("../../LangChainModels/.env")
loader = TextLoader('D:/pythonProj/python-for-ai/RAG/DocumentLoaders/cricket.txt', encoding = 'utf-8')
model= ChatOpenAI()

prompt = PromptTemplate(
    template='write a short summary for the following text \n {text}',
    input_variables=['text']
)
parser = StrOutputParser()

docs= loader.load()
#print(docs[0]) 
#print(docs) #with metadata and content
#print(len(docs)) #1
#print(docs[0].page_content) #i lowkey like playing cricket
#print(docs[0].metadata) #'source': 'D:/pythonProj/python-for-ai/RAG/DocumentLoaders/cricket.txt'
 
chain = prompt | model | parser 
print(chain.invoke({'text': docs[0].page_content})) #The person admits to enjoying playing cricket, but does not express a strong or overly enthusiastic interest in the sport.

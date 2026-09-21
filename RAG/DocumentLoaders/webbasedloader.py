from langchain_community.document_loaders import WebBaseLoader
from langchain_openai import ChatOpenAI
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import PromptTemplate
from dotenv import load_dotenv
import bs4
load_dotenv("../../LangChainModels/.env")
url = 'https://www.hafuboti.com/blog/blogs/hoti/'
loader = WebBaseLoader(url)
docs = loader.load()
model= ChatOpenAI()

prompt = PromptTemplate(
    template='write a short summary for the following text \n {text}',
    input_variables=['text']
)
parser = StrOutputParser()
chain = prompt | model | parser
print(chain.invoke({'text':docs[0].page_content}))


#print(len(docs))
#print(docs[0].page_content)
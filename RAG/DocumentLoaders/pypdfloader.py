from langchain_community.document_loaders import PyPDFLoader
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import PromptTemplate
from dotenv import load_dotenv

load_dotenv("../../LangChainModels/.env")
loader = PyPDFLoader(r'D:\pythonProj\python-for-ai\RAG\DocumentLoaders\AI_Engineer_Roadmap_TrackA_TrackB.pdf')
docs = loader.load()
#model= ChatOpenAI()

print(len(docs))
print(docs[0].page_content)
print(docs[1].metadata)
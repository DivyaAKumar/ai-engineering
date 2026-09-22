from langchain_text_splitters import CharacterTextSplitter
from langchain_community.document_loaders import PyPDFLoader

loader = PyPDFLoader(r'D:\pythonProj\python-for-ai\RAG\TextSplitter\💡 Generative AI Workshop Resource Document.pdf')
docs = loader.load()

splitter = CharacterTextSplitter(
    chunk_size = 400,
    chunk_overlap= 0,
    separator= ''
)
result = splitter.split_documents(docs)
#print(result)
print(result[0].page_content) #first chunk
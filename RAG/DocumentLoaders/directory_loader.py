from langchain_community.document_loaders import DirectoryLoader, PyPDFLoader
loader = DirectoryLoader(
    path = r'D:\pythonProj\python-for-ai\RAG\DocumentLoaders\books',
    glob = '*.pdf',
    loader_cls = PyPDFLoader
)

docs = loader.lazy_load()
#print(len(docs))
#print(docs[0].page_content)
#print(docs[0].metadata)
for document in docs:
    print(document.metadata)
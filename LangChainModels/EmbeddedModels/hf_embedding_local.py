from langchain_huggingface import HuggingFaceEmbeddings

embedding = HuggingFaceEmbeddings(model = "sentence-transformers/all-MiniLM-L6-v2")
text = 'Delhi is the capital of india'
vector = embedding.embed_query(text)
print(str(vector))

documents = [
    "delhi is the capital of india",
    "kolkata is capital of west bengal",
    "paris is the capital of france"
]
result = embedding.embed_documents(documents)
print(str(result))
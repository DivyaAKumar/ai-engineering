from langchain_openai import OpenAIEmbeddings
from dotenv import load_dotenv

load_dotenv()

embedding = OpenAIEmbeddings(model = "text-embedding-3-large", dimensions= 32) #dimensions= more dimension more context capture.

documents = [
    "delhi is the capital of india",
    "kolkata is capital of west bengal",
    "paris is the capital of france"
]
result = embedding.embed_documents(documents)
print(str(result))
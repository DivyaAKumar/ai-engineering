from langchain_openai import OpenAIEmbeddings
from dotenv import load_dotenv

load_dotenv()

embedding = OpenAIEmbeddings(model = "text-embedding-3-large", dimensions= 32) #dimensions= more dimension more context capture.
result = embedding.embed_query("delhi is the capital of india.")
print(str(result))
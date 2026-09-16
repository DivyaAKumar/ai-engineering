from langchain_openai import OpenAIEmbeddings
from dotenv import load_dotenv
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np

load_dotenv()

embedding = OpenAIEmbeddings(model = 'text-embedding-3-large', dimensions=300)
document = [
    "Divya A Kumar is a famous AI Engineer who is currently exploring AI. she is very fun and expressive and extremely chalant",
    "Parth Sharma is a profound software engineer in ITT. He takes care of his gf divya always",
    'Ayushi dubey is an artist who makes beautiful paintings',
    "Sanika is currently preparing for mba. she is very pretty too",
    'Naveen and harsh are the best duo any girl could ever ask for. they are both quite ambitious.'

]

query = "tell me about Parth Sharma"

doc_embedding = embedding.embed_documents(document)
query_embedding = embedding.embed_query(query)

score = cosine_similarity([query_embedding], doc_embedding)[0]
index, score = sorted(enumerate(score), key=lambda x: x[1])[-1]
print(document[index])
print("similarity score is: ", score)

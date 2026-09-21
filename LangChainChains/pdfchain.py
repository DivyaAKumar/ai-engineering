from dotenv import load_dotenv

from langchain_community.document_loaders import TextLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import FAISS

from langchain_openai import OpenAIEmbeddings, ChatOpenAI

from langchain_core.prompts import ChatPromptTemplate

from langchain.chains import create_retrieval_chain
from langchain.chains.combine_documents import create_stuff_documents_chain


load_dotenv("../LangChainModels/.env")


# Load the document
loader = TextLoader("docs.txt")
documents = loader.load()


# Split the text into smaller chunks
text_splitter = RecursiveCharacterTextSplitter(
    chunk_size=500,
    chunk_overlap=50
)

docs = text_splitter.split_documents(documents)


# Convert text into embeddings and store in FAISS
vectorstore = FAISS.from_documents(
    docs,
    OpenAIEmbeddings()
)


# Create a retriever
retriever = vectorstore.as_retriever()


# Initialize the LLM
model = ChatOpenAI(
    model="gpt-4o-mini",
    temperature=0.7
)


# Create a prompt
prompt = ChatPromptTemplate.from_template(
    """
    Answer the following question based only on the provided context.

    <context>
    {context}
    </context>

    Question: {input}
    """
)


# Create the document-combining chain
document_chain = create_stuff_documents_chain(
    model,
    prompt
)


# Create the retrieval chain
qa_chain = create_retrieval_chain(
    retriever,
    document_chain
)


# Ask a question
query = "What are the key takeaways from the document?"

response = qa_chain.invoke({
    "input": query
})


# Print the answer
print("Answer:", response["answer"])
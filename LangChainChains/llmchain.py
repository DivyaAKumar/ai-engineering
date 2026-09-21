from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser

from dotenv import load_dotenv

load_dotenv("../LangChainModels/.env")


# Load the LLM
model = ChatOpenAI(
    model="gpt-4o-mini",
    temperature=0.7
)


# Create a Prompt Template
prompt = PromptTemplate(
    input_variables=["topic"],
    template="Suggest a catchy blog title about {topic}."
)


# Create a chain using LCEL
parser = StrOutputParser()

chain = prompt | model | parser


# Run the chain with a specific topic
topic = input("Enter a topic: ")

output = chain.invoke({
    "topic": topic
})


print("Generated Blog Title:", output)
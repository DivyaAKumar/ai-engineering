from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser

load_dotenv("../LangChainModels/.env")

prompt1 = PromptTemplate(
    template = 'generate a detailed report on {topic}',
    input_variables= ['topic']
)

prompt2 = PromptTemplate(
    template='extract 3 major keypoints from given text \n {text}',
    input_variables=['text']
)

model = ChatOpenAI()

parser = StrOutputParser()

chain = prompt1 | model | parser | prompt2 | model | parser 

result = chain.invoke({'topic': 'black hole'})
print(result)
chain.get_graph().print_ascii()


from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv
from langchain_core.runnables import RunnableSequence

load_dotenv('../../LangChainModels/.env')

prompt1 = PromptTemplate(
    template='write a joke on {topic}',
    input_variable = ['topic']
)

model = ChatOpenAI()

parser = StrOutputParser()

prompt2 = PromptTemplate(
    template='explain the following joke- {text}',
    input_variables= ['text']
)

chain = RunnableSequence(prompt1, model , parser, prompt2, model, parser)

print(chain.invoke({'topic': 'ai'}))
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.output_parsers import PydanticOutputParser
from pydantic import BaseModel, Field
from typing import Literal
from langchain_core.runnables import RunnableParallel , RunnableBranch , RunnableLambda

load_dotenv("../LangChainModels/.env")

model = ChatOpenAI()

parser = StrOutputParser()

class Feedback(BaseModel):
    sentiment : Literal['positive', 'negative'] = Field(description = 'give the sentiment of the feedback')

parser2 = PydanticOutputParser(pydantic_object=Feedback)

prompt1 = PromptTemplate(
    template = 'classify the sentiment of the following feedback text into positive or negative \n {feedback} \n {format_instructions}',
    input_variables= ['feedback'],
    partial_variables= {'format_instructions': parser2.get_format_instructions}
)

classifier_chain = prompt1 | model | parser2 # sentiment = "positive" or sentiment = "negative" structured o/p

#result = classifier_chain.invoke({'feedback': 'this is a good smartphone'}).sentiment # positive or negative without sentiment = 
#print(result)

prompt2 = PromptTemplate(
    template='write an appropriate response to this positive feedback \n {feedback}',
    input_variables= ['feedback']
)

prompt3 = PromptTemplate(
    template='write an appropriate response to this negative feedback \n {feedback}',
    input_variables= ['feedback']
)
branch_chain = RunnableBranch( #multiple tuple
    #(condition1, chain),
    #(condition2, chain),
    #default chain
    (lambda x: x.sentiment == 'positive', prompt2 | model | parser),
    (lambda x: x.sentiment == 'negative', prompt3 | model | parser),
    #lambda x : 'could not find sentiment' #this is not a chain so convert it to runnnable Runnable Lambda
    RunnableLambda(lambda x : 'could not find sentiment')
)

chain = classifier_chain | branch_chain

result = chain.invoke({'feedback': 'this is a good smartphone'})
print(result)

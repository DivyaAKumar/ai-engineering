from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv
from langchain_core.runnables import RunnableSequence, RunnableParallel, RunnablePassthrough
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
joke_generator_chain = RunnableSequence(prompt1, model, parser)
parallel_chain = RunnableParallel({
    'joke': RunnablePassthrough(),
    'explaination': RunnableSequence(prompt2, model,parser)
})

final_chain = RunnableSequence(joke_generator_chain, parallel_chain)

print(final_chain.invoke({'topic': 'ai'}))
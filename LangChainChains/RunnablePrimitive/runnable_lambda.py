from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv
from langchain_core.runnables import RunnableSequence, RunnableParallel, RunnablePassthrough, RunnableLambda
load_dotenv('../../LangChainModels/.env')

#def word_count(text):
#   return len(text.split())

prompt = PromptTemplate(
    template='write a joke on {topic}',
    input_variable = ['topic']
)

model = ChatOpenAI()

parser = StrOutputParser()

joke_generator_chain = RunnableSequence(prompt, model, parser)
parallel_chain = RunnableParallel({
    'joke': RunnablePassthrough(),
    'word_count': RunnableLambda(lambda text: len(text.split()))
})

final_chain = RunnableSequence(joke_generator_chain, parallel_chain)

print(final_chain.invoke({'topic': 'ai'}))
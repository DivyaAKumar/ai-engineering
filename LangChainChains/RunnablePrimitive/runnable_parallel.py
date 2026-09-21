from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv
from langchain_core.runnables import RunnableParallel, RunnableSequence
from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint

load_dotenv('../../LangChainModels/.env')

llm = HuggingFaceEndpoint(
    repo_id = "openai/gpt-oss-120b",#model that we wanna use
    task = "text-generation",
   
)

prompt1 = PromptTemplate(
    template='generate a tweet about {topic}',
    input_variables=['topic']
)

prompt2 = PromptTemplate(
    template='generate a linkedin post about {topic}',
    input_variables=['topic']
)

model1 = ChatOpenAI()

model2 = ChatHuggingFace(llm=llm)

parser = StrOutputParser()

parallel_chain = RunnableParallel(
    {
        'tweet':RunnableSequence(prompt1, model1, parser),
        'linkedin': RunnableSequence(prompt2, model2, parser)
    }
)

result= parallel_chain.invoke({'topic': 'ai'})


print(result['tweet'])
print("----------------------")
print(result['linkedin'])
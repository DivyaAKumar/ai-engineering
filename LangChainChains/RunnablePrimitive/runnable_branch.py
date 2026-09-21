from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.output_parsers import PydanticOutputParser
from langchain_core.runnables import RunnableParallel , RunnableBranch , RunnableLambda, RunnableSequence , RunnablePassthrough

load_dotenv("../../LangChainModels/.env")

model = ChatOpenAI()

prompt1 = PromptTemplate(
    template= 'write detailed report on {topic}',
    input_variables=['topic']
)

prompt2 = PromptTemplate(
    template='summarize the following text \n {text}',
    input_variables=['text']
)

parser = StrOutputParser()

generate_report_chain = RunnableSequence(prompt1, model, parser)

branch_chain = RunnableBranch(
    (lambda x:len(x.split()) >= 500, RunnableSequence(prompt2, model,parser) ),
    RunnablePassthrough() 
)
final_chain = RunnableSequence(generate_report_chain, branch_chain)
print(final_chain.invoke({'topic': 'ai'}))
from langchain_openai import OpenAI
from langchain_core.prompts import PromptTemplate

#initialize the llm
llm = OpenAI(model='gpt-3.5-turbo', temperature = 0.7)

#create a prompt template
prompt = PromptTemplate(
    input_variables=['topic'],
    template='suggest a catchy blog title about {topic}'
)

#define the input
topic = input('enter the input')

#format the prompt manually using prompttemplate
formatted_prompt = prompt.format(topic=topic)
#call llm directly
blog_title = llm.predict(formatted_prompt)

#print o/p
print('generated blog title:', blog_title)
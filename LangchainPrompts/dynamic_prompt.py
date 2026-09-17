from langchain_core.prompts import ChatPromptTemplate
from langchain_core.messages import SystemMessage, HumanMessage, AIMessage

chat_template = ChatPromptTemplate([
    ('system', "you are a helpful {domain} expert" ),
    ('human', 'explain in simple terms, what is {topic}')
    # SystemMessage(content= "you are a helpful {domain} expert"),
    #HumanMessage(content='explain in simple terms, what is {topic}')
])
prompt = chat_template.invoke({'domain': 'cricket', 'topic': 'Dusra)'})

print(prompt)
from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import JsonOutputParser
load_dotenv("../../LangChainModels/.env")

llm = HuggingFaceEndpoint(
    repo_id="meta-llama/Llama-3.1-8B-Instruct",
    task="text-generation"
)
model = ChatHuggingFace(llm=llm)

parser = JsonOutputParser()

template = PromptTemplate(
    template = "give me the name, age and city of a fictional person \n {format_instruction}",
    input_variables=[],
    partial_variables={'format_instruction': parser.get_format_instructions()}

)# op cmplt prompt -give me the name, age and city of a fictional person Return a JSON object.


#prompt = template.format()

#result = model.invoke(prompt)

#final_result = parser.parse(result.content)

#print(final_result)
#print(type(final_result))

#with chains 
chain = template | model | parser 
result = chain.invoke({})

print(result)


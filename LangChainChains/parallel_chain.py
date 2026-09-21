from langchain_openai import ChatOpenAI
from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnableParallel

load_dotenv("../LangChainModels/.env")
llm = HuggingFaceEndpoint(
    repo_id = "openai/gpt-oss-120b",#model that we wanna use
    task = "text-generation",
   
)
model1 = ChatHuggingFace(llm=llm)
model2 = ChatOpenAI()
prompt1 = PromptTemplate(
    template='generate 3 line notes on {topic}',
    input_variables=['topic']
)

prompt2 = PromptTemplate(
    template = 'generate 3 question quiz on {topic}',
    input_variables= ['topic']
)

prompt3 = PromptTemplate(
    template="""
Create a single document containing BOTH the notes and the quiz.

NOTES:
{notes}

QUIZ:
{quiz}

Do not remove or summarize the quiz. Include all quiz questions exactly.
""",
    input_variables=['notes', 'quiz']
)

parser = StrOutputParser()

parallel_chain = RunnableParallel({
    'notes': prompt1 | model1 | parser,
    'quiz' : prompt2 | model2 | parser
}
)

merged_chain = prompt3 | model2 | parser

final_chain = parallel_chain | merged_chain 

text = "Overview Photosynthesis is the process used by plants, algae, and some bacteria to turn sunlight into energy. They convert light energy into chemical energy. This chemical energy is stored in glucose (a type of sugar) that the plant uses to grow and live.The ProcessPhotosynthesis takes place inside plant cells in small organs called chloroplasts. These chloroplasts contain a green pigment called chlorophyll, which captures the energy from sunlight.To make food, the plant needs three main ingredients:Sunlight: Provides the energy needed for the reaction.Water (H₂O): Absorbed by the plant's roots from the soil.Carbon dioxide (CO₂): Taken in from the air through tiny pores in the leaves called stomata.The Chemical EquationDuring this process, light energy helps convert carbon dioxide and water into glucose and oxygen.Inputs (What goes in): 6CO₂ (Carbon dioxide) + 6H₂O (Water) + Light energyOutputs (What comes out): C₆H₁₂O₆ (Glucose) + 6O₂ (Oxygen)Why It MattersPhotosynthesis is vital for life on Earth. It produces oxygen, which humans and animals need to breathe. It also forms the base of nearly all food chains by providing food for plants, which are then eaten by herbivores and other animals."
result = final_chain.invoke({'topic': text})
print(result)

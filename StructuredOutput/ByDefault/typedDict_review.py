from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
from typing import TypedDict, Annotated, Optional,Literal

load_dotenv("../../LangChainModels/.env")

model = ChatOpenAI()
#schema
class Review(TypedDict):
    key_themes : Annotated[list[str], "write down all the key themes discussed in the review in a list"]
    summary : Annotated[Literal['pos', 'neg', 'neutral'], 'A brief summary of the review']
    sentiment : Annotated[str, 'Return sentiment of the review either negative, positive or neutral']
    pros : Annotated[Optional[list[str]], "write all the pros inside the list"]
    cons : Annotated[Optional[list[str]], "write all the cons inside the list"]

StructuredModel = model.with_structured_output(Review,
    method="function_calling")
result = StructuredModel.invoke('''good display and good graphics''')
print(result)
print(result['summary'])
print(result['sentiment'])
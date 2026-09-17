from pydantic import BaseModel, Field
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
from typing import Annotated, Optional,Literal

load_dotenv("../../LangChainModels/.env")

model = ChatOpenAI()
#schema
class Review(BaseModel):

    key_themes: list[str] = Field(
        description="write down all the key themes discussed in the review in a list"
    )

    summary: str = Field(
        description="A brief summary of the review"
    )

    sentiment: Literal['pos', 'neg', 'neutral'] = Field(
        description="Return sentiment of the review as positive, negative or neutral"
    )

    pros: Optional[list[str]] = Field(default=None,
        description="write all the pros inside the list"
    )

    cons: Optional[list[str]] = Field( default=None,
        description="write all the cons inside the list"
    )

StructuredModel = model.with_structured_output(Review,
    method="function_calling")
result = StructuredModel.invoke('''good display and good graphics''')
print(result)


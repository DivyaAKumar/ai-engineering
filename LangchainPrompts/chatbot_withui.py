from langchain_openai import ChatOpenAI
from langchain_core.messages import HumanMessage, AIMessage
from dotenv import load_dotenv
import streamlit as st

load_dotenv("../LangChainModels/.env")

model = ChatOpenAI()

if "chat_history" not in st.session_state:
    st.session_state.chat_history = []


# Display previous messages
for message in st.session_state.chat_history:

    if isinstance(message, HumanMessage):
        with st.chat_message("user"):
            st.write(message.content)

    else:
        with st.chat_message("assistant"):
            st.write(message.content)


# Get new input
user_input = st.chat_input("Type your message...")


if user_input:

    # Add and immediately display user message
    user_message = HumanMessage(content=user_input)
    st.session_state.chat_history.append(user_message)

    with st.chat_message("user"):
        st.write(user_input)


    # Get AI response
    result = model.invoke(st.session_state.chat_history)

    # Add and immediately display AI response
    ai_message = AIMessage(content=result.content)
    st.session_state.chat_history.append(ai_message)

    with st.chat_message("assistant"):
        st.write(result.content)
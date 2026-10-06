import streamlit as st
from backend_chatbot import chatbot
from langchain_core.messages import HumanMessage
import uuid

if "thread_id" not in st.session_state:
    st.session_state["thread_id"] = str(uuid.uuid4())

config = {
    "configurable": {
        "thread_id": st.session_state["thread_id"]
    }
}

# st.session_state -> dict
if "message_history" not in st.session_state:
    st.session_state["message_history"] = []

# Display previous messages
for message in st.session_state["message_history"]:
    with st.chat_message(message["role"]):
        st.text(message["content"])

# Taking user input
user_input = st.chat_input("Type here")

if user_input:

    # Exit handling
    if user_input.strip().lower() in ["exit", "quit", "bye", "end"]:
        st.write("Goodbye!")
        st.stop()

    # Store user message
    st.session_state["message_history"].append({
        "role": "user",
        "content": user_input
    })

    with st.chat_message("user"):
        st.text(user_input)

    # Calling LangGraph
    response = chatbot.invoke(
        {
            "messages": [
                HumanMessage(content=user_input)
            ]
        },
        config=config
    )

    # Get AI response
    ai_message = response["messages"][-1].content

    # Store AI message
    st.session_state["message_history"].append({
        "role": "assistant",
        "content": ai_message
    })

    with st.chat_message("assistant"):
        st.text(ai_message)
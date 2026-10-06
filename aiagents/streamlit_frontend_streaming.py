import streamlit as st
from backend_chatbot import chatbot
from langchain_core.messages import HumanMessage
import uuid


def generate_thread_id():
    thread_id = uuid.uuid4()
    return thread_id

if "thread_id" not in st.session_state:
    st.session_state["thread_id"] = generate_thread_id()

config = {
    "configurable": {
        "thread_id": st.session_state["thread_id"]
    }
}

#--------------sidebar ui------------------
st.sidebar.title('langGraph Chatbot')
st.sidebar.button('New Chat')
st.sidebar.header('Recent Conversations')
st.sidebar.text(st.session_state['thread_id'])



if "message_history" not in st.session_state:
    st.session_state["message_history"] = []

for message in st.session_state["message_history"]:
    with st.chat_message(message["role"]):
        st.text(message["content"])

user_input = st.chat_input("Type here")

if user_input:

    if user_input.strip().lower() in ["exit", "quit", "bye", "end"]:
        st.write("Goodbye!")
        st.stop()

    st.session_state["message_history"].append({
        "role": "user",
        "content": user_input
    })

    with st.chat_message("user"):
        st.text(user_input)

    with st.chat_message("assistant"):
        ai_message = st.write_stream(
            message_chunk.content
            for message_chunk, metadata in chatbot.stream(
                {
                    "messages": [
                        HumanMessage(content=user_input)
                    ]
                },
                config=config,
                stream_mode="messages"
            )
        )

    st.session_state["message_history"].append({
        "role": "assistant",
        "content": ai_message
    })
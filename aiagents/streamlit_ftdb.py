import streamlit as st
from db_backend import chatbot, extract_threads
from langchain_core.messages import HumanMessage, AIMessage
import uuid
from dotenv import load_dotenv

load_dotenv("../LangChainModels/.env")


def generate_thread_id():
    return str(uuid.uuid4())


def reset_chat():
    st.session_state["thread_id"] = generate_thread_id()
    st.session_state["message_history"] = []


def add_thread(thread_id):
    if thread_id not in st.session_state["chat_threads"]:
        st.session_state["chat_threads"].append(thread_id)


def load_convo(thread_id):
    return chatbot.get_state(
        config={
            "configurable": {
                "thread_id": thread_id
            }
        }
    ).values.get("messages", [])


def generate_title(messages):
    for message in messages:
        if isinstance(message, HumanMessage):
            text = message.content.strip()

            if text.lower() not in ["hi", "hello", "hey", "hii", "yo"]:
                return text[:35] + "..." if len(text) > 35 else text

    return "New Chat"


if "thread_id" not in st.session_state:
    st.session_state["thread_id"] = generate_thread_id()

if "chat_threads" not in st.session_state:
    st.session_state["chat_threads"] = extract_threads()

if "message_history" not in st.session_state:
    st.session_state["message_history"] = []


st.session_state["chat_threads"] = [
    thread_id
    for thread_id in st.session_state["chat_threads"]
    if load_convo(thread_id)
]


config = {
    "configurable": {
        "thread_id": st.session_state["thread_id"]
    }
}


st.sidebar.title("langGraph Chatbot")

if st.sidebar.button("New Chat"):
    reset_chat()
    st.rerun()


st.sidebar.header("Recent Conversations")

for thread_id in st.session_state["chat_threads"][::-1]:

    messages = load_convo(thread_id)

    if messages:
        title = generate_title(messages)
    else:
        continue

    if st.sidebar.button(title, key=f"thread_{thread_id}"):

        st.session_state["thread_id"] = thread_id

        temp_messages = []

        for message in messages:

            if isinstance(message, HumanMessage):
                role = "user"
            else:
                role = "assistant"

            temp_messages.append({
                "role": role,
                "content": message.content
            })

        st.session_state["message_history"] = temp_messages

        st.rerun()


for message in st.session_state["message_history"]:

    with st.chat_message(message["role"]):
        st.text(message["content"])


user_input = st.chat_input("Type here")


if user_input:

    if user_input.strip().lower() in ["exit", "quit", "bye", "end"]:
        st.write("Goodbye!")
        st.stop()


    if st.session_state["thread_id"] not in st.session_state["chat_threads"]:
        add_thread(st.session_state["thread_id"])


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


    st.rerun()
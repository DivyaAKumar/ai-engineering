import streamlit as st
import uuid
from copy import deepcopy

from backend_chatbot import chatbot
from langchain_core.messages import HumanMessage, AIMessage


st.set_page_config(
    page_title="AI Chat",
    layout="wide",
    initial_sidebar_state="expanded"
)


st.markdown("""
<style>
.stApp {
    background-color: #0f1117;
}

.block-container {
    max-width: 1050px;
    padding-top: 2rem;
    padding-bottom: 6rem;
}

[data-testid="stSidebar"] {
    background-color: #0b0d12;
    border-right: 1px solid #252832;
}

[data-testid="stSidebar"] .stButton button {
    border-radius: 10px;
}

[data-testid="stChatMessage"] {
    background: transparent !important;
    border: none !important;
    margin-bottom: 12px;
}

[data-testid="stChatMessageContent"] {
    border-radius: 18px !important;
    padding: 12px 17px !important;
}

[data-testid="stChatMessage"]:has(
    [data-testid="stChatMessageAvatarUser"]
) {
    justify-content: flex-end !important;
}

[data-testid="stChatMessage"]:has(
    [data-testid="stChatMessageAvatarUser"]
) [data-testid="stChatMessageContent"] {
    background-color: #2b2e3b !important;
    border-radius: 18px 18px 4px 18px !important;
    max-width: 70% !important;
}

[data-testid="stChatMessage"]:has(
    [data-testid="stChatMessageAvatarAssistant"]
) [data-testid="stChatMessageContent"] {
    background-color: #191c24 !important;
    border: 1px solid #252934 !important;
    border-radius: 18px 18px 18px 4px !important;
    max-width: 75% !important;
}

.edit-button button {
    width: 30px !important;
    min-width: 30px !important;
    height: 30px !important;
    padding: 0 !important;
    border-radius: 50% !important;
    background: transparent !important;
    border: none !important;
    color: #858994 !important;
    font-size: 15px !important;
}

.edit-button button:hover {
    background: #292d37 !important;
    color: #ffffff !important;
}

.recent-title {
    color: #8c909b;
    font-size: 12px;
    font-weight: 600;
    letter-spacing: 0.5px;
    margin-top: 20px;
    margin-bottom: 8px;
}

.chat-title {
    color: #f1f1f1;
    font-size: 15px;
    font-weight: 600;
}

.chat-subtitle {
    color: #777c88;
    font-size: 12px;
}

.welcome-title {
    text-align: center;
    font-size: 28px;
    font-weight: 600;
    color: #f1f1f1;
    margin-top: 150px;
}

.welcome-subtitle {
    text-align: center;
    font-size: 14px;
    color: #858995;
    margin-top: 8px;
}
</style>
""", unsafe_allow_html=True)


if "messages" not in st.session_state:
    st.session_state["messages"] = []

if "thread_id" not in st.session_state:
    st.session_state["thread_id"] = str(uuid.uuid4())

if "editing_index" not in st.session_state:
    st.session_state["editing_index"] = None

if "recent_conversations" not in st.session_state:
    st.session_state["recent_conversations"] = []


def new_chat():
    if st.session_state["messages"]:
        save_current_conversation()

    st.session_state["messages"] = []
    st.session_state["thread_id"] = str(uuid.uuid4())
    st.session_state["editing_index"] = None


def save_current_conversation():
    messages = st.session_state["messages"]

    if not messages:
        return

    first_user_message = next(
        (
            message.content
            for message in messages
            if isinstance(message, HumanMessage)
        ),
        "New conversation"
    )

    conversation = {
        "id": st.session_state["thread_id"],
        "title": first_user_message[:35],
        "messages": deepcopy(messages)
    }

    existing = [
        conversation_item
        for conversation_item in st.session_state["recent_conversations"]
        if conversation_item["id"] != conversation["id"]
    ]

    st.session_state["recent_conversations"] = [
        conversation
    ] + existing


def load_conversation(conversation):
    st.session_state["messages"] = deepcopy(
        conversation["messages"]
    )
    st.session_state["thread_id"] = conversation["id"]
    st.session_state["editing_index"] = None


def get_config():
    return {
        "configurable": {
            "thread_id": st.session_state["thread_id"]
        }
    }


def generate_response(messages):
    result = chatbot.invoke(
        {
            "messages": messages
        },
        config=get_config()
    )

    return result["messages"][-1]


with st.sidebar:

    st.markdown(
        """
        <div style="
            font-size: 26px;
            font-weight: 600;
            margin-bottom: 5px;
        ">
            AI Chat
        </div>

        <div style="
            color: #999999;
            font-size: 14px;
            margin-bottom: 25px;
        ">
            LangGraph-powered assistant
        </div>
        """,
        unsafe_allow_html=True
    )

    if st.button(
        "＋  New chat",
        use_container_width=True
    ):
        new_chat()
        st.rerun()

    if st.button(
        "⌫  Clear conversation",
        use_container_width=True
    ):
        st.session_state["messages"] = []
        st.session_state["thread_id"] = str(uuid.uuid4())
        st.session_state["editing_index"] = None
        st.rerun()

    st.divider()

    st.markdown(
        '<div class="recent-title">RECENT CONVERSATIONS</div>',
        unsafe_allow_html=True
    )

    recent = st.session_state["recent_conversations"]

    if not recent:
        st.caption("No recent conversations")

    else:
        for index, conversation in enumerate(recent[:10]):

            if st.button(
                conversation["title"],
                key=f"conversation_{conversation['id']}",
                use_container_width=True
            ):
                save_current_conversation()
                load_conversation(conversation)
                st.rerun()

    st.divider()

    st.caption(
        f"Messages: {len(st.session_state['messages'])}"
    )

    st.caption(
        f"Thread: {st.session_state['thread_id'][:12]}..."
    )


if not st.session_state["messages"]:

    st.markdown(
        '<div class="welcome-title">How can I help?</div>',
        unsafe_allow_html=True
    )

    st.markdown(
        '<div class="welcome-subtitle">'
        'Ask anything and start a conversation.'
        '</div>',
        unsafe_allow_html=True
    )


for index, message in enumerate(
    st.session_state["messages"]
):

    if isinstance(message, HumanMessage):

        left, middle, right = st.columns(
            [2.5, 6, 0.5]
        )

        with middle:

            with st.chat_message("user"):
                st.markdown(message.content)

        with right:

            st.markdown(
                '<div class="edit-button">',
                unsafe_allow_html=True
            )

            if st.button(
                "✎",
                key=f"edit_{index}",
                help="Edit message"
            ):
                st.session_state["editing_index"] = index
                st.rerun()

            st.markdown(
                "</div>",
                unsafe_allow_html=True
            )

        if st.session_state["editing_index"] == index:

            edited_text = st.text_area(
                "Edit message",
                value=message.content,
                key=f"edit_text_{index}",
                label_visibility="collapsed"
            )

            save_col, cancel_col = st.columns(2)

            with save_col:

                if st.button(
                    "Save & regenerate",
                    key=f"save_{index}",
                    use_container_width=True
                ):

                    if edited_text.strip():

                        previous_messages = (
                            st.session_state["messages"][:index]
                        )

                        edited_message = HumanMessage(
                            content=edited_text
                        )

                        new_messages = (
                            previous_messages
                            + [edited_message]
                        )

                        st.session_state["messages"] = (
                            new_messages
                        )

                        st.session_state["editing_index"] = None

                        with st.spinner("Thinking..."):

                            ai_message = generate_response(
                                new_messages
                            )

                        st.session_state["messages"].append(
                            AIMessage(
                                content=ai_message.content
                            )
                        )

                        st.rerun()

            with cancel_col:

                if st.button(
                    "Cancel",
                    key=f"cancel_{index}",
                    use_container_width=True
                ):
                    st.session_state["editing_index"] = None
                    st.rerun()

    elif isinstance(message, AIMessage):

        with st.chat_message("assistant"):
            st.markdown(message.content)


user_input = st.chat_input(
    "Message AI Assistant..."
)


if user_input:

    if user_input.strip().lower() in [
        "exit",
        "quit",
        "bye",
        "end"
    ]:
        st.write("Goodbye!")
        st.stop()

    user_message = HumanMessage(
        content=user_input
    )

    st.session_state["messages"].append(
        user_message
    )

    messages_for_llm = st.session_state["messages"]

    with st.spinner("Thinking..."):

        ai_message = generate_response(
            messages_for_llm
        )

    st.session_state["messages"].append(
        AIMessage(
            content=ai_message.content
        )
    )

    st.rerun()
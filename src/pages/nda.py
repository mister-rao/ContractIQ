import os
import streamlit as st

from langchain_core.messages import HumanMessage, SystemMessage, AIMessage
from langgraph.graph import MessagesState
from pages.graphs.nda import graph


if "openai_api_key" not in st.session_state:
    st.session_state["openai_api_key"] = ""


def callback():
    st.session_state["openai_api_key"] = st.session_state.api_key


config = {"configurable": {"thread_id": 1}, "recursion_limit": 40}

with st.sidebar:
    st.text_input(
        "OpenAI API Key",
        key="api_key",
        type="password",
        value=st.session_state["openai_api_key"] or "",
        on_change=callback,
    )
    "[Get an OpenAI API key](https://platform.openai.com/account/api-keys)"
    "[View the source code]()"

st.title("📝 Draft NDA")
st.caption("🚀 An AI assistant to draft NDAs")


if "nda_messages" not in st.session_state:
    st.session_state["nda_messages"] = [
        AIMessage(content="Hey! I can help you draft an NDA!")
    ]

for msg in st.session_state.nda_messages:
    role = "assistant" if type(msg) == SystemMessage or AIMessage else "user"
    content = msg.content
    st.chat_message(role).write(content)


if prompt := st.chat_input():
    if not st.session_state.openai_api_key:
        st.info("Please add your OpenAI API key to continue.")
        st.stop()

    os.environ["OPENAI_API_KEY"] = st.session_state.openai_api_key
    st.session_state.nda_messages.append(HumanMessage(content=prompt))
    st.chat_message("user").write(prompt)
    response = graph.invoke({"messages": st.session_state.nda_messages}, config)
    msg = response["messages"][-1].content
    print(msg)
    st.session_state.nda_messages.append(SystemMessage(content=msg))
    st.chat_message("assistant").write(msg)

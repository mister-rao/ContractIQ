import os
import streamlit as st

from langchain_core.messages import HumanMessage, SystemMessage, AIMessage
from pages.graphs.employee_agreement import graph

config = {"configurable": {"thread_id": 1}, "recursion_limit": 40}

if "openai_api_key" not in st.session_state:
    st.session_state["openai_api_key"] = ""


def callback():
    st.session_state["openai_api_key"] = st.session_state.api_key


with st.sidebar:
    st.text_input(
        "OpenAI API Key",
        key="api_key",
        type="password",
        value=st.session_state["openai_api_key"],
        on_change=callback,
    )
    "[Get an OpenAI API key](https://platform.openai.com/account/api-keys)"
    "[View the source code]()"

st.title("📝 Draft Employee Agreement")
st.caption("🚀 An AI assistant to draft Employee Agreement")


if "ea_messages" not in st.session_state:
    st.session_state["ea_messages"] = [
        AIMessage(content="Hey! I can help you draft an Employee Agreement!")
    ]

for msg in st.session_state.ea_messages:
    role = "assistant" if type(msg) == SystemMessage or AIMessage else "user"
    content = msg.content
    st.chat_message(role).write(content)


if prompt := st.chat_input():
    if not st.session_state.openai_api_key:
        st.info("Please add your OpenAI API key to continue.")
        st.stop()

    os.environ["OPENAI_API_KEY"] = st.session_state.openai_api_key
    st.session_state.ea_messages.append(HumanMessage(content=prompt))
    st.chat_message("user").write(prompt)
    response = graph.invoke({"messages": st.session_state.ea_messages}, config)
    msg = response["messages"][-1].content
    st.session_state.ea_messages.append(SystemMessage(content=msg))
    st.chat_message("assistant").write(msg)

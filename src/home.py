from openai import OpenAI
import streamlit as st

st.set_page_config(
    page_title="ContractIQ",
    page_icon="📑",
)

with st.sidebar:
    "[Get an OpenAI API key](https://platform.openai.com/account/api-keys)"
    "[View the source code]()"


st.title("💬 ContractIQ")
st.caption("🚀 An AI assistant to draft NDAs and Employee Agreements")


if "openai_api_key" not in st.session_state:
    st.session_state["openai_api_key"] = ""

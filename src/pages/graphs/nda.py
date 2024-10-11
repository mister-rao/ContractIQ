from langgraph.graph import MessagesState
from pages.tools.nda import tools
from langchain_core.messages import SystemMessage
from langchain_openai import ChatOpenAI

from langgraph.graph import START, StateGraph
from langgraph.prebuilt import tools_condition
from langgraph.prebuilt import ToolNode

system_message = SystemMessage(
    content="""
You are an expert in drafting Non-Disclosure Agreement. Ask the user for required 
information and draft an NDA.

Ask for the required details in groups, don't overwhelm user by asking all at once. 
Don't ask the user for the default information.

These are some of the default values for the NDA. present this to the user at the end before finalising the draft.

survival_period: 5 years
post_binding_agreement_period: 2 years
governing_laws: India
jurisdiction_city: Bangalore
arbitration_act: Indian Arbitration & Conciliation Act, 1996
arbitration_city: Bangalore
arbitration_language: English
"""
)

llm = ChatOpenAI(model="gpt-3.5-turbo")

llm_with_tools = llm.bind_tools(tools)


# Node
def assistant(state: MessagesState):
    return {"messages": [llm_with_tools.invoke([system_message] + state["messages"])]}


# Graph
builder = StateGraph(MessagesState)

# nodes: Orchestrator and tools
builder.add_node("chatbot", assistant)

# tools
builder.add_node("tools", ToolNode(tools))

# edges
builder.add_edge(START, "chatbot")

builder.add_conditional_edges("chatbot", tools_condition)
builder.add_edge("tools", "chatbot")


graph = builder.compile()

from langchain_core.globals import set_llm_cache
from langchain_community.cache import SQLiteCache
from langchain.chat_models import init_chat_model
from langgraph.graph import StateGraph, START, END

from config.config import MODEL_NAME, TOGETHER_API_KEY, MODEL_PROVIDER
from state.graph_state import GraphState
from nodes.planner_node import planner_node
from nodes.researcher_node import researcher_node
from nodes.contitions.conditions import check_research_complete
from nodes.summarizer_node import summarizer_node

set_llm_cache(SQLiteCache(database_path="db/.langchain_cache.db"))

model = init_chat_model(
    model=MODEL_NAME,
    api_key=TOGETHER_API_KEY,
    model_provider=MODEL_PROVIDER,
    temperature=0.7,
)

# Create graph builder
workflow = StateGraph(GraphState)

# Add planner node
workflow.add_node("planner", lambda state: planner_node(state, model))
workflow.add_node("researcher", lambda state: researcher_node(state, model))
workflow.add_node("summarizer", lambda state: summarizer_node(state, model))

# Add edges
workflow.add_edge(START, "planner")
workflow.add_edge("planner", "researcher")

workflow.add_conditional_edges(
    "researcher", check_research_complete, {"done": "summarizer", "not_done": "researcher"}
)

workflow.add_edge("summarizer", END)

# Compile
graph = workflow.compile()

from typing import Dict
from state.graph_state import GraphState
from agents.summarizer_agent import summarizer_agent

def summarizer_node(state: GraphState, model) -> Dict:
    research_notes = state.get("research_notes", {})
    
    combined = "\n".join([f"{k}: {v}" for k, v in research_notes.items()])

    summary = summarizer_agent(model, combined)
    
    state["summary"] = summary
    return state
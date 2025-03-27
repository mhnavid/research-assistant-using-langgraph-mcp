from typing import Dict

from state.graph_state import GraphState
from agents.researcher_agent import researcher_agent

def researcher_node(state: GraphState, model) -> Dict:
    subtopics = state["subtopics"]
    research_notes = state.get("research_notes", {})

    # Find the next subtopic that hasn't been researched yet
    next_subtopic = next((s for s in subtopics if s not in research_notes), None)

    if next_subtopic is None:
        return state  

    summary = researcher_agent(model, next_subtopic)

    research_notes[next_subtopic] = summary
    
    state["research_notes"] = research_notes
    return state
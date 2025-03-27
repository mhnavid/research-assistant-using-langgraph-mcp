from state.graph_state import GraphState

def check_research_complete(state: GraphState) -> bool:
    subtopics = state.get("subtopics", [])
    research_notes = state.get("research_notes", {})

    is_complete = True
    for subtopic in subtopics:
        if subtopic not in research_notes:
            is_complete = False
            break
        
    if is_complete:
        return "done"
    
    return "not_done"
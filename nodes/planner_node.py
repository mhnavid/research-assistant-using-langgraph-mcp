from typing import Dict
from state.graph_state import GraphState
from agents.planner_agent import planner_agent

def planner_node(state: GraphState, model) -> Dict:
    topic = state["topic"]
    subtopics = planner_agent(model, topic)
    state["subtopics"] = subtopics
    return state
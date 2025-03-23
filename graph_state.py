from typing_extensions import TypedDict
from typing import List, Dict


class GraphState(TypedDict):
    topic: str
    subtopics: List[str]
    research_notes: Dict[str, str]
    summary: str

from mcp.server.fastmcp import FastMCP
import json

from graph_workflow_builder import graph

mcp = FastMCP("AI Research Assistant")

@mcp.tool()
def research(topic: str) -> dict:
    """Run the full research workflow for a given topic using LangGraph"""
    initial_state = {"topic": topic}
    result = graph.invoke(initial_state)
    return json.dumps({
        "topic": topic,
        "subtopics": result.get("subtopics", []),
        "research_notes": result.get("research_notes", {}),
        "summary": result.get("summary", "")
    })


if __name__ == "__main__":
    mcp.run()
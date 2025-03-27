import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from graphs.graph_workflow_builder import graph

# Topic to research
topic = "The role of AI in climate change adaptation"

initial_state = {"topic": topic}

result = graph.invoke(initial_state)

print("\n📋 Subtopics:")
for sub in result["subtopics"]:
    print(f"🔹 {sub}")

print("\n📚 Research Notes:")
for sub, summary in result["research_notes"].items():
    print(f"🔸 {sub}\n{summary}\n")
    
print("\n📝 Final Summary:")
print(result["summary"])
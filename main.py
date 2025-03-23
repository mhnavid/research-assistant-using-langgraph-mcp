from langchain_core.globals import set_llm_cache
from langchain_community.cache import SQLiteCache
from langchain.chat_models import init_chat_model

from config import MODEL_NAME, TOGETHER_API_KEY, MODEL_PROVIDER
from planner_agent import planner_agent
from researcher_agent import researcher_agent

set_llm_cache(SQLiteCache(database_path=".langchain_cache.db"))


model = init_chat_model(
    model=MODEL_NAME,
    api_key=TOGETHER_API_KEY,
    model_provider=MODEL_PROVIDER,
    temperature=0.7,
)


def run_research_pipeline(topic: str):
    subtopics = planner_agent(model, topic)
    research_notes = {}

    for sub in subtopics:
        description = researcher_agent(model, sub)
        research_notes[sub] = description

    return research_notes


topic = "The impact of climate change on the economy"
notes = run_research_pipeline(topic)

for sub, summary in notes.items():
    print(f"🔹 {sub}\n{summary}\n")

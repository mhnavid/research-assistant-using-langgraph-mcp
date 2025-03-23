from langchain.chat_models import init_chat_model
from langchain_core.prompts import PromptTemplate
from langchain_core.globals import set_llm_cache
from langchain_core.caches import InMemoryCache

from config import MODEL_NAME, TOGETHER_API_KEY, MODEL_PROVIDER

model = init_chat_model(
    model=MODEL_NAME,
    api_key=TOGETHER_API_KEY,
    model_provider=MODEL_PROVIDER,
    temperature=0.7,
)

set_llm_cache(InMemoryCache())

prompt_template = PromptTemplate.from_template(
    "I'm providing a research topic. Break the topic: '{topic}' into 2 subtopics for in-depth research. Provide only the name of the subtopics."
)


def planner_agent(topic: str) -> list[str]:
    prompt = prompt_template.format_prompt(topic=topic)
    response = model.invoke(prompt)

    subtopics = []
    for line in response.content.strip().split("\n"):
        if line.strip():
            subtopic = line.strip().lstrip("0123456789. )-")
            subtopics.append(subtopic.strip())

    return subtopics

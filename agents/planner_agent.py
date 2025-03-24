from langchain_core.prompts import PromptTemplate

prompt_template = PromptTemplate.from_template(
    "I'm providing a research topic. Break the topic: '{topic}' into 2 subtopics for in-depth research. Provide only the name of the subtopics."
)


def planner_agent(model: any, topic: str) -> list[str]:
    prompt = prompt_template.format_prompt(topic=topic)
    response = model.invoke(prompt)

    subtopics = []
    for line in response.content.strip().split("\n"):
        if line.strip():
            subtopic = line.strip().lstrip("0123456789. )-")
            subtopics.append(subtopic.strip())

    return subtopics

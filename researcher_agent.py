from langchain_core.prompts import PromptTemplate

prompt_template = PromptTemplate.from_template(
    "Think as a researcher. Write a concise and simple two lines about the {subtopic}"
)

def researcher_agent(model: any, subtopic: str) -> str:
    prompt = prompt_template.format_prompt(subtopic=subtopic)
    response = model.invoke(prompt)
    return response.content.strip()
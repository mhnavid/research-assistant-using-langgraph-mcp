from langchain_core.prompts import PromptTemplate

prompt_template = PromptTemplate.from_template(
    "Based on the following subtopic and descriptions, write a clear and concise overall summary of {description} in a few words. Maintain simple and concise language."
)

def summarizer_agent(model: any, description: str) -> str:
    prompt = prompt_template.format_prompt(description=description)
    response = model.invoke(prompt)
    return response.content.strip()
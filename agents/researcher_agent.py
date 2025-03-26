from langchain_core.prompts import PromptTemplate

from rag.rag_pipeline import get_context_from_subtopic

prompt_template = PromptTemplate.from_template(
    """Think as a researcher. Write a concise and simple two lines explanation about the {subtopic}
    context: {context}
    """
)
def researcher_agent(model: any, subtopic: str) -> str:
    context = get_context_from_subtopic(subtopic)

    if not context:
        print(f"No context found for {subtopic}. Using fallback mode.")
        fallback_prompt = f"Think as a researcher. Write a concise and simple two lines about the {subtopic}"
        return model.invoke(fallback_prompt).content.strip()
    
    prompt = prompt_template.format_prompt(subtopic=subtopic, context=context)
    response = model.invoke(prompt)
    return response.content.strip()

from langchain_core.prompts import PromptTemplate

prompt = PromptTemplate.from_template(
    "Explain the research paper {paper_name}."
)

formatted_prompt = prompt.format(
    paper_name="Attention Is All You Need"
)

print(formatted_prompt)
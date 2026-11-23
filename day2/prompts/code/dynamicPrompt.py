from langchain_core.prompts import PromptTemplate
# from openai import OpenAI
# import os
# from dotenv import load_dotenv
prompt = PromptTemplate.from_template(
    """
    You are an AI research assistant.

    Explain the research paper: {paper_name}

    Explanation level: {difficulty}
    Maximum length: {word_limit} words.

    Structure your response using:
    1. Introduction
    2. Main concepts
    3. Architecture
    4. Key contributions
    5. Limitations
    """
)

formatted_prompt = prompt.format(
    paper_name="Attention Is All You Need",
    difficulty="Beginner",
    word_limit=500
)

print(formatted_prompt)
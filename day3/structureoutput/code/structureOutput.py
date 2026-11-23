

from anyio import Path
from langchain_openai import ChatOpenAI
from typing_extensions import TypedDict
from typing import List
resume_text = """
My name is MIlan Paudel.

I am a Python Backend Developer with
3 years of professional experience.

I previously worked at ABC Technologies
from 2022 to 2025.

My technical skills include:
Python, FastAPI, PostgreSQL, Docker,
AWS and Apache Kafka.

I have a Bachelor's degree in Computer Science.

My email is john@example.com.
"""
from dotenv import load_dotenv
import os
load_dotenv()
class Resume(TypedDict):
    name: str
    email: str
    job_title: str
    experience_years: int
    skills: List[str]
    education: str


from langchain_openai import ChatOpenAI
env_path = Path(__file__).with_name(".env")
llm = ChatOpenAI(
    model="gpt-4.1-mini",
    temperature=0,
    api_key=os.getenv("OPENAI_API_KEY")
)

structured_llm = llm.with_structured_output(Resume)

result = structured_llm.invoke(resume_text)

print(result)
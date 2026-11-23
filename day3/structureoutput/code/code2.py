
import os

from dotenv import load_dotenv
from pydantic import BaseModel, Field, EmailStr
from typing import List

from langchain_openai import ChatOpenAI


# 1. Load environment variables
load_dotenv()


# 2. Define the Pydantic schema
class Resume(BaseModel):

    name: str = Field(
        description="Full name of the candidate"
    )

    email: EmailStr

    job_title: str

    experience_years: int = Field(
        ge=0,
        le=50
    )

    skills: List[str]

    education: str


# 3. Initialize the LLM
llm = ChatOpenAI(
    model="gpt-4.1-mini",
    temperature=0,
    api_key=os.getenv("OPENAI_API_KEY")
)


# 4. Enable structured output
structured_llm = llm.with_structured_output(
    Resume
)


# 5. Sample resume
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


# 6. Invoke the model
result = structured_llm.invoke(resume_text)


# 7. Display the extracted information
print("Candidate Name:", result.name)

print("Email:", result.email)

print("Job Title:", result.job_title)

print("Experience:", result.experience_years)

print("Skills:", result.skills)

print("Education:", result.education)


# 8. Convert to dictionary
candidate_data = result.model_dump()

print("\nStructured Dictionary:")
print(candidate_data)

1. What is Structured Output?
Structured output is the process of instructing an LLM to return information in a predefined format or schema rather than generating free-form text.

Normally, when you ask an LLM a question, it responds with natural language. The response might be correct, but its format can vary.

For example, imagine you are building a resume-processing application.

You provide this resume to an LLM:
My name is John Smith. I have 3 years of experience as a Python developer. I worked at ABC Technologies from 2022 to 2025. I have experience with Python, FastAPI, PostgreSQL, and Docker.

Without structured output
The LLM might return:

"John Smith is a Python developer with three years of experience. He has worked at ABC Technologies and has experience with several backend technologies."

This is understandable to humans, but difficult for an application to process automatically.
With structured output
We instruct the LLM to follow a predefined schema.
{
    "name": "John Smith",
    "experience_years": 3,
    "job_title": "Python Developer",
    "company": "ABC Technologies",
    "skills": [
        "Python",
        "FastAPI",
        "PostgreSQL",
        "Docker"
    ]
}

2. Key Use Cases
Let's understand the three major use cases.
A. Data Extraction
Data extraction means extracting specific information from unstructured data and converting it into structured records.

Example: Resume extraction

Suppose an HR application receives 1,000 resumes in PDF format.

Each resume has different formatting and writing styles.

One candidate might write:
Experienced Python developer with 3 years of experience.

Another might write:
Worked as a backend engineer for three years, primarily using Python.

Although the wording differs, we want the same structured information.

Our expected schema:
{
    "candidate_name": "string",
    "experience_years": "integer",
    "primary_skill": "string",
    "email": "string"
}


Where does this information go?
- PostgreSQL or MySQL database.
- HR management systems.
- Data warehouses.
- Candidate filtering applications.
For example, we can query the database to find all candidates with at least three years of Python experience.

This is particularly useful when building LLM-powered data ingestion pipelines.


C. Building Agents
This is one of the most interesting use cases.

An AI agent is an LLM-powered system that can decide what action to perform and interact with external tools.

For example, suppose we provide an agent with a calculator tool.

User:
Calculate 250 multiplied by 40.

The LLM needs to provide structured arguments to the calculator.

Expected tool input:
{
    "a": 250,
    "b": 40,
    "operation": "multiply"
}


The calculator receives these arguments and executes:
250 * 40



Result:
10000


The agent then communicates the result to the user.
Agent tool-calling workflow
User: Calculate 250 × 40

LLM decides to call calculator

Generates structured arguments


Calculator Tool

Receives a=250, b=40, operation=multiply


Result: 10,000


Notice that the LLM does not necessarily perform the calculation itself. It provides the required structured arguments to a specialized tool.

This is why structured output is important in agentic applications.
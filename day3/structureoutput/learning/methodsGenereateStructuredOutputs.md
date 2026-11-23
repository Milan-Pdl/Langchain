A. TypedDict
TypedDict is a Python feature used to define the expected structure of a dictionary.

It specifies:
- What keys should exist.
- What data type each key should contain.
Example:
from typing import TypedDictclass Student(TypedDict):    name: str    age: int    course: str



Here, we define a structure called Student.

A dictionary following this structure looks like:
student = {    "name": "Milan",    "age": 22,    "course": "Data Engineering"}



The expected types are:
Field	Data type
name	str
age	int
course	str

Important limitation:

TypedDict primarily provides static type information. It does not automatically validate dictionary values at runtime.

For example:
student = {    "name": "Milan",    "age": "twenty-two",    "course": "Data Engineering"}



Python will not automatically reject this dictionary just because age is a string instead of an integer.

So, TypedDict is useful for defining expected structure, but it does not provide strict runtime validation by itself.



B. Pydantic
Recommended for validation
Pydantic is a Python library used for data validation, parsing, and serialization.

Unlike TypedDict, Pydantic provides runtime validation.

It also supports:
- Required fields.
- Default values.
- Numeric constraints.
- String validation.
- Automatic type conversion in supported cases.
Let's create the same student schema using Pydantic.
from pydantic import BaseModel, Field

class Student(BaseModel):

    name: str

    age: int = Field(
        gt=0,
        lt=100
    )

    course: str

    cgpa: float = Field(
        ge=0,
        le=4.0,
        default=0.0
    )


Let's understand the constraints.
Field	Validation
name	Must be a string
age	Greater than 0 and less than 100
course	Must be a string
cgpa	Between 0 and 4.0, default 0.0

Now let's create a student object.
student = Student(    name="Milan",    age=22,    course="Data Engineering",    cgpa=3.6)print(student)



Output:
name='Milan'
age=22
course='Data Engineering'
cgpa=3.6


What happens if we provide an invalid age?
student = Student(    name="Milan",    age=-5,    course="Data Engineering")



Pydantic raises a validation error because the age must be greater than zero.

Why is Pydantic important in LangChain?

We can provide a Pydantic model as the schema for an LLM's structured response.

LangChain can use this schema to guide the model and parse the returned information into a validated Python object.

C. JSON Schema
JSON Schema is a standard format for describing the structure and validation rules of JSON data.

It is particularly useful when different programming languages or technology stacks need to share the same schema.

For example, imagine you have:
- Python backend using FastAPI.
- JavaScript frontend using React.
- Java microservice.
- An LLM application using LangChain.
Instead of defining different schemas independently, you can share a JSON Schema.

Example:
student_schema = {    "title": "Student",    "type": "object",    "properties": {        "name": {            "type": "string"        },        "age": {            "type": "integer",            "minimum": 1,            "maximum": 99        },        "course": {            "type": "string"        }    },    "required": [        "name",        "age",        "course"    ]}



This schema defines:
- The output must be a JSON object.
- name must be a string.
- age must be an integer between 1 and 99.
- course must be a string.
- All three fields are required.
Comparison of the three methods
Feature	TypedDict	Pydantic	JSON Schema
Defines fields	Yes	Yes	Yes
Defines types	Yes	Yes	Yes
Runtime validation	No, not by itself	Yes	Requires a validator
Constraints	Limited	Yes	Yes
Default values	Not runtime-enforced	Yes	Yes, but defaults are annotations
Language independent	No	No	Yes

My recommendation: Start with Pydantic when building LangChain applications in Python. It provides a convenient combination of schema definition, validation, and parsing.
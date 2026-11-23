3. Types of Output Parsers
We will explore four important parsers:
1. StrOutputParser
2. JsonOutputParser
3. StructuredOutputParser
4. PydanticOutputParser
Let's understand them individually.
A. String Output Parser
Simplest parser
StrOutputParser extracts the textual content from an LLM response.

Let's understand the problem first.

When you invoke a chat model in LangChain:

from langchain_openai import ChatOpenAI

llm = ChatOpenAI(
    model="gpt-4.1-mini"
)

response = llm.invoke(
    "Explain what data engineering is."
)

print(response)

The model generally returns an AIMessage object.

Conceptually, it looks like:
AIMessage(
    content="Data engineering is the practice of..."
)

But LangChain provides a convenient component for this: StrOutputParser.
Implementation

from langchain_core.output_parsers import StrOutputParser

parser = StrOutputParser()

result = parser.invoke(response)

print(result)

Data engineering is the practice of designing,
building, and maintaining systems that collect,
process, and store data.

Now we have the plain text instead of the complete AIMessage object.
Why is it useful?
Imagine building a chain with multiple LLMs.

The first LLM generates a summary, and the second LLM generates questions based on that summary.

We don't necessarily need the complete message object. We just need its text.

This is where StrOutputParser is useful.
Using LCEL (LangChain Expression Language)
One of the most common patterns in LangChain is:



from langchain_openai import ChatOpenAI

llm = ChatOpenAI(model="gpt-4.1-mini")

response = llm.invoke(
    "Explain the Attention Is All You Need paper "
    "in simple language."
)

print(response.content)
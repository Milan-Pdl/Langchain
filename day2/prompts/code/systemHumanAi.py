from langchain_openai import ChatOpenAI

from langchain_core.messages import (
    SystemMessage,
    HumanMessage
)

llm = ChatOpenAI(model="gpt-4.1-mini")

messages = [
    SystemMessage(
        content="You are a helpful customer support assistant."
    ),
    HumanMessage(
        content="Where is my refund?"
    )
]

response = llm.invoke(messages)

print(response.content)

from langchain_core.prompts import (
    ChatPromptTemplate,
    MessagesPlaceholder
)
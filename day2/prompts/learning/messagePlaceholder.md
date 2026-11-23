What is a Message Placeholder?
LangChain provides MessagesPlaceholder to dynamically insert a list of messages into a chat prompt.

Instead of manually writing all previous messages inside the template, you reserve a place for them.

Let's implement it.

from langchain_core.prompts import (
    ChatPromptTemplate,
    MessagesPlaceholder
)

chat_prompt = ChatPromptTemplate.from_messages([

    (
        "system",
        """
        You are a helpful customer support assistant.
        Help users with refund-related questions.
        """
    ),

    MessagesPlaceholder(variable_name="chat_history"),

    (
        "human",
        "{user_input}"
    )

])

Let's understand each part.

1. System message

Defines the chatbot's role and behavior.

2. MessagesPlaceholder

MessagesPlaceholder(
    variable_name="chat_history"
)

This tells LangChain:

"At this position, insert the conversation history supplied through the chat_history variable."

3. Human message
("human", "{user_input}")

This represents the latest user input.
Now let's provide the conversation history.

from langchain_core.messages import (
    HumanMessage,
    AIMessage
)

chat_history = [

    HumanMessage(
        content="I want a refund for my order."
    ),

    AIMessage(
        content="Sure! Please provide your order ID."
    ),

    HumanMessage(
        content="My order ID is ORD12345."
    ),

    AIMessage(
        content="Thank you. I'll help check your refund."
    )

]

response_prompt = chat_prompt.invoke({

    "chat_history": chat_history,

    "user_input": "How long will it take?"

})

print(response_prompt)

What happens?

LangChain inserts the previous conversation at the exact location of MessagesPlaceholder.

The resulting message structure is conceptually:

SYSTEM:
You are a helpful customer support assistant.

HUMAN:
I want a refund for my order.

AI:
Sure! Please provide your order ID.

HUMAN:
My order ID is ORD12345.

AI:
Thank you. I'll help check your refund.

HUMAN:
How long will it take?

Now the model has the relevant conversational context.

from langchain_openai import ChatOpenAI

llm = ChatOpenAI(model="gpt-4.1-mini")

chain = chat_prompt | llm

response = chain.invoke({

    "chat_history": chat_history,

    "user_input": "How long will it take?"

})

print(response.content) 
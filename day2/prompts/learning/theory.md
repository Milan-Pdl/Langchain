A. System Message
The system message defines the AI's behavior, role, and general instructions.

Example:
from langchain_core.messages import SystemMessage

system_message = SystemMessage(
    content="""
    You are a professional customer support assistant.

    Be polite and helpful.
    Provide clear answers.
    Never invent refund information.
    """
)



Think of this as the general operating instructions for the assistant.
B. Human Message
The human message represents input from the user.
from langchain_core.messages import HumanMessage

human_message = HumanMessage(
    content="Where is my refund?"
)



C. AI Message
The AI message represents the assistant's response.
from langchain_core.messages import AIMessage

ai_message = AIMessage(
    content="Your refund is currently being processed."
)
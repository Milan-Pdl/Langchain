from langchain_core.prompts import PromptTemplate
from langchain_openai import ChatOpenAI
from langchain_core.output_parsers import StrOutputParser

# 1. Create prompt template
prompt = PromptTemplate.from_template(
    "Summarize this paper in 200 words: {paper}"
)

# 2. Initialize LLM
llm = ChatOpenAI(model="gpt-4o-mini")
#chatopenai is a wrapper of openai that provides a more convenient 
# interface for interacting with OpenAI's chat models. It simplifies the process of sending messages to the model 
# and receiving responses, making it easier to integrate into applications.
# 3. Create output parser
parser = StrOutputParser()

# 4. Connect everything into a chain
chain = prompt | llm | parser

# 5. Execute the chain
result = chain.invoke({
    "paper": "Your research paper content..."
})

print(result)
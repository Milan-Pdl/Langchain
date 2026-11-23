from openai import OpenAI
from dotenv import load_dotenv
import os
from pathlib import Path

env_path = Path(__file__).with_name(".env")
load_dotenv(env_path)

api_key = os.getenv("OPENAI_API_KEY")
if not api_key or api_key.startswith("replace-with"):
    raise RuntimeError(
        "OPENAI_API_KEY is missing. Add a valid key to day2/code/.env."
    )

client = OpenAI(api_key=api_key)

response = client.responses.create(
    model="gpt-4o-mini",
    instructions="Talk like Lionel Messi.",
    input="suggest 5 boys name.",
)

print(response)
print(env_path)
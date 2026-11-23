import os
from huggingface_hub import InferenceClient
from dotenv import load_dotenv
load_dotenv()
import pathlib
enc_path=pathlib.Path(__file__).with_name(".env")
# Initialize client with your HF_TOKEN
client = InferenceClient(api_key=os.environ.get("HF_TOKEN"))

completion = client.chat.completions.create(
    model="deepseek-ai/DeepSeek-V3", # Or any supported model ID from the Hub
    messages=[
        {"role": "user", "content": "Explain async/await in JavaScript briefly."}
    ],
    max_tokens=200
)

print(completion.choices[0].message.content)
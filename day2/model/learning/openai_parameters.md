# OpenAI Client Parameters

## 1. Constructor Parameters vs. Request Parameters

Parameters passed to `OpenAI(...)` configure the API client, while parameters passed to
`client.responses.create(...)` configure an individual model response.

```python
client = OpenAI(
    api_key=api_key,
    timeout=30,
)

response = client.responses.create(
    model="gpt-4o-mini",
    input="Explain Python variables.",
)
```

Passing `temperature`, `max_output_tokens`, or `top_p` to `OpenAI(...)` is incorrect.
Those parameters belong in `responses.create(...)`.

## 2. `OpenAI(...)` Constructor Parameters

### `api_key`

Authenticates the application with OpenAI.

```python
client = OpenAI(api_key=api_key)
```

It is better to store the key in an environment variable or `.env` file rather than
writing it directly in source code.

```env
OPENAI_API_KEY=your-api-key
```

```python
import os

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
```

### `organization`

Specifies an organization if the account belongs to multiple organizations.

```python
client = OpenAI(
    api_key=api_key,
    organization="org-example",
)
```

### `project`

Specifies a project associated with the API key.

```python
client = OpenAI(
    api_key=api_key,
    project="proj_example",
)
```

### `base_url`

Changes the API endpoint. This is normally only needed for approved API-compatible
services or proxies.

```python
client = OpenAI(
    api_key=api_key,
    base_url="https://api.openai.com/v1",
)
```

### `timeout`

Sets how many seconds the client waits before timing out a network request.

```python
client = OpenAI(
    api_key=api_key,
    timeout=30,
)
```

The timeout can also be set for one request:

```python
response = client.responses.create(
    model="gpt-4o-mini",
    input="Hello",
    timeout=30,
)
```

### `max_retries`

Defines how many times the SDK retries a failed request for eligible errors.

```python
client = OpenAI(
    api_key=api_key,
    max_retries=3,
)
```

### `default_headers`

Adds custom HTTP headers to requests.

```python
client = OpenAI(
    api_key=api_key,
    default_headers={
        "X-Application-Name": "learning-app",
    },
)
```

Do not use custom headers to send credentials that already belong to the SDK.

### `http_client`

Allows a custom `httpx` client to be provided, for example for a proxy or custom
transport.

```python
import httpx
from openai import OpenAI

http_client = httpx.Client(timeout=30)

client = OpenAI(
    api_key=api_key,
    http_client=http_client,
)
```

## 3. Important `responses.create(...)` Parameters

### `model`

Selects the model used to generate the response.

```python
response = client.responses.create(
    model="gpt-4o-mini",
    input="Suggest five boy names.",
)
```

Model availability and pricing depend on the account and provider.

### `input`

Contains the prompt or input message.

```python
response = client.responses.create(
    model="gpt-4o-mini",
    input="Write a short Python function that adds two numbers.",
)
```

### `instructions`

Defines the model's behavior for the current response.

```python
response = client.responses.create(
    model="gpt-4o-mini",
    instructions="You are a Python tutor. Use simple language.",
    input="What is a list?",
)
```

### `temperature`

Controls randomness.

- Lower values such as `0.0` to `0.3` produce more focused and predictable answers.
- Higher values such as `0.7` to `1.0` produce more varied answers.

```python
response = client.responses.create(
    model="gpt-4o-mini",
    input="Write a creative name for a coffee shop.",
    temperature=0.9,
)
```

For factual answers, use a low temperature:

```python
temperature=0.2
```

### `max_output_tokens`

Limits the maximum number of tokens generated in the response.

```python
response = client.responses.create(
    model="gpt-4o-mini",
    input="Summarize: Artificial intelligence helps computers perform tasks.",
    max_output_tokens=100,
)
```

For the Responses API, use `max_output_tokens`; it is not `max_tokens`.

Tokens are pieces of text, not exactly the same as words. A token may contain one or
more characters.

### `top_p`

Controls nucleus sampling. The model considers a probability-based set of likely next
tokens.

```python
response = client.responses.create(
    model="gpt-4o-mini",
    input="Write a poem about the sea.",
    top_p=0.8,
)
```

Avoid changing both `temperature` and `top_p` unless the effect is intentional.
Usually, adjust one of them.

### `reasoning`

Configures reasoning effort for models that support reasoning.

```python
response = client.responses.create(
    model="an-supported-reasoning-model",
    input="Solve this logic problem step by step.",
    reasoning={"effort": "low"},
)
```

Common values may include `low`, `medium`, and `high`, but they must be supported by
the selected model.

Do not assume that every model accepts the `reasoning` parameter.

### `stream`

Streams the response while it is being generated instead of waiting for the complete
result.

```python
stream = client.responses.create(
    model="gpt-4o-mini",
    input="Explain recursion.",
    stream=True,
)

for event in stream:
    if event.type == "response.output_text.delta":
        print(event.delta, end="", flush=True)
```

Streaming is useful for chat interfaces because users see output earlier.

### `store`

Controls whether OpenAI stores the response according to API and account settings.

```python
response = client.responses.create(
    model="gpt-4o-mini",
    input="What is Python?",
    store=True,
)
```

Use project/account data-retention settings and API policies to decide the appropriate
value.

### `previous_response_id`

References a previous response for response-based conversation continuity.

```python
first = client.responses.create(
    model="gpt-4o-mini",
    input="My favorite language is Python.",
)

second = client.responses.create(
    model="gpt-4o-mini",
    input="What did I say my favorite language was?",
    previous_response_id=first.id,
)
```

Chat applications can alternatively send the complete conversation in `input`.

### `conversation`

Connects the request to a conversation resource when using the Conversations API.

```python
response = client.responses.create(
    model="gpt-4o-mini",
    conversation="conv_example",
    input="Continue our conversation.",
)
```

Use a valid conversation ID created or obtained through your OpenAI workflow.

### `metadata`

Attaches custom key-value data for application tracking.

```python
response = client.responses.create(
    model="gpt-4o-mini",
    input="Summarize the product description.",
    metadata={
        "user_id": "user-123",
        "feature": "summary",
    },
)
```

Do not store passwords, API keys, or sensitive personal information in metadata.

### `text`

Configures text output, including structured output format.

```python
response = client.responses.create(
    model="gpt-4o-mini",
    input="Return a JSON object with name and age.",
    text={
        "format": {
            "type": "json_object",
        },
    },
)
```

### `tools`

Provides tools that the model can use, such as web search or custom functions.

```python
response = client.responses.create(
    model="gpt-4o-mini",
    input="Search for today's weather in Kathmandu.",
    tools=[
        {"type": "web_search_preview"},
    ],
)
```

Tool availability depends on the SDK version and model.

### `tool_choice`

Controls whether the model may use a tool.

```python
response = client.responses.create(
    model="gpt-4o-mini",
    input="Calculate 12 multiplied by 8.",
    tools=[
        {
            "type": "function",
            "name": "multiply",
            "description": "Multiply two numbers.",
            "parameters": {
                "type": "object",
                "properties": {
                    "a": {"type": "number"},
                    "b": {"type": "number"},
                },
                "required": ["a", "b"],
            },
        },
    ],
    tool_choice="auto",
)
```

Tool choice options commonly include `auto`, `required`, or an explicit tool selection,
depending on the API interface.

### `parallel_tool_calls`

Allows the model to request multiple tool calls in the same turn.

```python
response = client.responses.create(
    model="gpt-4o-mini",
    input="Check the status of orders 101 and 102.",
    parallel_tool_calls=True,
)
```

### `top_logprobs`

Requests the top candidate tokens and their log probabilities.

```python
response = client.responses.create(
    model="gpt-4o-mini",
    input="Complete: The sky is",
    top_logprobs=3,
)
```

This is primarily useful for analysis and model debugging.

### `truncation`

Controls automatic truncation behavior.

```python
response = client.responses.create(
    model="gpt-4o-mini",
    input="Explain distributed databases.",
    truncation="disabled",
)
```

Use `auto` or `disabled` only when you understand the model context limits.

## 4. Complete Example

```python
from dotenv import load_dotenv
from openai import OpenAI
import os

load_dotenv()

api_key = os.getenv("OPENAI_API_KEY")

if not api_key:
    raise RuntimeError("Set OPENAI_API_KEY in the .env file.")

client = OpenAI(
    api_key=api_key,
    timeout=30,
    max_retries=2,
)

response = client.responses.create(
    model="gpt-4o-mini",
    instructions="You are a Python tutor. Answer clearly and briefly.",
    input="What is a Python dictionary?",
    temperature=0.2,
    max_output_tokens=150,
)

print(response.output_text)
```

## 5. Recommended Parameter Combinations

### Factual Question

```python
temperature=0.2
top_p=1
max_output_tokens=200
```

### Creative Answer

```python
temperature=0.8
top_p=0.9
max_output_tokens=300
```

### Predictable JSON Output

```python
temperature=0
text={"format": {"type": "json_object"}}
```

## 6. Important Notes

- `api_key`, `base_url`, `timeout`, and `max_retries` are common client constructor settings.
- `temperature`, `top_p`, `max_output_tokens`, `stream`, and `tools` are usually response
  settings.
- `max_output_tokens` is the current Responses API parameter; do not confuse it with
  `max_tokens`.
- Supported parameters and values depend on the installed SDK and selected model.
- Never place an API key directly in source code or commit it to Git.

# Code taken from https://github.com/SakanaAI/AI-Scientist/blob/main/ai_scientist/llm.py.

import json
import os
import re

import anthropic
import backoff
import openai
import tiktoken

# Only set for non-reasoning models.
MAX_OUTPUT_TOKENS = 4096

AVAILABLE_LLMS = [
    # Anthropic Claude
    "claude-3-5-sonnet-20240620",
    "claude-3-5-sonnet-20241022",
    # OpenAI
    "gpt-4o-2024-05-13",
    "gpt-4o-2024-08-06",
    "gpt-4o-mini-2024-07-18",
    "o1-mini-2024-09-12",
    "o1-2024-12-17",
    "o3-mini-2025-01-31",
    # DeepSeek
    "deepseek-chat",
    "deepseek-coder",
    "deepseek-reasoner",
    # Llama Meta
    "llama3.1-8b",
    "llama3.1-70b",
    "llama3.1-405b",
    # Anthropic Claude models via Amazon Bedrock
    "bedrock/anthropic.claude-3-sonnet-20240229-v1:0",
    "bedrock/anthropic.claude-3-5-sonnet-20240620-v1:0",
    "bedrock/anthropic.claude-3-5-sonnet-20241022-v2:0",
    "bedrock/anthropic.claude-3-haiku-20240307-v1:0",
    "bedrock/anthropic.claude-3-opus-20240229-v1:0",
    # Anthropic Claude models via Vertex AI
    "vertex_ai/claude-3-opus@20240229",
    "vertex_ai/claude-3-5-sonnet@20240620",
    "vertex_ai/claude-3-5-sonnet-v2@20241022",
    "vertex_ai/claude-3-sonnet@20240229",
    "vertex_ai/claude-3-haiku@20240307",
]


def create_client(model: str):
    """
    Create and return an LLM client based on the specified model.

    Args:
        model (str): The name of the model to use.

    Returns:
        Tuple[Any, str]: A tuple containing the client instance and the client model name.
    """
    if model in ["claude-3-5-sonnet-20240620", "claude-3-5-sonnet-20241022"]:
        client_model = model
        client = anthropic.Anthropic()
    elif model.startswith("bedrock") and "claude" in model:
        client_model = model.split("/")[-1]
        client = anthropic.AnthropicBedrock(
            aws_access_key=os.getenv("AWS_ACCESS_KEY_ID"),
            aws_secret_key=os.getenv("AWS_SECRET_ACCESS_KEY"),
            aws_region=os.getenv("AWS_REGION_NAME"),
        )
    elif model.startswith("vertex_ai") and "claude" in model:
        client_model = model.split("/")[-1]
        client = anthropic.AnthropicVertex()
    elif (
        model.startswith("gpt-4o-")
        or model.startswith("o1-")
        or model.startswith("o3-")
    ):
        client_model = model
        client = openai.OpenAI()
    elif model in ["deepseek-chat", "deepseek-coder", "deepseek-reasoner"]:
        client_model = model
        client = openai.OpenAI(
            api_key=os.environ["DEEPSEEK_API_KEY"], base_url="https://api.deepseek.com"
        )
    elif model.startswith("llama3.1-"):
        llama_size = model.split("-")[-1]
        client_model = f"meta-llama/llama-3.1-{llama_size}-instruct"
        client = openai.OpenAI(
            api_key=os.environ["OPENROUTER_API_KEY"],
            base_url="https://openrouter.ai/api/v1",
        )
    else:
        raise ValueError(f"Model {model} not supported.")

    print(f"Using {client.__class__.__name__} API with model {client_model}.")
    return client, client_model


# Get N responses from a single message, used for ensembling.
@backoff.on_exception(
    backoff.expo,
    (
        openai.RateLimitError,
        openai.APITimeoutError,
        anthropic.RateLimitError,
        anthropic.APIStatusError,
    ),
)
def get_batch_responses_from_llm(
    msg,
    client,
    model,
    system_message,
    print_debug=False,
    msg_history=None,
    temperature=0.7,
    n_responses=1,
):
    if msg_history is None:
        msg_history = []

    if model.startswith("gpt-4o-"):
        new_msg_history = msg_history + [{"role": "user", "content": msg}]
        response = client.chat.completions.create(
            model=model,
            messages=[
                {"role": "system", "content": system_message},
                *new_msg_history,
            ],
            temperature=temperature,
            max_tokens=MAX_OUTPUT_TOKENS,
            n=n_responses,
            stop=None,
            seed=0,
        )
        content = [r.message.content for r in response.choices]
        new_msg_history = [
            new_msg_history + [{"role": "assistant", "content": c}] for c in content
        ]
    else:
        content, new_msg_history = [], []
        for _ in range(n_responses):
            c, hist = get_response_from_llm(
                msg,
                client,
                model,
                system_message,
                print_debug=False,
                msg_history=None,
                temperature=temperature,
            )
            content.append(c)
            new_msg_history.append(hist)

    if print_debug:
        print()
        print("*" * 20 + " LLM START " + "*" * 20)
        print(f'User: {new_msg_history[0][-2]["content"]}')
        print(f'Assistant: {new_msg_history[0][-1]["content"]}')
        print("*" * 21 + " LLM END " + "*" * 21)
        print()

    return content, new_msg_history


@backoff.on_exception(
    backoff.expo,
    (
        openai.RateLimitError,
        openai.APITimeoutError,
        anthropic.RateLimitError,
        anthropic.APIStatusError,
    ),
)
def get_response_from_llm(
    msg,
    client,
    model,
    system_message,
    print_debug=False,
    msg_history=None,
    temperature=0.7,
):
    if msg_history is None:
        msg_history = []

    if "claude" in model:
        new_msg_history = msg_history + [
            {
                "role": "user",
                "content": [
                    {
                        "type": "text",
                        "text": msg,
                    }
                ],
            }
        ]
        response = client.messages.create(
            model=model,
            max_tokens=MAX_OUTPUT_TOKENS,
            temperature=temperature,
            system=system_message,
            messages=new_msg_history,
        )
        content = response.content[0].text
        new_msg_history = new_msg_history + [
            {
                "role": "assistant",
                "content": [
                    {
                        "type": "text",
                        "text": content,
                    }
                ],
            }
        ]
    elif model.startswith("gpt-4o-"):
        new_msg_history = msg_history + [{"role": "user", "content": msg}]
        response = client.chat.completions.create(
            model=model,
            messages=[
                {"role": "system", "content": system_message},
                *new_msg_history,
            ],
            temperature=temperature,
            max_tokens=MAX_OUTPUT_TOKENS,
            n=1,
            stop=None,
            seed=0,
        )
        content = response.choices[0].message.content
        new_msg_history = new_msg_history + [{"role": "assistant", "content": content}]
    elif model.startswith("o1-") or model.startswith("o3-"):
        new_msg_history = msg_history + [{"role": "user", "content": msg}]
        response = client.chat.completions.create(
            model=model,
            messages=[
                {"role": "user", "content": system_message},
                *new_msg_history,
            ],
            response_format={"type": "text"},
            reasoning_effort="high",
        )
        content = response.choices[0].message.content
        new_msg_history = new_msg_history + [{"role": "assistant", "content": content}]
    elif model in ["deepseek-chat", "deepseek-coder"]:
        new_msg_history = msg_history + [{"role": "user", "content": msg}]
        response = client.chat.completions.create(
            model=model,
            messages=[
                {"role": "system", "content": system_message},
                *new_msg_history,
            ],
            temperature=temperature,
            max_tokens=MAX_OUTPUT_TOKENS,
            n=1,
            stop=None,
        )
        content = response.choices[0].message.content
        new_msg_history = new_msg_history + [{"role": "assistant", "content": content}]
    elif model in ["deepseek-reasoner"]:
        new_msg_history = msg_history + [{"role": "user", "content": msg}]
        response = client.chat.completions.create(
            model=model,
            messages=[
                {"role": "system", "content": system_message},
                *new_msg_history,
            ],
            n=1,
            stop=None,
        )
        content = response.choices[0].message.content
        new_msg_history = new_msg_history + [{"role": "assistant", "content": content}]
    elif model.startswith("meta-llama/llama-3.1-"):
        new_msg_history = msg_history + [{"role": "user", "content": msg}]
        response = client.chat.completions.create(
            model=model,
            messages=[
                {"role": "system", "content": system_message},
                *new_msg_history,
            ],
            temperature=temperature,
            max_tokens=MAX_OUTPUT_TOKENS,
            n=1,
            stop=None,
        )
        content = response.choices[0].message.content
        new_msg_history = new_msg_history + [{"role": "assistant", "content": content}]
    else:
        raise ValueError(f"Model {model} not supported.")

    if print_debug:
        print()
        print("*" * 20 + " LLM START " + "*" * 20)
        print(f'User: {new_msg_history[-2]["content"]}')
        print(f'Assistant: {new_msg_history[-1]["content"]}')
        print("*" * 21 + " LLM END " + "*" * 21)
        print()

    return content, new_msg_history


def extract_json_between_markers(llm_output):
    # Regular expression pattern to find JSON content between ```json and ```
    json_pattern = r"```json(.*?)```"
    matches = re.findall(json_pattern, llm_output, re.DOTALL)

    if not matches:
        # Fallback: Try to find any JSON-like content in the output
        json_pattern = r"\{.*?\}"
        matches = re.findall(json_pattern, llm_output, re.DOTALL)

    for json_string in matches:
        json_string = json_string.strip()
        try:
            parsed_json = json.loads(json_string)
            return parsed_json
        except json.JSONDecodeError:
            # Attempt to fix common JSON issues
            try:
                # Remove invalid control characters
                json_string_clean = re.sub(r"[\x00-\x1F\x7F]", "", json_string)
                parsed_json = json.loads(json_string_clean)
                return parsed_json
            except json.JSONDecodeError:
                continue  # Try next match

    return None  # No valid JSON found


# Embedding function
@backoff.on_exception(backoff.expo, openai.RateLimitError)
def get_embedding(client, text, model="text-embedding-3-small"):
    text = text.replace("\n", " ")

    try:
        # Try getting embedding with full text first
        response = client.embeddings.create(input=[text], model=model)
        return response.data[0].embedding

    except Exception as e:
        if "maximum context length" not in str(e).lower():
            raise e

        # If we hit context length error, truncate and retry
        try:
            encoding = tiktoken.encoding_for_model(model)
        except KeyError:
            encoding = tiktoken.get_encoding("cl100k_base")

        tokens = encoding.encode(text)
        token_limit = 8191  # Maximum tokens for embedding models

        print(
            f"Input text is too long ({len(tokens)} tokens) for model {model}, truncating to first {token_limit} tokens."
        )
        tokens = tokens[:token_limit]
        truncated_text = encoding.decode(tokens)

        response = client.embeddings.create(input=[truncated_text], model=model)
        return response.data[0].embedding

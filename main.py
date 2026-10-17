import os
import argparse
from config import system_prompt
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()
api_key = os.environ.get("OPENROUTER_API_KEY")
if api_key is None:
    raise RuntimeError("No API key found.")

client = OpenAI(
    base_url="https://openrouter.ai/api/v1",
    api_key=api_key,
)

# Get user prompt, maybe
parser = argparse.ArgumentParser(description="Chatbot")
parser.add_argument("user_prompt", type=str, help="User prompt")
parser.add_argument("--verbose", action="store_true", help="Enable verbose output")
args = parser.parse_args()

messages=[
        {"role": "system", "content": system_prompt},
        {"role": "user","content": args.user_prompt},
]

response = client.chat.completions.create(
    model="openrouter/free",
    messages=messages,
    temperature=0
)

if response.usage.prompt_tokens is None or response.usage.completion_tokens is None:
    raise RuntimeError("Possibly incomplete response.")
else:
    prompt_tokens = response.usage.prompt_tokens
    completion_tokens = response.usage.completion_tokens


def main():
    if args.verbose==True:
        print(f"User prompt: {args.user_prompt}")
        print(f"Model: {response.model}")
        print(f"Prompt tokens: {prompt_tokens}")
        print(f"Response tokens: {completion_tokens}")
    print(response.choices[0].message.content)


if __name__ == "__main__":
    main()

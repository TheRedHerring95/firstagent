import os
import argparse
import json
from functions.get_files_info import *
from call_function import call_function
from config import system_prompt
from call_function import available_functions
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()
api_key = os.environ.get("OPENROUTER_API_KEY")
if api_key is None:
    raise RuntimeError("No API key found.")

client = OpenAI(
    base_url="http://127.0.0.1:11434/v1",
    api_key="LocallyHosted",
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

def call_AI(messages, num: int):
    if num == 19:
        response = client.chat.completions.create(
            model="gemma4:12b",
            messages=messages,
            tools=available_functions,
            temperature=0,
            tool_choice="none"
        )
    else:
        response = client.chat.completions.create(
            model="gemma4:12b",
            messages=messages,
            tools=available_functions,
            temperature=0
        )
    if response.usage.prompt_tokens is None or response.usage.completion_tokens is None:
        raise RuntimeError("Possibly incomplete response.")
    else:
        prompt_tokens = response.usage.prompt_tokens
        completion_tokens = response.usage.completion_tokens
    return response

def main():
    for i in range(0,20):
        print(i)
        response = call_AI(messages, i)
        message = response.choices[0].message
        prompt_tokens = response.usage.prompt_tokens
        completion_tokens = response.usage.completion_tokens
        messages.append(message)
        if message.tool_calls != None:
            for tool_call in message.tool_calls:
                function_args = json.loads(tool_call.function.arguments or "{}")
                result = call_function(tool_call, args.verbose)
                messages.append(result)
                if result["content"] == None or "":
                    raise Exception("Error: No tool content")
                if args.verbose == True:
                    print(f'-> {result["content"]}')
                print(f"Calling function: {tool_call.function.name}({function_args})")
        else:
            #messages.append(message)
            if args.verbose==True:
                print(f"User prompt: {args.user_prompt}")
                print(f"Model: {response.model}")
                print(f"Prompt tokens: {prompt_tokens}")
                print(f"Response tokens: {completion_tokens}")
            print(message.content)
            break
        if i == 19:
            print(f"Out of calls")
            return 1
    return 0


if __name__ == "__main__":
    main()

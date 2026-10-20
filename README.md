# First Agent
First Agent is the first agent I call on when I need help with a code problem.

Custom built based on the results of building the agent in Boot.dev, this agent is being customised to work exactly the way I want it to, with the focus being on assisting me learn rather than getting code out as fast as possible. 

## Functions:
- Finding files within a directory
- Reading files within a directory
- Running Python code
- Not being able to write (write_file has been commented out of call function, and exists only so I can reimplement if I need to quickly)
- Running on my local hardware using Ollama endpoint.

## Not included:
As I run different configuragtions for this, is local.py. That has a single variable called MODEL, which is where the selected backend model is selected; Gemma4:12b on my main system, Qwen3.5:4b on my laptop.

# DISCLAIMER:
## This is still being regularly updated, and is primarily intended solely for my own usage. As a basic agent, it does not have all the security and safety considerations found in common agents. Do not expect the most polished behaviour out of this project, as it is for my own personal education (both the building itself and its usage) and not for production!
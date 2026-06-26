# Imports
from pydantic import BaseModel, create_model
import requests
import numpy as np
from langchain_ollama import ChatOllama
import json

# Set model
model = 'gemma4:e4b'

# Set structures output for returning a prompt
class PromptOutput(BaseModel):
    prompt: str


llm=ChatOllama(model=model,
               reasoning=False,
               temperature=0.0,
               num_predict=4096)

llm.with_structured_output(PromptOutput)

def initial_prompt(topic):
    return f"""I would like you to create a prompt that can be used in downstream LLM calls to obtain information useful in a summary around the given topic.
Topic = {topic}
Just the prompt no other text.
For the paper text put the word 'paper' in curly braces so it can be used as an f-string. Put this as the end and mark as 'Paper: {{paper}}'
"""

def summarise(topic):
    resp = llm.invoke(initial_prompt(topic))
    prompt = resp.content
    return prompt
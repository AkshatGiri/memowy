from dotenv import load_dotenv
from litellm import completion, encode, decode, token_counter, get_max_tokens, model_cost
import litellm
import os
from pathlib import Path
import requests
load_dotenv()

def get_env(k: str):
  if k in os.environ:
    return os.environ[k]
  else:
    raise Exception(f"Environment variable {k} not found")
  
litellm.openrouter_key = get_env("OPENROUTER_API_KEY")

###############
# Updating all openrouter models in litellm to make sure all the information is up do date.
###############

def fetch_openrouter_models():
  url = "https://openrouter.ai/api/v1/models"
  response = requests.get(url)
  return response.json()

def openrouter_model_to_litellm(model):
  return { 
    "max_tokens": model['context_length'],
    "input_cost_per_token": float(model['pricing']['prompt']),
    "output_cost_per_token": float(model['pricing']['completion']),
    "litellm_provider": "openrouter",
    "mode": "chat"
  }  

models = fetch_openrouter_models()['data']

for model in models:
  model_cost[f'openrouter/{model['id']}'] = openrouter_model_to_litellm(model)


###################
# Reading local files so they can be used in prompts so we can use up all the tokens in the context window.
###################

# Get the directory of the current script
script_dir = Path(__file__).parent.resolve()

opnet_wp_path = script_dir / 'opnet_wp.txt'

# read txt file 
with opnet_wp_path.open('r') as file: 
  openet_wp = file.read()
  
bee_movie_path = script_dir / 'bee_movie.txt'
with bee_movie_path.open("r") as file:
  bee_movie = file.read()
  
theo_von_path = script_dir / 'tony_robins_theo_von.txt'
with theo_von_path.open("r") as file:
  theo_von = file.read()


################
# Creating messages 
################
messages = [
  # { "content": f"Hey here is the opnet whitepaper. What are your thoughts \n\n{openet_wp}", "role": "user"},
  # { "content": f"Here's the transcript to the bee movie, what do you think? \n\n{bee_movie}", "role": "user"},
  { "content": f"Here's the transcript to a theo von and tony robbins podcast. In the transcript there is Speaker A and B. Can you tell me which one is Theo and which one is Tony. Also provide the reason behind your guess. \n\n{theo_von}", "role": "user"},
  # { "content": f"Hey how's it going?", "role": "user"},  
]

tokens = token_counter(model="mistral", messages=messages)
print(f"Number of tokens: {tokens}")

###########
# Getting model info 
###########

model = "openrouter/mistralai/mistral-7b-instruct"

context_size = get_max_tokens(model) # max token count

print(f"Context Size for model {model} : {context_size}")

if(tokens > context_size):
  print(f"Input exceeds model context size. Input: {tokens} | Context Size: {context_size}")
  exit()

###################
# Generate response.
###################

# NOTE: If we pass in messages that exceed the context size of the model
# the completion throws an error ( a very generic one ), so we'll just have
# to catch handle that appropriately.
response = completion(
  model=model,
  messages=messages,
  stream=False
)

print(response.choices[0].message.content)

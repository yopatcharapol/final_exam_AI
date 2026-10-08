import requests
import json
import os

from dotenv import load_dotenv
load_dotenv()
KEY = os.getenv("OPENROUTER_API_KEY")

# First API call with reasoning
# response = requests.post(
#   url="https://openrouter.ai/api/v1/chat/completions",
#   headers={
#     "Authorization": f"Bearer {KEY}",
#     "Content-Type": "application/json",
#   },
#   data=json.dumps({
#     "model": "openrouter/free",
#     "messages": [
#         {
#           "role": "user",
#           "content": "How many r's are in the word 'strawberry'?"
#         }
#       ],
#     "reasoning": {"enabled": True}
#   })
# )

# # Extract the assistant message with reasoning_details
# response = response.json()
# response = response['choices'][0]['message']

# print(response['reasoning'])
# print(response['reasoning_details'][0]['text'])


messages = {"role": "user", "content": "สวัสดี บอกชื่อตัวเองหน่อย"}

# Second API call - model continues reasoning from where it left off
response = requests.post(
  url="https://openrouter.ai/api/v1/chat/completions",
  headers={
    "Authorization": f"Bearer {KEY}",
    "Content-Type": "application/json",
  },
  data=json.dumps({
    "model": "openrouter/free",
    "messages": [
        messages
      ],
    "reasoning": {"enabled": True}
  })
)

# Extract the assistant message with reasoning_details
response = response.json()
response = response['choices'][0]['message']
print('******************************')
print('Thinking...')
print('******************************')
print(response['reasoning'])
print('******************************')
print('Answer')
print('******************************')
print(response['reasoning_details'][0]['text'])
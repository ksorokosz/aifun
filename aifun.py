#!/usr/bin/env python3
#
# Some AI examples
#
# Documentation: https://github.com/openai/openai-python

from openai import OpenAI
client = OpenAI()

response = client.chat.completions.create(
  model="gpt-3.5-turbo-0125",
  response_format={ "type": "json_object" },
  messages=[
    {"role": "system", "content": "You are a helpful assistant designed to output JSON."},
    {"role": "user", "content": "Give me an example of GetAccounts response with a single account. Response must be compatible with polish api standard version 2.1.1"}
  ]
)
print(response.choices[0].message.content)

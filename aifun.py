#!/usr/bin/env python3.8
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
    {"role": "user", "content": "Zwróć przykład odpowiedzi na usługę getAccounts zgodnej ze schemą opublikowaną na https://app.swaggerhub.com/apis/ZBP/polish-api/2_1_1"}
  ]
)
print(response.choices[0].message.content)

from openai import OpenAI
import os
from dotenv import load_dotenv

load_dotenv()

client = OpenAI(
  api_key=os.getenv('OPENAI_API_KEY'),
)

# response = client.completions.create(
#     model="text-davinci-003",
#     prompt="Translate the following English text to Japanese: 'Hello, how are you?'",
#     max_tokens=1000
# )

response = client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[
        {"role": "system", "content": "Your aer a helpful assistant."},
        {"role": "user", "content": "Hello! I'm Tom"}
    ]
)

print(response)

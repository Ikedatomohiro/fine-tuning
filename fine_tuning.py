import openai
from dotenv import load_dotenv
import os

load_dotenv()

api_key = os.getenv('OPENAI_API_KEY')
if api_key is None:
    raise ValueError("The OPENAI_API_KEY environment variable is not set.")

openai.api_key = api_key

try:
    if not os.path.isfile("test_data.jsonl"):
        raise FileNotFoundError("The training file test_data.jsonl was not found.")

    openai.FineTuningJob.create(training_file="test_data.jsonl", model="gpt-3.5-turbo")
    print("Fine-tuning job created successfully.")
except Exception as e:
    print(f"An error occurred while creating the fine-tuning job: {e}")
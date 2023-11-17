import openai
from dotenv import load_dotenv
import os

load_dotenv()

openai.api_key = os.getenv('OPENAI_API_KEY')
openai.FineTuningJob.create(training_file="test_data.jsonl", model="gpt-3.5-turbo")

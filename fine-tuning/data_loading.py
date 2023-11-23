import json
from collections import defaultdict

data_path = "test_data.jsonl"

# Load the dataset
try:
    with open(data_path, 'r', encoding='utf-8') as f:
        dataset = [json.loads(line) for line in f]
except (FileNotFoundError, PermissionError) as e:
    print(f"Error opening file: {e}")
except json.JSONDecodeError as e:
    print(f"Error parsing JSON: {e}")

# Initial dataset stats
print("Num examples:", len(dataset))
print("First example:")
for message in dataset[0]["messages"]:
    print(message)
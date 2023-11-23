from openai import OpenAI
import os
from dotenv import load_dotenv
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np

load_dotenv()

client = OpenAI(
    api_key=os.getenv('OPENAI_API_KEY')
)

embeddings = []
lines = []
with open('test_data.txt', 'r') as file:
    for line in file:
        text = line.strip()
        lines.append(text)
        response = client.embeddings.create(
            input=text,
            model="text-embedding-ada-002"
        )
        embeddings.append(response.data[0].embedding)

# 質問の埋め込みを取得
question = "2022年に発生した世界各地での自然災害の例を教えてください。"
question_res = client.embeddings.create(
    input=question,
    model="text-embedding-ada-002"
)
question_embedding = question_res.data[0].embedding

# 最も近いテキストを特定
cosine_similarities = cosine_similarity([question_embedding], embeddings)
closest_idx = np.argmax(cosine_similarities)

print("一番近い行：", closest_idx)

# ChatGPTに質問
closest_text = lines[closest_idx]
response = client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[
        {"role": "system", "content": "以下の情報に基づいて質問に答えてください: " + closest_text},
        {"role": "user", "content": question}
    ]
)
print(response)

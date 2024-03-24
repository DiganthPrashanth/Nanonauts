import os

from groq import Groq

client = Groq(
    api_key=os.environ.get("GROQ_API_KEY"),
)

Groq.api_key = "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"

chat_completion = client.chat.completions.create(
    messages=[
        {
            "role": "user",
            "content": "Explain the importance of low latency LLMs",
        }
    ],
    model="mixtral-8x7b-32768",
)

print(chat_completion.choices[0].message.content)
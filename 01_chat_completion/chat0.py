from openai import OpenAI

client = OpenAI()

chat_completion = client.chat.completions.create(
    messages=[
        {"role": "user", "content": "Hello, World!"}
    ],
    model="gpt-4"
)

response_text = chat_completion.choices[0].message.content

print(f"Assistant: {response_text}")
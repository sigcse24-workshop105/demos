from openai import OpenAI

client = OpenAI()

system_prompt = """
You are a friendly and supportive teaching assistant for CS50.
You are also a cat.
""".replace("\n", " ").strip()

user_prompt = input("User: ")

chat_completion = client.chat.completions.create(
    messages=[
        {"role": "system", "content": f"{system_prompt}"},
        {"role": "user", "content": f"{user_prompt}"}
    ],
    model="gpt-4",
)

response_text = chat_completion.choices[0].message.content

print(f"Assistant: {response_text}")

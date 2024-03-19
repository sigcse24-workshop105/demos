from openai import OpenAI

client = OpenAI()

system_prompt = """
You are a friendly and supportive teaching assistant for CS50.
You are also a cat.
""".replace("\n", " ").strip()

messages = []
messages.append({"role": "system", "content": f"{system_prompt}"})

while True:

    user_prompt = input("User: ")
    messages.append({"role": "user", "content": f"{user_prompt}"})

    chat_completion = client.chat.completions.create(
        messages=messages,
        model="gpt-4",
    )

    response_text = chat_completion.choices[0].message.content
    print(f"Assistant: {response_text}".strip())

    messages.append({"role": "assistant", "content": f"{response_text}"})

import os
import time
from openai import OpenAI

client = OpenAI()

instructions = """
You are a knowledgeable and approachable assistant for attendees of SIGCSE 2024.
Your purpose is to provide information, guidance, and support related to the SIGCSE 2024 conference,
its sessions, workshops, and any related computer science education topics.
Engage with inquiries in a friendly manner,
offering insights and resources that enhance the attendees' conference experience.
While your primary focus is on SIGCSE 2024, you can also address broader questions related to computer science education and research.
Avoid discussions unrelated to SIGCSE 2024 or the broader field of computer science education.
""".replace("\n", " ").strip()

# Upload a file with an "assistants" purpose
# https://platform.openai.com/docs/assistants/tools/supported-files
file_path = "./data/"

# Create file for each file in the data directory
files = []
for file in os.listdir(file_path):
    file = client.files.create(file=open(file_path + file, "rb"), purpose="assistants")
    files.append(file)

# Create an assistant if it doesn't exist
current_assistant = f"sigcse24-workshop105-{os.getenv('GITHUB_USER')}"
all_assistants = {assistant.name: assistant.id for assistant in client.beta.assistants.list(limit=100).data}
if current_assistant not in all_assistants:
    assistant = client.beta.assistants.create(
        name=f"sigcse24-workshop105-{os.getenv('GITHUB_USER')}",
        instructions=instructions,
        tools=[{"type": "retrieval"}],
        file_ids=[file.id for file in files],
        model="gpt-4-turbo-preview",
    )
else:
    print(f"Assistant {current_assistant} already exists")
    assistant = client.beta.assistants.retrieve(all_assistants[current_assistant])

user_prompt = input("User: ")

thread = client.beta.threads.create(messages=[{"role": "user", "content": user_prompt}])

run = client.beta.threads.runs.create(
    thread_id=thread.id,
    assistant_id=assistant.id,
)

while True:
    _run = client.beta.threads.runs.retrieve(thread_id=run.thread_id, run_id=run.id)
    print(f"run status: {_run.status}")

    if _run.status == "completed":
        thread_messages = client.beta.threads.messages.list(run.thread_id)
        print(f"Assistant: {thread_messages.data[0].content[0].text.value}")
        break

    time.sleep(1)

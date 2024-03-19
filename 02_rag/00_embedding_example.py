# Import the OpenAI module to use OpenAI's API
from openai import OpenAI

# Initialize the OpenAI client
client = OpenAI()

# Create an embedding for the input text "SIGCSE 2024" using the specified model "text-embedding-3-small"
response = client.embeddings.create(
    input="SIGCSE 2024",
    model="text-embedding-3-small"
)

# Print the embedding for the input text from the response
# The response object contains a list of data elements, and we access the first element's embedding attribute
print(response.data[0].embedding)

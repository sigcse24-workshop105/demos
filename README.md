# Workshop 105

Welcome to Workshop 105: Teaching with AI (GPT). This workshop is designed to introduce you to the capabilities of OpenAI's APIs, including Chat Completion, Embedding, and Assistant APIs, with hands-on demonstrations and code examples.

## Requirements

- Python 3.x
- OpenAI Python Library (installation guide below)
- OpenAI API Key (we have set the API key for you in the workshop)
- Internet Connection

## Installation

Before we dive into the demos, please ensure your environment is set up with the necessary software and libraries (we have done this for you in Codespace):

```bash
# Install the OpenAI library
pip install -r requirements.txt
```

## Demo 1: Chat Completion API

This demo illustrates how to utilize the Chat Completion API to create an interactive chatbot.

### Key Features

- **System Message**: Sets the context for the AI (e.g., "You are a friendly and supportive teaching assistant for CS50. You are also a cat.")
- **User Interaction**: Accepts user input to simulate a conversation.
- **API Integration**: Utilizes the `chat.completions.create` method to generate responses based on the conversation history.
- **Streaming Responses**: Demonstrates how to handle long-running completions with streaming.

## Demo 2: Text Embeddings and Semantic Search

This demo showcases the use of OpenAI's text embeddings to perform semantic search, enabling the identification of the most relevant information chunk in response to a user query. This technique can significantly enhance the way educational content is queried and retrieved, making it a powerful tool for educators and students alike.

### Key Features of Demo 2

- **Text Embeddings**: Illustrates how to generate and utilize text embeddings using OpenAI's `embeddings.create` method.
- **Semantic Search**: Demonstrates how to compute similarity scores between embeddings to find the most relevant content.
- **Integration with Chat API**: Combines the result of semantic search with the Chat Completion API to generate contextually relevant responses.

### Usage Notes

- **Pre-computed Embeddings**: Before running this demo, ensure you have a `embeddings.jsonl` file containing pre-computed embeddings for various content chunks relevant to your subject matter.
- **Custom Model Selection**: You can experiment with different models for embeddings to suit your content and accuracy requirements.

## Demo 3: Assistant API with Custom Data and Context

This demo showcases how to create a custom assistant that can utilize specific data files to provide tailored responses. It is particularly useful for creating specialized assistants for events, courses, or research projects.

### Key Features

- **Custom Assistant Creation**: Guides you through creating an assistant tailored to the needs of SIGCSE 2024 attendees.
- **Data File Utilization**: Demonstrates how to upload and associate data files with your assistant to enrich its responses.
- **Dynamic Interaction**: Engages users in a conversational interface, utilizing the assistant to respond to queries based on the provided data and instructions.

### Usage Notes

- **Data Preparation**: Before running the demo, ensure your `./data/` directory contains relevant files you wish to use with your assistant.
- **Customization**: You can customize the assistant's name, behavior, and capabilities to fit various educational or research contexts.
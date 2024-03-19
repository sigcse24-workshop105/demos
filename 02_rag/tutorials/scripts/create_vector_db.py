# these three lines swap the stdlib sqlite3 lib with the pysqlite3 package
__import__('pysqlite3')
import sys
sys.modules['sqlite3'] = sys.modules.pop('pysqlite3')

import chromadb
import json
import os
from chromadb.config import Settings

# path to our caption text embeddings
embeddings_data = "../data/processed_data/lectures_2023_embeddings.jsonl"


# open JSONL file and store data in-memory
print("Loading embeddings to memory...")
text_documents = []  # our caption text data
embeddings = []  # embedding for each caption text
metadatas = []  # metadata for each caption text
with open(embeddings_data) as f:
    for json_doc in f.readlines():
        json_doc = json.loads(json_doc)
        embeddings.append(json_doc["embedding"])
        text_documents.append(json_doc["text"])
        metadatas.append(json_doc["metadata"])


# remove existing vector database
os.system("rm -rf ../vector_db")


# setup Chroma db client
# https://docs.trychroma.com/getting-started#2-get-the-chroma-client
print("Creating chroma db...")
client = chromadb.PersistentClient(path="../vector_db")


# https://docs.trychroma.com/getting-started#3-create-a-collection
print("Creating chroma db collection...")
collection = client.create_collection("cs50_lectures_2023")

# Add docs to the collection. Can also update and delete. Row-based API coming soon!
# https://docs.trychroma.com/getting-started#4-add-some-text-documents-to-the-collection
print("Adding documents to collection...")
collection.add(
    documents=text_documents,  # we handle tokenization, embedding, and indexing automatically. You can skip that and add your own embeddings as well
    embeddings=embeddings,
    metadatas=metadatas,
    ids=[f"{each}" for each in range(len(text_documents))],
)

del text_documents
del embeddings
del metadatas

print("Done!")

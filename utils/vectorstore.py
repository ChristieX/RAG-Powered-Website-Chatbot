from langchain_community.vectorstores import Chroma
from langchain_ollama import OllamaEmbeddings
from chunker import chunk_text

chunk = chunk_text("https://pypi.org/project/langchain/")
embeddings=OllamaEmbeddings(model="nomic-embed-text")
vectorstore = Chroma.from_documents(chunk, embeddings, persist_directory="db")



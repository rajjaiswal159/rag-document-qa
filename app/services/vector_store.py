from pathlib import Path

from langchain_google_genai import GoogleGenerativeAIEmbeddings
from langchain_community.vectorstores import FAISS

from app.config.settings import settings


class VectorStoreService:

    def __init__(self):
        # Initialize Gemini embedding model
        self.embeddings = GoogleGenerativeAIEmbeddings(
            model="gemini-embedding-001",
            google_api_key=settings.GOOGLE_API_KEY
        )

    def create_vector_store(self, chunks):
        # Create a FAISS vector store from document chunks
        return FAISS.from_documents(
            documents=chunks,
            embedding=self.embeddings
        )

    def save_vector_store(self, vector_store, path: str):
        # Save the vector store to disk
        try:
            vector_store.save_local(path)
        except Exception as e:
            raise RuntimeError(f"Failed to save vector store: {e}")

    def load_vector_store(self, path: str):
        # Load the vector store from disk
        try:
            return FAISS.load_local(
                folder_path=path,
                embeddings=self.embeddings,
                allow_dangerous_deserialization=True
            )
        except Exception as e:
            raise RuntimeError(f"Failed to load vector store: {e}")

    def vector_store_exists(self, path: str) -> bool:
        # Check whether the vector store exists
        return Path(path).exists()

    def add_documents(self, vector_store, chunks):
        # Add new document chunks to the existing vector store
        vector_store.add_documents(chunks)
        return vector_store
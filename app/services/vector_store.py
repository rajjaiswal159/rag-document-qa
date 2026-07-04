from langchain_google_genai import GoogleGenerativeAIEmbeddings
from langchain_community.vectorstores import FAISS
from pathlib import Path

from app.config.settings import settings

class VectorStoreService:

    def __init__(self):

        self.embeddings = GoogleGenerativeAIEmbeddings(
            model="gemini-embedding-001",
            google_api_key=settings.GOOGLE_API_KEY
        )

    def create_vector_store(self, chunks):

        vector_store = FAISS.from_documents(
            documents=chunks,
            embedding=self.embeddings
        )
    
        return vector_store
    
    def save_vector_store(self, vector_store, path: str):

        vector_store.save_local(path)

    def load_vector_store(self, path: str):

        return FAISS.load_local(
            folder_path=path,
            embeddings=self.embeddings,
            allow_dangerous_deserialization=True
        )
    
    def vector_store_exists(self, path: str) -> bool:
        return Path(path).exists()
    
    def add_documents(self, vector_store, chunks):

        vector_store.add_documents(chunks)
    
        return vector_store
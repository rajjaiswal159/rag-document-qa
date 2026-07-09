from langchain_google_genai import GoogleGenerativeAIEmbeddings
from langchain_community.vectorstores import FAISS
from app.utils.logger import logger
from app.config.settings import settings


class VectorStoreService:

    def __init__(self):
        # Initialize Gemini embedding model
        self.embeddings = GoogleGenerativeAIEmbeddings(
            model="gemini-embedding-001",
            google_api_key=settings.GOOGLE_API_KEY
        )

    def create_vector_store(self, chunks):
        try:
            return FAISS.from_documents(
                documents=chunks,
                embedding=self.embeddings
            )
    
        except Exception:
            logger.exception("Failed to create vector store.")
    
            raise RuntimeError("Failed to create vector store.")
        
    def save_vector_store(self, vector_store, path: str):
        # Save the vector store to disk
        try:
            vector_store.save_local(path)

            logger.info(
                "Vector store saved successfully at: %s",
                path
            )
            
        except Exception:
            logger.exception(
                "Failed to save vector store at: %s", 
                path
            )
    
            raise RuntimeError("Failed to save vector store.")

    def load_vector_store(self, path: str):
        try:
            return FAISS.load_local(
                folder_path=path,
                embeddings=self.embeddings,
                allow_dangerous_deserialization=True
            )
    
        except Exception:
            logger.exception(
                "Failed to load vector store from: %s",
                path
            )
    
            raise RuntimeError("Failed to load vector store.")
from app.services.vector_store import VectorStoreService
from app.config.settings import settings
from pathlib import Path

class Retriever:

    def __init__(self):
        # Initialize vector store service
        self.vector_store_path = settings.VECTOR_STORE_PATH
        self.vector_store_service = VectorStoreService()

    def retrieve(self, document_id: str, question: str, k: int = 4):

        vector_store_path = (
            Path(self.vector_store_path) / document_id
        )

        if not vector_store_path.exists():
            raise FileNotFoundError(
                f"Vector store for document '{document_id}' not found."
            )

        # Load the existing vector store
        vector_store = self.vector_store_service.load_vector_store(
            str(vector_store_path)
        )

        # Retrieve the most relevant documents
        documents = vector_store.similarity_search(
            query=question,
            k=k
        )

        return documents
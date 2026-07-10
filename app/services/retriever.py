from app.services.vector_store import VectorStoreService
from app.config.settings import settings
from pathlib import Path
from app.services.document_service import DocumentService

class Retriever:

    def __init__(self):
        # Initialize vector store service
        self.vector_store_path = settings.VECTOR_STORE_PATH
        self.vector_store_service = VectorStoreService()
        self.document_service = DocumentService()

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

        # Update last accessed time
        self.document_service.update_last_access(document_id)

        # Retrieve the most relevant documents
        documents = vector_store.similarity_search(
            query=question,
            k=k
        )

        return documents
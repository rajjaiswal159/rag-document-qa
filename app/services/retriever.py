from app.services.vector_store import VectorStoreService
from app.exceptions import VectorStoreNotFoundError


class Retriever:

    def __init__(self, vector_store_path: str):

        self.vector_store_path = vector_store_path
        self.vector_store_service = VectorStoreService()

    def retrieve(self, question: str, k: int = 4):

        if not self.vector_store_service.vector_store_exists(self.vector_store_path):
            raise VectorStoreNotFoundError(
                "No documents have been uploaded yet."
            )

        vector_store = self.vector_store_service.load_vector_store(
            self.vector_store_path
        )

        documents = vector_store.similarity_search(
            query=question,
            k=k
        )

        return documents
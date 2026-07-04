from pathlib import Path

from app.services.document_processor import DocumentProcessor
from app.services.vector_store import VectorStoreService

class IndexingService:

    def __init__(self):

        self.processor = DocumentProcessor()
        self.vector_store = VectorStoreService()

        self.vector_store_path = Path("data/vector_store")

    def index_document(self, pdf_path: str):

        documents = self.processor.load_document(pdf_path)
    
        chunks = self.processor.split_documents(documents)
    
        if self.vector_store.vector_store_exists(str(self.vector_store_path)):

            vector_db = self.vector_store.load_vector_store(
                str(self.vector_store_path)
            )        

            vector_db = self.vector_store.add_documents(
                vector_db,
                chunks
            )        

        else:        

            vector_db = self.vector_store.create_vector_store(
                chunks
            )        

        self.vector_store.save_vector_store(
            vector_db,
            str(self.vector_store_path)
        )
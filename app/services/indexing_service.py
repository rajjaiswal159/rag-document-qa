from pathlib import Path

from app.config.settings import settings
from app.services.document_processor import DocumentProcessor
from app.services.vector_store import VectorStoreService


class IndexingService:

    def __init__(self):
        # Initialize document processor and vector store service
        self.processor = DocumentProcessor()
        self.vector_store = VectorStoreService()

    def index_document(self, pdf_path: Path):

        # Extract UUID from filename
        document_id = pdf_path.stem

        # Create vector store path for this document
        vector_store_path = (
            Path(settings.VECTOR_STORE_PATH) / document_id
        )
        
        # Extract and split the uploaded PDF into chunks
        documents = self.processor.load_document(str(pdf_path))
        chunks = self.processor.split_documents(documents)

        # Create vector store
        vector_db = self.vector_store.create_vector_store(chunks)

        # Save the updated vector store
        self.vector_store.save_vector_store(
            vector_db,
            str(vector_store_path)
        )

        return document_id
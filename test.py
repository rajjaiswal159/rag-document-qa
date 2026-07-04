from app.services.document_processor import DocumentProcessor
from app.services.vector_store import VectorStoreService

processor = DocumentProcessor()
vector_service = VectorStoreService()

documents = processor.load_document("data/uploads/Summary Report.pdf")
chunks = processor.split_documents(documents)

vector_store = vector_service.create_vector_store(chunks)

vector_service.save_vector_store(
    vector_store,
    "data/vector_store"
)

print("Vector store created successfully!")
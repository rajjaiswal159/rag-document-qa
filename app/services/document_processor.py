from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter


class DocumentProcessor:

    def __init__(self):
        self.text_splitter = RecursiveCharacterTextSplitter(
            chunk_size=1000,
            chunk_overlap=200
        )

    def load_document(self, pdf_path: str):

        # Initialize the PDF loader
        loader = PyPDFLoader(pdf_path)

        # Load all pages as LangChain Document objects
        documents = loader.load()

        return documents
    
    def split_documents(self, documents):
        return self.text_splitter.split_documents(documents)
from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter


class DocumentProcessor:

    def __init__(self):
        # Initialize the text splitter
        self.text_splitter = RecursiveCharacterTextSplitter(
            chunk_size=1000,
            chunk_overlap=200
        )

    def load_document(self, pdf_path: str):
        # Initialize the PDF loader
        loader = PyPDFLoader(pdf_path)

        # Load all pages as LangChain Document objects
        return loader.load()

    def split_documents(self, documents):
        # Split documents into smaller overlapping chunks
        return self.text_splitter.split_documents(documents)
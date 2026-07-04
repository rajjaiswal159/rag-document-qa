from langchain_community.document_loaders import PyPDFLoader


class DocumentProcessor:

    def load_document(self, pdf_path: str):

        # Initialize the PDF loader
        loader = PyPDFLoader(pdf_path)

        # Load all pages as LangChain Document objects
        documents = loader.load()

        return documents
# 📄 Document Q&A API (RAG)

A production-style Retrieval-Augmented Generation (RAG) API built with **FastAPI**, **LangChain**, **FAISS**, and **Google Gemini**. The application allows users to upload PDF documents, indexes them into a vector database, and answers questions using only the uploaded document content while providing source citations.

---

## 🚀 Features

- Upload PDF documents
- Dedicated FAISS vector store for each uploaded document
- Automatic document chunking
- Google Gemini embeddings for semantic search
- Retrieval-Augmented Generation (RAG)
- Source citations with page numbers
- SQLAlchemy + SQLite for document metadata management
- Automatic cleanup of inactive documents and vector stores
- RESTful FastAPI endpoints
- File validation and configurable size limits
- Structured service-based architecture
- Logging and error handling

---

## 🛠️ Tech Stack

- Python
- FastAPI
- LangChain
- Google Gemini
- FAISS
- SQLAlchemy
- SQLite
- Pydantic Settings
- Uvicorn

---


## 📁 Project Structure

│app/
│
├── api/                 # FastAPI route handlers
│   ├── upload.py
│   └── question.py
│
├── config/             # Application configuration
│   └── settings.py
│
├── db/                  # SQLAlchemy database setup
│   ├── database.py
│   └── models.py
│
├── schemas/             # Request and response models
│   ├── question.py
│   └── response.py
│
├── services/            # Core business logic
│   ├── cleanup_service.py
│   ├── document_processor.py
│   ├── document_service.py
│   ├── file_service.py
│   ├── indexing_service.py
│   ├── qa_service.py
│   ├── retriever.py
│   └── vector_store.py
│
├── utils/
│   └── logger.py
│
└── main.py

---

## ⚙️ Installation

### Clone the repository

```bash
git clone https://github.com/rajjaiswal159/rag-document-qa.git
cd rag-document-qa
```

### Create a virtual environment

```bash
python -m venv .venv
```

Activate it:

Windows

```bash
.venv\Scripts\activate
```

Linux / macOS

```bash
source .venv/bin/activate
```

### Install dependencies

```bash
pip install -r requirements.txt
```

---

## 🔑 Environment Variables

Create a `.env` file in the project root.

```env
GOOGLE_API_KEY=your_google_api_key
```

---

## ▶️ Run the Application

```bash
uvicorn app.main:app --reload
```

The API will be available at:

```
http://127.0.0.1:8000
```

Swagger documentation:

```
http://127.0.0.1:8000/docs
```

---

## 📤 Upload a PDF

**POST**

```
/upload/
```

Example using cURL:

```bash
curl -X POST \
  "http://127.0.0.1:8000/upload/" \
  -F "file=@sample.pdf"
```

Example Response

```json
{
  "message": "File uploaded successfully.",
  "document_id": "f18c6b25-6c1d-4b6d-8b1e-3d9e7f4d2abc",
  "filename": "sample.pdf"
}
```

---

## ❓ Ask Questions

**POST**

```
/ask
```

Request

```json
{
  "document_id": "f18c6b25-6c1d-4b6d-8b1e-3d9e7f4d2abc",
  "question": "What is Retrieval-Augmented Generation?"
}
```

Example Response

```json
{
  "answer": "Retrieval-Augmented Generation (RAG) combines information retrieval with large language models to generate answers grounded in external documents.",
  "sources": [
    {
      "source": "sample.pdf",
      "page": 2
    }
  ]
}
```

---

## 🔄 How It Works

1. The user uploads a PDF document.
2. The uploaded PDF is validated and temporarily stored.
3. The document is loaded using `PyPDFLoader`.
4. The text is split into overlapping chunks.
5. Chunks are converted into Gemini embeddings.
6. A dedicated FAISS vector store is created for the uploaded document.
7. The vector store is saved using a unique document ID.
8. Document metadata (filename, upload time and last accessed time) is stored in SQLite using SQLAlchemy.
9. The API returns the generated document ID.
10. When a question is submitted:
    - The client sends the document ID and question.
    - Expired documents are automatically cleaned up.
    - The corresponding FAISS vector store is loaded.
    - Relevant chunks are retrieved using similarity search.
    - The document's last access time is updated.
    - Gemini generates an answer using only the retrieved context.
11. The API returns the answer along with source citations and page numbers.

---

## ✨ Key Highlights

- Production-style Retrieval-Augmented Generation (RAG) pipeline
- Dedicated FAISS vector store for every uploaded document
- SQLAlchemy + SQLite metadata management
- Automatic cleanup of inactive vector stores
- Configurable document expiration
- Google Gemini for embeddings and answer generation
- Source citations with page numbers
- Modular service-based architecture
- RESTful FastAPI API with structured logging and error handling

---

## 📄 License

This project is licensed under the MIT License.

# 📄 Document Q&A API (RAG)

A production-style Retrieval-Augmented Generation (RAG) API built with **FastAPI**, **LangChain**, **FAISS**, and **Google Gemini**. The application allows users to upload PDF documents, indexes them into a vector database, and answers questions using only the uploaded document content while providing source citations.

---

## 🚀 Features

* Upload PDF documents
* Automatic document chunking
* Gemini Embeddings for semantic search
* FAISS vector database
* Retrieval-Augmented Generation (RAG)
* Source citations with page numbers
* RESTful FastAPI endpoints
* File validation and size limits
* Structured project architecture
* Logging and error handling

---

## 🛠️ Tech Stack

* Python
* FastAPI
* LangChain
* Google Gemini
* FAISS
* Pydantic Settings
* Uvicorn

---

## 📁 Project Structure

```text
app/
│
├── api/                 # FastAPI route handlers
│   ├── upload.py
│   └── question.py
│
├── config/              # Application configuration
│   └── settings.py
│
├── schemas/             # Request and response models
│   ├── question.py
│   ├── response.py
│
├── services/            # Core business logic
│   ├── document_processor.py
│   ├── file_service.py
│   ├── indexing_service.py
│   ├── qa_service.py
│   ├── retriever.py
│   └── vector_store.py
│
├── utils/               # Utility modules
│   └── logger.py
│
└── main.py              # FastAPI application entry point
```

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

1. User uploads a PDF.
2. The PDF is loaded using `PyPDFLoader`.
3. Documents are split into overlapping chunks.
4. Chunks are converted into embeddings using Gemini.
5. Embeddings are stored in a FAISS vector database.
6. When a question is asked:

   * Relevant chunks are retrieved using similarity search.
   * Retrieved chunks are passed to Gemini as context.
   * Gemini generates an answer using only the provided context.
7. The API returns the answer along with the source documents and page numbers.

---

## ✨ Key Highlights

- Modular service-based architecture
- Retrieval-Augmented Generation (RAG) pipeline
- FAISS vector database for semantic search
- Google Gemini for embeddings and answer generation
- Source citations with page numbers
- RESTful API built with FastAPI

---

## 📄 License

This project is licensed under the MIT License.

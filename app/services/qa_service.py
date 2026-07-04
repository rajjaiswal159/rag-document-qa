from langchain_google_genai import ChatGoogleGenerativeAI

from app.config.settings import settings
from app.services.retriever import Retriever


class QAService:

    def __init__(self, vector_store_path: str):

        self.retriever = Retriever(vector_store_path)

        self.llm = ChatGoogleGenerativeAI(
            model="gemini-2.5-flash",
            google_api_key=settings.GOOGLE_API_KEY,
            temperature=0
        )

    def answer_question(self, question: str):

        documents = self.retriever.retrieve(question)
        context = "\n\n".join(document.page_content for document in documents)

        prompt = f"""
You are an AI assistant for answering questions from uploaded documents.

Instructions:
- Answer ONLY using the provided context.
- If the answer is not present in the context, say:
  "I couldn't find the answer in the uploaded documents."
- Do not make up information.
- Keep your answer clear and concise.

Context:
{context}

Question:
{question}

Answer:
"""
        
        response = self.llm.invoke(prompt)

        sources = []
        seen = set()
        
        for document in documents:
        
            source = (
                document.metadata.get("source"),
                document.metadata.get("page")
            )
        
            if source not in seen:
                seen.add(source)
        
                sources.append({
                    "source": source[0],
                    "page": source[1]
                })
        
        return {
            "answer": response.content,
            "sources": sources
        }
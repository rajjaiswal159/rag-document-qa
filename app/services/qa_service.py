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
            You are an AI assistant for question answering.
            
            Use ONLY the information provided in the context below.
            
            If the answer is not present in the context, reply:
            
            "I couldn't find the answer in the uploaded documents."
            
            Context:
            {context}
            
            Question:
            {question}
            
            Answer:
            """
        
        response = self.llm.invoke(prompt)

        return {
            "answer": response.content,
            "documents": documents
        }
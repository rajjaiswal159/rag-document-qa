from sqlalchemy.orm import Session
from app.db.models import Document
from app.db.database import SessionLocal
from datetime import datetime
from app.utils.logger import logger


class DocumentService:

    def __init__(self):
        pass

    def get_db(self) -> Session:
        return SessionLocal()
    
    def add_document(
        self,
        document_id: str,
        filename: str
    ):
        db = self.get_db()
    
        try:
            document = Document(
                document_id=document_id,
                filename=filename
            )
    
            db.add(document)
            db.commit()

        except Exception:
            db.rollback()
    
            logger.exception(
                "Failed to save document metadata: %s",
                document_id
            )
    
            raise RuntimeError(
                "Failed to save document metadata."
            )
    
        finally:
            db.close()

    def update_last_access(
        self,
        document_id: str
    ):
        db = self.get_db()
    
        try:
            document = db.get(
                Document,
                document_id
            )
    
            if document:
    
                document.last_accessed = datetime.utcnow()
    
                db.commit()


        except Exception:
            db.rollback()
        
            logger.exception(
                "Failed to update last access time: %s",
                document_id
            )
        
            raise RuntimeError(
                "Failed to update document metadata."
            )
    
        finally:
            db.close()

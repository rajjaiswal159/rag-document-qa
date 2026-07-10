from datetime import datetime, timedelta
from pathlib import Path
import shutil
from sqlalchemy import select
from app.config.settings import settings
from app.db.database import SessionLocal
from app.db.models import Document
from app.utils.logger import logger


class CleanupService:

    def __init__(self):

        self.vector_store_path = Path(settings.VECTOR_STORE_PATH)

        self.expiration_minutes = (settings.DOCUMENT_EXPIRATION_MINUTES)

    def cleanup_expired(self):

        db = SessionLocal()
    
        try:
    
            cutoff = (
                datetime.utcnow()
                - timedelta(minutes=self.expiration_minutes)
            )
    
            expired_documents = db.scalars(
                select(Document).where(
                    Document.last_accessed < cutoff
                )
            ).all()
    
            for document in expired_documents:
    
                vector_store = (
                    self.vector_store_path
                    / document.document_id
                )
    
                if vector_store.exists():
    
                    shutil.rmtree(vector_store)
    
                    logger.info(
                        "Deleted vector store: %s",
                        document.document_id
                    )
    
                db.delete(document)
    
            db.commit()

        except Exception:
            logger.exception(
                "Failed to clean up document %s",
                document.document_id
            )
    
        finally:
    
            db.close()
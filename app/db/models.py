from datetime import datetime

from sqlalchemy import DateTime, String
from sqlalchemy.orm import Mapped, mapped_column

from app.db.database import Base


class Document(Base):
    __tablename__ = "documents"

    # Unique ID used for the vector store folder
    document_id: Mapped[str] = mapped_column(
        String,
        primary_key=True
    )

    # Original uploaded filename
    filename: Mapped[str] = mapped_column(
        String,
        nullable=False
    )

    # Upload timestamp
    uploaded_at: Mapped[datetime] = mapped_column(
        DateTime,
        default=datetime.utcnow
    )

    # Last time the document was queried
    last_accessed: Mapped[datetime] = mapped_column(
        DateTime,
        default=datetime.utcnow
    )
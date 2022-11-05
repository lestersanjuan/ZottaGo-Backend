import uuid
from app import db
from Base import Base
from sqlalchemy.dialects.postgresql import UUID


class Review(Base):
    __tablename__ = 'review'
    review_id = db.Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    rating = db.Column(db.Integer())
    description = db.Column(db.String())
    bathroom_id = db.Column(UUID(as_uuid=True))
    
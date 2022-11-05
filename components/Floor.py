import uuid
from app import db
from Base import Base
from sqlalchemy.dialects.postgresql import UUID

class Floor(Base):
    __tablename__ = 'Floor'
    floor_id = db.Column(db.Integer(),primary_key=true)
    bathroom_id = db.Column(UUID(as_uuid=True), default=uuid.uuid4)
    floor_number = db.Column(db.Integer())
    name_of_building = db.Column(db.String())

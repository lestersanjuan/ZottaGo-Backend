import uuid
from app import db
from ..base import Base
from sqlalchemy.dialects.postgresql import UUID

class Bathrooms(Base):
    __tablename__ = 'Bathroom'
    bathroom_id = db.Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    name_of_building = db.Column(db.String())
    flood_number = db.column(db.Integer())
    direction = db.column(db.String())
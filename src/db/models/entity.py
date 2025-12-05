from sqlalchemy import Column, BigInteger, String
from sqlalchemy.orm import relationship
from src.db.database import Base

class Entity(Base):
    __tablename__ = "core_entity"

    id = Column(BigInteger, primary_key=True, autoincrement=True)
    entity_name = Column(String(100), nullable=False)
    entity_description = Column(String(255))
    entity_type = Column(String(20), nullable=False)

    records = relationship(
        "Record",
        back_populates="entity",
        foreign_keys="Record.entity_id"
    )

    def __repr__(self):
        return f"<Entity id={self.id} name={self.entity_name}>"

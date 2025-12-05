from sqlalchemy import Column, BigInteger, String
from sqlalchemy.orm import relationship
from src.db.database import Base

class Currency(Base):
    __tablename__ = "core_currency"

    id = Column(BigInteger, primary_key=True, autoincrement=True)
    currency_name = Column(String(100), nullable=False)
    currency_code = Column(String(3), nullable=False)

    records = relationship(
        "Record",
        back_populates="currency",
        foreign_keys="Record.currency_id"
    )

    def __repr__(self):
        return f"<Currency id={self.id} code={self.currency_code}>"

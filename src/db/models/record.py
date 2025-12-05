from sqlalchemy import Column, BigInteger, String, Date, DateTime, ForeignKey, Numeric
from sqlalchemy.orm import relationship
from src.db.database import Base

class Record(Base):
    __tablename__ = "records_record"

    id = Column(BigInteger, primary_key=True, autoincrement=True)
    record_type = Column(String(20), nullable=False)
    record_amount = Column(Numeric(12, 2), nullable=False)
    record_description = Column(String(255))
    record_date = Column(Date, nullable=False)
    created_at = Column(DateTime)

    account_id = Column(BigInteger, ForeignKey("accounts_account.id"))
    currency_id = Column(BigInteger, ForeignKey("core_currency.id"))
    entity_id = Column(BigInteger, ForeignKey("core_entity.id"))

    transfer_id = Column(BigInteger, ForeignKey("accounts_account.id"))
    transfer_account_id = Column(BigInteger, ForeignKey("accounts_account.id"))

    subcategory_id = Column(BigInteger, ForeignKey("records_subcategory.id"))

    account = relationship(
    "Account",
    foreign_keys=[account_id],
    back_populates="records")

    transfer_account = relationship(
    "Account",
    foreign_keys=[transfer_account_id],
    back_populates=None)

    currency = relationship("Currency", back_populates="records")
    entity = relationship("Entity", back_populates="records")
    subcategory = relationship("Subcategory", back_populates="records")

    def __repr__(self):
        return f"<Record id={self.id} type={self.record_type} amount={self.record_amount}>"

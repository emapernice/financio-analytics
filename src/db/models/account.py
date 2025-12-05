from sqlalchemy import Column, BigInteger, String, Numeric, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from src.db.database import Base

class Account(Base):
    __tablename__ = "accounts_account"

    id = Column(BigInteger, primary_key=True, autoincrement=True)
    account_name = Column(String(100), nullable=False)
    account_type = Column(String(20), nullable=False)
    initial_balance = Column(Numeric(12, 2), nullable=False)
    created_at = Column(DateTime, nullable=False)

    currency_id = Column(BigInteger, ForeignKey("core_currency.id"), nullable=False)
    user_id = Column(BigInteger, ForeignKey("users_user.id"), nullable=False)

    records = relationship(
        "Record",
        back_populates="account",
        foreign_keys="Record.account_id",
    )

    def __repr__(self):
        return f"<Account id={self.id} name={self.account_name}>"

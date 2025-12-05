from sqlalchemy import Column, BigInteger, String, Boolean, ForeignKey
from sqlalchemy.orm import relationship
from src.db.database import Base

class Subcategory(Base):
    __tablename__ = "records_subcategory"

    id = Column(BigInteger, primary_key=True, autoincrement=True)
    subcategory_name = Column(String(100), nullable=False)
    is_fixed = Column(Boolean, nullable=False)

    category_id = Column(BigInteger, ForeignKey("records_category.id"), nullable=False)
    user_id = Column(BigInteger, ForeignKey("users_user.id"), nullable=True)

    category = relationship("Category", back_populates="subcategories")
    user = relationship("User", back_populates="subcategories")

    records = relationship(
        "Record",
        back_populates="subcategory",
        foreign_keys="Record.subcategory_id"
    )

    def __repr__(self):
        return (
            f"<Subcategory id={self.id} name={self.subcategory_name} fixed={self.is_fixed}>"
        )

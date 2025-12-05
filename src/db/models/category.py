from sqlalchemy import Column, BigInteger, String, ForeignKey
from sqlalchemy.orm import relationship
from src.db.database import Base

class Category(Base):
    __tablename__ = "records_category"

    id = Column(BigInteger, primary_key=True, autoincrement=True)
    category_name = Column(String(100), nullable=False)
    category_type = Column(String(20), nullable=False)
    user_id = Column(BigInteger, ForeignKey("users_user.id"), nullable=True)

    user = relationship("User", back_populates="categories")
    subcategories = relationship("Subcategory", back_populates="category")

    def __repr__(self):
        return (
            f"<Category id={self.id} name={self.category_name} type={self.category_type}>"
        )

from sqlalchemy import Column, BigInteger, String, Boolean, DateTime
from sqlalchemy.orm import relationship
from src.db.database import Base

class User(Base):
    __tablename__ = "users_user"

    id = Column(BigInteger, primary_key=True, autoincrement=True)
    password = Column(String(128), nullable=False)
    last_login = Column(DateTime, nullable=True)
    is_superuser = Column(Boolean, nullable=False)
    username = Column(String(150), nullable=False, unique=True)
    first_name = Column(String(150), nullable=False)
    last_name = Column(String(150), nullable=False)
    email = Column(String(254), nullable=False)
    is_staff = Column(Boolean, nullable=False)
    is_active = Column(Boolean, nullable=False)
    date_joined = Column(DateTime, nullable=False)

    categories = relationship(
        "Category",
        back_populates="user",
        foreign_keys="Category.user_id"
    )

    subcategories = relationship(
        "Subcategory",
        back_populates="user",
        foreign_keys="Subcategory.user_id"
    )

    def __repr__(self):
        return f"<User id={self.id} username={self.username}>"

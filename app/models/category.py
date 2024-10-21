from sqlalchemy import Column, String, Integer
from app.db.base import Base

class Category(Base):
    __tablename__ = "categories"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True, nullable=False)
    image_url = Column(String, nullable=True)  # New column for storing image URL
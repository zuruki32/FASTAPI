from .database import Base, engine, SessionLocal
from sqlalchemy import Column, Integer, String

class Blog(Base):
    __tablename__ = "blogs"
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)
    body = Column(String, index=True)
    
    
from sqlalchemy import Column, Integer, String, Text, TIMESTAMP, func
from database import Base

class Message(Base):
    __tablename__ = "messages"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(100), nullable=False)
    email = Column(String(150), nullable=False)
    phone = Column(String(20))
    message = Column(Text, nullable=False)
    created_at = Column(TIMESTAMP, server_default=func.now())

class Project(Base):
    __tablename__ = "projects"
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(200), nullable=False)
    description = Column(Text, nullable=False)
    image_url = Column(String(500), nullable=False)
    live_url = Column(String(500), nullable=False)
    created_at = Column(TIMESTAMP, server_default=func.now())
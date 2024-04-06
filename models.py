from sqlalchemy import create_engine
from sqlalchemy.orm import DeclarativeBase, sessionmaker
from sqlalchemy import Column, String, DateTime, Integer, func, Text
from config import (
    POSTGRES_DB, 
    POSTGRES_HOST, 
    POSTGRES_PASSWORD, 
    POSTGRES_PORT, 
    POSTGRES_USER,)

engine = create_engine(f"postgresql+psycopg2://{POSTGRES_USER}:{POSTGRES_PASSWORD}@{POSTGRES_HOST}:{POSTGRES_PORT}/{POSTGRES_DB}",)
Session = sessionmaker(bind=engine)

class Base(DeclarativeBase):
    pass

class Advertisement(Base):
    __tablename__ = 'advertisement'
    
    id = Column(Integer, primary_key=True)
    title = Column(String, nullable=False)
    description = Column(String, nullable=False)
    creation_datetime = Column(DateTime, server_default=func.now())
    owner = Column(String, nullable=False)

Base.metadata.create_all(bind=engine)
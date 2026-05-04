from sqlalchemy import DATETIME, Column, Integer, String , DATETIME_
from sqlalchemy.sql import func
from ..core.database import Base


class User(Base):
    __tablename__ = "users" 
    id = Column(Integer, primary_key=True)
    username = Column(String(50) , unique=True , nullable=False)
    email = Column(String(100) , unique=True , nullable=False)
    password = Column(String(255) , nullable=False)
    created_at = Column(DATETIME, server_default=func.now())

    

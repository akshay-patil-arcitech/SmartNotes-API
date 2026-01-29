from database import BASE
from typing import Annotated
from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from datetime import datetime
from sqlalchemy.sql import func

class User(BASE):
    __tablename__="users"
    id = Column(Integer,primary_key=True)
    name = Column(String)
    email = Column(String,unique=True)
    password = Column(String)
    created_at = Column(DateTime,server_default=func.now())
    

from database import BASE
from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from datetime import datetime
from sqlalchemy.sql import func


class Note(BASE):
    __tablename__="notes"
    id = Column(Integer,primary_key=True)
    title = Column(String)
    content = Column(String)
    owner_id = Column(Integer,ForeignKey("users.id"))
    created_at = Column(DateTime,server_default=func.now())
    updated_on = Column(DateTime,onupdate=datetime.utcnow)
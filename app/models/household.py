# app/models/household.py

from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.sql import func
from app.database import Base

class Household(Base):
    __tablename__ = "households"
    
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(255), nullable=False) # String(255) is the máx. length for this text (255 characters)
    created_at = Column(DateTime(timezone=True), server_default=func.now())

from sqlalchemy import Column, ForeignKey, Integer, String, Float, DateTime, Enum
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func

from db import Base

class Medicine(Base):
    __tablename__ = "medicines"
    medicine_id = Column(Integer, primary_key=True,index=True)
    name = Column(String(200), nullable=False, unique=False)
    med_type = Column(String(80), nullable=False, unique=False)
    ingredients = Column(String(500), nullable=True, unique=False)
    category = Column(String(80), nullable=True, unique=False)
    
    def __repr__(self):
        return f'Medicine(medicine_id={self.medicine_id}, name={self.name}, med_type={self.med_type}, ingredients={self.ingredients}, category={self.category})'
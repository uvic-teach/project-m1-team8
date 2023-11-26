from sqlalchemy import Column, ForeignKey, Integer, String, Float, DateTime, Enum
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func

from db import Base

class Nurse(Base):
    __tablename__ = "nurses"
    nurse_id = Column(Integer, primary_key=True,index=True)
    name = Column(String(200), nullable=False, unique=False)
    license_id = Column(String(80), nullable=False, unique=False)
    
    def __repr__(self):
        return f'Nurse(nurse_id={self.nurse_id}, name={self.name}, license_id={self.license_id})'
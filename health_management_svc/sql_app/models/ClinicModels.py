from sqlalchemy import Column, ForeignKey, Integer, String, Float, DateTime, Enum
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func

from db import Base

class Clinic(Base):
    __tablename__ = "clinics"
    clinic_id = Column(Integer, primary_key=True,index=True)
    name = Column(String(200), nullable=False, unique=False)
    phone_number = Column(String(200), nullable=True, unique=False)
    address = Column(String(200), nullable=True, unique=False)
    area = Column(String(200), nullable=True, unique=False)
    provice = Column(String(200), nullable=True, unique=False)
    
    def __repr__(self):
        return f'Clinic(clinic_id={self.clinic_id}, name={self.name}, phone_number={self.phone_number}, address={self.address}, area={self.area}, provice={self.provice} )'
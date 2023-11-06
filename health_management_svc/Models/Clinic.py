from sqlalchemy import Column, ForeignKey, Integer, String, Float
from sqlalchemy.orm import relationship

from db import Base

class Clinic(Base):
    __tablename__ = "clinic"

    clinic_id = Column(Integer, primary_key=True,index=True)
    name = Column(String(200), nullable=False,index=True)
    address = Column(String(200), nullable=False)
    phone = Column(String(20))
    def __repr__(self):
        return f'ClinicModel(name:{self.name}, address={self.address},phone:{self.phone})'
    
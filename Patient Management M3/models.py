from sqlalchemy import Column, ForeignKey, Integer, String, Float
from sqlalchemy.orm import relationship

from db import Base

class UserHealthInfo(Base):
    _tablename_ = "items"

    patient_name = Column(String(80), nullable=False, unique=True, index=True)
    patient_id = Column(Integer, primary_key=True, index=True)
    height = Column(Integer, primary_key=True, index=True)
    weight = Column(Integer, primary_key=True, index=True)
    blood_type = Column(String(80), nullable=False, unique=True, index=True)
    blood_pressure = Column(Integer, primary_key=True, index=True)
    allergies = Column(String(80), nullable=False, unique=True, index=True)
    complication = Column(String(80), nullable=False, unique=True, index=True)

    def __repr__(self):
        return 'UserModel(patient_name=%s, patient_id=%s)' % (self.patient_name, self.patient_id)



    
from sqlalchemy import Column, ForeignKey, Integer, String, Float, DateTime
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func

from db import Base
from enum import Enum

class ERBookingStatus(Enum):
    WAITING = "waiting"
    PROCESSING = "processing"
    CONFIRMED = "confirmed"
    CANCELED = "canceled"
    OVERDUE = "overdue"

class ERBooking(Base):
    __tablename__ = "erbookings"
    booking_id = Column(Integer, primary_key=True,index=True)
    patient_id = Column(Integer, nullable=False, unique=False)
    booking_time = Column(DateTime(timezone=True), server_default=func.now())
    status = Column(String(80), nullable=False, unique=False)
    last_updated = Column(DateTime(timezone=True), server_default=func.now())
    estimated_time = Column(String(80), nullable=False, unique=False)
    area = Column(String(200), nullable=False, unique=False)
    hospital_name = Column(String(200), nullable=False, unique=False)
    slot_number = Column(Integer, nullable=False, unique=False)
    
    def __repr__(self):
        return f'ERBooking(booking_time={self.booking_time}, status={self.status}, last_updated={self.last_updated}, estimated_time={self.estimated_time}, area={self.area}, hospital_name={self.hospital_name}, slot_number=%{self.slot_number})'
    
class ERQueue(Base):
    __tablename__ = "erqueues"
    queue_id = Column(Integer, primary_key=True,index=True)
    estimated_waiting_time = Column(String(80), nullable=False, unique=False)
    area = Column(String(80), nullable=False, unique=False)
    hospital_name = Column(String(80), nullable=False, unique=True, index=True)
    current_capacity = Column(Integer, nullable=False, unique=False)
    max_capacity = Column(Integer, nullable=False, unique=False)

    
    def __repr__(self):
        return f'ERQueue(estimated_waiting_time={self.estimated_waiting_time}, area={self.area}, hospital_name={self.hospital_name}, current_capacity={self.current_capacity}, max_capacity={self.max_capacity})'
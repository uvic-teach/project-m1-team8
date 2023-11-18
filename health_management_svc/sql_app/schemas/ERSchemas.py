# build a schema using pydantic
from pydantic import BaseModel
from typing import List, Optional
from datetime import datetime
from sql_app.models.ERModels import ERBookingStatus

class ERBookingBase(BaseModel):
    patient_id: int
    status: str
    estimated_time: str
    area: str
    hospital_name: str
    slot_number: int

class ERBookingCreate(ERBookingBase):
    pass

class ERBooking(ERBookingBase):
    booking_id: int

    class Config:
        orm_mode = True

class ERQueueBase(BaseModel):
    estimated_waiting_time: str
    area: str
    hospital_name: str
    current_capacity: int
    max_capacity: int

class ERQueueCreate(ERQueueBase):
    pass

class ERQueue(ERQueueBase):
    queue_id: int

    class Config:
        orm_mode = True
        

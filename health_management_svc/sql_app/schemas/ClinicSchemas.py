# build a schema using pydantic
from pydantic import BaseModel
from typing import List, Optional
from datetime import datetime

class ClinicBase(BaseModel):
    name: str
    address: str
    phone_number: str
    address: str
    area: str
    province: str
    
class ClinicCreate(ClinicBase):
    pass

class Clinic(ClinicBase):
    clinic_id: int

    class Config:
        orm_mode = True
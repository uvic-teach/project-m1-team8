from typing import List, Optional

from pydantic import BaseModel


class UserHealthInfoBase(BaseModel):
    patient_name: str
    patient_id: str
    height: float
    weight: float
    blood_type: str
    blood_pressure: float
    allergies: str
    complications: str


class UserHealthInfoCreate(UserHealthInfoBase):
    pass

class BasicHealthInfoBase(BaseModel):
    height: float
    weight: float
    blood_type: str
    blood_pressure: float
    allergies: str
    complications: str


class UserHealthInfo(BasicHealthInfoBase):


    class Config:
        orm_mode = True

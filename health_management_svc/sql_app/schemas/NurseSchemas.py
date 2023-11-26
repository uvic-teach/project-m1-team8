# build a schema using pydantic
from pydantic import BaseModel
from typing import List, Optional
from datetime import datetime

class NurseBase(BaseModel):
    name: str
    license_id: str
    
class NurseCreate(NurseBase):
    pass

class Nurse(NurseBase):
    nurse_id: int

    class Config:
        orm_mode = True
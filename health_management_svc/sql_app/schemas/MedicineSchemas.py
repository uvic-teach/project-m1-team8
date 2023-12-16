# build a schema using pydantic
from pydantic import BaseModel
from typing import List, Optional
from datetime import datetime

class MedicineBase(BaseModel):
    name: str
    med_type: str
    ingredients: str
    category: str
    
class MedicineCreate(MedicineBase):
    pass

class Medicine(MedicineBase):
    medicine_id: int

    class Config:
        orm_mode = True
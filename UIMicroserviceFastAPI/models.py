from database import Base
from sqlalchemy import Column, Integer, String, Boolean, Float

class Notification(Base):
    __tablename__ = 'notifications'

    id = Column(Integer, primary_key =True, index=True)
    amount = Column(Float)
    category = Column(String)
    description = Column(String)
    is_income = Column(Boolean)
    date = Column(String)
    
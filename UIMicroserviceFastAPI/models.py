from database import Base
from sqlalchemy import Column, Integer, String

class Notification(Base):
    __tablename__ = 'notifications'

    id = Column(Integer, primary_key =True, index=True)
    message = Column(String)
    username = Column(String)
    date = Column(String)
    
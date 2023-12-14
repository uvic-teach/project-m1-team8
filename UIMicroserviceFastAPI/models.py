from database import Base
from sqlalchemy import Column, Integer, String, DateTime, Boolean
import datetime
from sqlalchemy.sql import func

class Notification(Base):
    __tablename__ = 'notifications'

    notification_id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    user_id = Column(Integer)
    message = Column(String(500))
    time_sent = Column(DateTime(timezone=True), default=func.now())


class Bookings(Base):
    __tablename__ = 'bookings'

    booking_id = Column(Integer, primary_key =True, index=True)
    user_id = Column(Integer, nullable=False)
    hospital_name = Column(String(100), nullable=False)
    wait_time = Column(DateTime(timezone=True),default=datetime.datetime.now())

    
class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    username = Column(String(50),  nullable=False)
    email = Column(String(100), unique=True, nullable=False)
    password = Column(String(100), nullable=False)

class TokenTable(Base):
    __tablename__ = 'token'

    user_id = Column(Integer)
    access_toke = Column(String(450), primary_key=True)
    refresh_toke = Column(String(450),nullable=False)
    status = Column(Boolean)
    created_date = Column(DateTime, default=datetime.datetime.now)
    
    
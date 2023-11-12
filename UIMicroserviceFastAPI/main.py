from flask_sqlalchemy import SQLAlchemy
from fastapi import FastAPI, HTTPException, Depends, status
from sqlalchemy import Column, Integer, String, DateTime, Boolean
from database import SessionLocal, engine, Base
from sqlalchemy.orm import Session
from typing import Annotated, List
from pydantic import BaseModel, Field
import datetime
import models
from models import User, Notification, TokenTable, Bookings
import schemas
import os
import jwt
from fastapi.middleware.cors import CORSMiddleware
from fastapi.security import OAuth2PasswordBearer
from auth_bearer import JWTBearer
from functools import wraps
from utils import create_access_token,create_refresh_token,verify_password,get_hashed_password
ACCESS_TOKEN_EXPIRE_MINUTES = 30  # 30 minutes
REFRESH_TOKEN_EXPIRE_MINUTES = 60 * 24 * 7 # 7 days
ALGORITHM = "HS256"
JWT_SECRET_KEY = "narscbjim@$@&^@&%^&RFghgjvbdsha"   # should be kept secret
JWT_REFRESH_SECRET_KEY = "13ugfdfgh@#$%^@&jkl45678902"


#from Services import ERService, Authentication, NotificationService, TriageDataGetter
#from components import notification, Booking, AccountInfo, UserHealthInfo

app = FastAPI()

origins = [
   'http://localhost:3000'
]

app.add_middleware(
   CORSMiddleware,
   allow_origins = origins,
   allow_credentials = True,
   allow_methods=['*'],
   allow_headers=['*']
)

def token_required(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
    
        payload = jwt.decode(kwargs['dependencies'], JWT_SECRET_KEY, ALGORITHM)
        user_id = payload['sub']
        data= kwargs['session'].query(models.TokenTable).filter_by(user_id=user_id,access_toke=kwargs['dependencies'],status=True).first()
        if data:
            return func(kwargs['dependencies'],kwargs['session'])
        
        else:
            return {'msg': "Token blocked"}
        
    return wrapper

currentTime = datetime.datetime.now()


class NotificationsBase(BaseModel):
    class Config:
        arbitrary_types_allowed = True

    notification_id: int = Field(example=121)
    patient_id: int = Field(example=12313)
    message: str = Field(example="meow")
    time_sent: DateTime = Field(example= None) 

class BookingsBase(BaseModel):
    class Config:
        arbitrary_types_allowed = True
    booking_id: int = Field(example=123456789)
    patient_id: int = Field(example=101010010)
    message: str = Field(example="Booking time")
    wait_time: DateTime = Field(example=None) 
    
class NotificationModel(NotificationsBase):
   id: int

   class Config:
      orm_mode =  True
      arbitrary_types_allowed = True

class BookingsModel(BookingsBase):
   id: int

   class Config:
      orm_mode =  True
      arbitrary_types_allowed = True

def get_db():
  db = SessionLocal()
  try: 
    yield db
  finally: db.close()

Base.metadata.create_all(engine)

def get_session():
    session = SessionLocal()
    try:
        yield session
    finally:
        session.close()

db_dependancy = Annotated[Session, Depends(get_db)]

models.Base.metadata.create_all(bind=engine)

class UserHealthInfo(BaseModel):
    patient_id: str = Field(example="12345")
    patient_age: int = Field(example = 20)
    height: float = Field(example=175.3)
    weight: float = Field(example=68.5)
    blood_type: str = Field(example="A+")
    blood_pressure: float = Field(example=120.8)

@app.get("/")
async def homepage():
    return "MisterED User Interface"

@app.get("/notifications/", response_model=List[NotificationModel])
async def get_notifications(db: db_dependancy, skip: int = 0, limit: int = 100):
   notifications = db.query(models.Notification).offset(skip).limit(limit).all()
   return notifications
    
@app.post("/notifications/", response_model=NotificationModel)
async def create_notification(notification: NotificationsBase, db: db_dependancy):
  db_notification = models.Notification(**notification.model_dump())
  db.add(db_notification)
  db.commit()
  db.refresh(db_notification)
  return db_notification

# AUTHENTICATION API CALLS

@app.post("/authentication/create")
async def register_user(user: schemas.UserCreate, session: Session = Depends(get_session)):
    existing_user = session.query(models.User).filter_by(email=user.email).first()
    if existing_user:
        raise HTTPException(status_code=400, detail="Email already registered")

    encrypted_password = get_hashed_password(user.password)

    new_user = models.User(username=user.username, email=user.email, password=encrypted_password )

    session.add(new_user)
    session.commit()
    session.refresh(new_user)

    return {"message":"user created successfully"}

@app.post("/authentication/update")
async def change_password(request: schemas.changepassword, db: Session = Depends(get_session)):
    user = db.query(models.User).filter(models.User.email == request.email).first()
    if user is None:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="User not found")
    
    if not verify_password(request.old_password, user.password):
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Invalid old password")
    
    encrypted_password = get_hashed_password(request.new_password)
    user.password = encrypted_password
    db.commit()
    
    return {"message": "Password changed successfully"}
   
@app.get("/authentication/login")
def login(request: schemas.requestdetails, db: Session = Depends(get_session)):
    user = db.query(User).filter(User.email == request.email).first()
    if user is None:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Incorrect email")
    hashed_pass = user.password
    if not verify_password(request.password, hashed_pass):
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Incorrect password"
        )
    
    access= create_access_token(user.id)
    refresh = create_refresh_token(user.id)

    token_db = models.TokenTable(user_id=user.id,  access_toke=access,  refresh_toke=refresh, status=True)
    db.add(token_db)
    db.commit()
    db.refresh(token_db)
    return {
        "access_token": access,
        "refresh_token": refresh,
    }

@app.post('/authentication/logout')
def logout(dependencies=Depends(JWTBearer()), db: Session = Depends(get_session)):
    token=dependencies
    payload = jwt.decode(token, JWT_SECRET_KEY, ALGORITHM)
    user_id = payload['sub']
    token_record = db.query(models.TokenTable).all()
    info=[]
    for record in token_record :
        print("record",record)
        if (datetime.utcnow() - record.created_date).days >1:
            info.append(record.user_id)
    if info:
        existing_token = db.query(models.TokenTable).where(TokenTable.user_id.in_(info)).delete()
        db.commit()
        
    existing_token = db.query(models.TokenTable).filter(models.TokenTable.user_id == user_id, models.TokenTable.access_toke==token).first()
    if existing_token:
        existing_token.status=False
        db.add(existing_token)
        db.commit()
        db.refresh(existing_token)
    return {"message":"Logout Successfully"} 

############################ ER API CALLS

@app.get("/er/loadTime/{hospital_id}")
async def check_er_load(hospital_id: int):
  return {"message": "Current wait time is 2 hours"}


@app.get("/er/booking/{booking_id}")
async def get_er_booking(booking_id: int):
  return {
      "booking_id": booking_id
  }

@app.post("/er/booking/request")
async def create_er_request(booking: BookingsBase, db: db_dependancy):
  db_bookings = models.Bookings(**booking.model_dump())
  db.add(db_bookings)
  db.commit()
  db.refresh(db_bookings)
  return db_bookings

@app.post("/er/booking/cancel")
async def cancel_er_booking(booking_id: int, booking: BookingsBase, db: db_dependancy):
  db_bookings = models.Bookings(**booking.model_dump())
  if db_bookings is None:
    raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="the booking does not exist")
  db.delete(db_bookings)
  db.commit()
  db.refresh(db_bookings)
  return {
    "message": "booking successfully cancelled",
    "booking_id": booking_id
  }

### TRIAGE API CALLS

@app.get("/triage/display/element/{triage_id}")
async def get_triage_element(self, patient_id:str, triage_id:str ):
   '''
    request the patients triage instances list from TriageManagement and 
    display it on the webpage
    Args:
      patient_id(str): ID of patient to check
    Changes to page:
      load triage history page with a table containing the one selected
      element from the list of triage instances
    Returns:
      none
    '''
    
   return{
          "message": "User Triage information successfully displayed",
          "patient_id": patient_id,
          "triage_id": triage_id
   }
   
   
@app.get("/triage/display/list/{triage_id}")
def get_triage_list(self, patient_id:str):
    '''
    request the patients triage instances list from TriageManagement and 
    display it on the webpage
    Args:
      patient_id(str): ID of patient to check
    Changes to page:
      load triage history page a table containing the full 
      list of triage instances
    Returns:
      none
    '''
    return{
            "message": "Patient triage instances list successfully displayed",
            "patient_id": patient_id
    }
   
   

  

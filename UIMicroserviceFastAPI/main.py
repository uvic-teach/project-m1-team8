from fastapi import FastAPI, HTTPException, Depends
from database import SessionLocal, engine
from sqlalchemy.orm import Session
from typing import Annotated, List
from pydantic import BaseModel, Field
from datetime import timedelta
import models
from fastapi.middleware.cors import CORSMiddleware

#from Services import ERService, Authentication, NotificationService, TriageDataGetter
#from components import notification, Booking, AccountInfo, UserHealthInfo

app = FastAPI()
#notificationService = NotificationService()

#erService = erService()
origins = [
   'http://localhost:3000'
]

app.add_middleware(
   CORSMiddleware,
   allow_origins = origins,
)

class AccountInfo(BaseModel):
    username: str = Field(example="username")
    password: str = Field(example="password123")

class NotificationBase(BaseModel):
    message: str = Field(example = "Message")
    username: str = Field(example="username")
    date: str = Field(example="password123")

class NotificationModel(NotificationBase):
   id: int

   class Config:
      orm_mode=  True

def get_db():
  db = SessionLocal()
  try: 
    yield db
  finally: db.close()

db_dependancy = Annotated[Session, Depends(get_db)]

models.Base.metadata.create_all(bind=engine)



  

class UserHealthInfo(BaseModel):
    patient_id: str = Field(example="12345")
    patient_age: int = Field(example = 20)
    height: float = Field(example=175.3)
    weight: float = Field(example=68.5)
    blood_type: str = Field(example="A+")
    blood_pressure: float = Field(example=120.8)

class Booking(BaseModel):
    patient_id: int = Field(example = 4234232)
    booking_id: int = Field(example = 42342)
    hospital_id: int = Field(example = 5)
    booking_time: timedelta = Field(example = 2)
    hospital_name: str = Field(example = "Chilliwack General Hospital")
    estimated_wait: str = Field(example = "2 hours")
    queue_position: int = Field(example = 2)

#functions definition

@app.get("/")
async def homepage():
    return "MisterED User Interface"

@app.get("/notifications/", response_model=List[TransactionModel])
async def get_notifications(db: db_dependancy, skip: int = 0, limit: int = 100):
   notifications = db.query(models.Notifcation).offset(skip).limit(limit).all()
   return notifications
    



@app.post("/notifications/", response_model=NotificationModel)
async def create_notification(notification: NotificationBase, db: db_dependancy):
  db_notification = models.Notification(**notification.dict())
  db.add(db_notification)
  db.commit()
  db.refresh(db_notification)
  return db_notification
    # NotificationService.create_notification(user_id, message) append to notification_list 
    # Send to user

@app.get("/er/loadTime/{hospital_id}")
async def check_er_load(hospital_id: int):
  return {"message": "Current wait time at Chilliwack General Hospital is 2 hours"}

@app.get("/er/booking/{booking_id}")
async def get_er_booking(booking_id: int):
  #get booking id from erService
  return {
      "patient_id": user_id,
      "booking_id": booking_id,
      "hospital_id": hospital_id,
      "booking_time": booking_timedelta,
      "hospital_name": "Chilliwack General Hospital",
      "estimated_wait": "2 hours",
      "queue_position": 6
  }

@app.post("/er/booking/request")
async def create_er_request(patient_id: int):
  #erService does work to create booking
  return {
          "message": "Booking request successfull.",
          "patient_id": user_id,
          "booking_id": booking_id,
          "hospital_id": hospital_id,
          "booking_time": booking_timedelta,
          "hospital_name": "Chilliwack General Hospital",
          "estimated_wait": "2 hours",
          "queue_position": 6
        }

@app.post("/er/booking/cancelbooking")
async def cancel_er_booking(booking_id: int):
  #clear booking from erqueue in erService
  return {
        "message": "Booking cancellation request successfull.",
        "booking_id": booking_id,
  }

@app.get("/triage/display/element/{triage_id}")
async def get_triage_element(self, patient_id:str, triage_id:str ):
   """
    request the patients triage instances list from TriageManagement and 
    display it on the webpage
    Args:
      patient_id(str): ID of patient to check
    Changes to page:
      load triage history page with a table containing the one selected
      element from the list of triage instances
    Returns:
      none
    """
   return{
          "message": "User Triage information successfully displayed",
          "patient_id": patient_id,
          "triage_id": triage_id
   }
   
   
@app.get("/triage/display/list/{triage_id}")
def get_triage_list(self, patient_id:str):
    """
    request the patients triage instances list from TriageManagement and 
    display it on the webpage
    Args:
      patient_id(str): ID of patient to check
    Changes to page:
      load triage history page a table containing the full 
      list of triage instances
    Returns:
      none
    """
    return{
            "message": "Patient triage instances list successfully displayed",
            "patient_id": patient_id,
    }
   
   
@app.post("/authentication/account/create")
async def request_account_creation(self, account_info: AccountInfo, health_info: UserHealthInfo):
   #Requests patient management service to create new account
   return{
        "message": "Account creation successfull",
        "account_info": account_info,
        "health_info": health_info
   }

@app.post("/authentication/account/update")
async def request_account_update(self, new_username:str, new_password:str ):
   #Requests patient management service to update account information
   account_info = 0
   return{
        "message": "Account update successfull.",
        "account_info": account_info,
        "new_username": new_username,
        "new_password": new_password
   }
   
@app.get("/authentication/account/validate")
async def request_account_validation(self, username:str, password: str):
   #Requests patient management service to validate username and password
   return{
        "message": "Log-in successfull.",
   }
  

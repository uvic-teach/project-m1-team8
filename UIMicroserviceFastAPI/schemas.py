from pydantic import BaseModel
import datetime

class UserCreate(BaseModel):
    username: str
    email: str
    password: str

class requestdetails(BaseModel):
    email:str
    password:str
        
class TokenSchema(BaseModel):
    access_token: str
    refresh_token: str

class changepassword(BaseModel):
    email:str
    old_password:str
    new_password:str

class TokenCreate(BaseModel):
    user_id:str
    access_token:str
    refresh_token:str
    status:bool
    created_date:datetime.datetime

class NotificationsBase(BaseModel):
    user_id: int 
    message: str 
    time_sent: datetime.datetime

class BookingsBase(BaseModel):
    user_id: int 
    message: str 
    wait_time: str

class UserBase(BaseModel):
    id: int 
    username: str
    password: str 
    email: str 

class NotificationCreate(NotificationsBase):
    pass

class BookingCreate(BookingsBase):
    pass

class NotificationModel(NotificationsBase):
   notification_id: int

   class Config:
        from_attributes =  True

class BookingsModel(BookingsBase):
   booking_id: int

   class Config:
        from_attributes =  True


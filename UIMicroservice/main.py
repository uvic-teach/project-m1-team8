from fastapi import FastAPI
from Services import ERService, Authentication, NotificationService, TriageDataGetter
from components import notification

app = FastAPI()
#notificationService = NotificationService()

#functions definition

@app.get("/")
  async def homepage():
    return "MisterED User Interface"

@app.get("/notification/{user_id}")
async def get_notifications(user_id: int)
    return {
            "user_id": user_id
            "notification_list": []
           }

@app.post("/notification/{user_id}")
async def add_notification(user_id: int, message: string):
    # NotificationService.create_notification(user_id, message) append to notification_list 
  return {"message": Notification was successfully added"}

@app.post("/er/loadTime/{hospital_id}")
async def check_er_load(hospital_id: int):
  return {"message": "Current wait time at Chilliwack General Hospital is 2 hours"}

@app.post("/er/booking/request")
async def create_er_request(patient_id: int, priority_level: int):
  return {"Current wait time at Chilliwack General Hospital is 2 hours"}





from fastapi import FastAPI
from Services import ERService, Authentication, NotificationService, TriageDataGetter
from components import notification

app = FastAPI()
#notificationService = NotificationService()

#functions definition

@app.get("/")
  async def homepage():
    return "MisterED User Interface"

@app.get("/notificationSvc/{user_id}")
async def get_notifications(user_id: int)
    return {
            "user_id": user_id
            "notification_list": []
           }
@app.post("/notificationSvc/{user_id}")
async def add_notification(user_id: int, message: string):
    # notificationService.create_notification(user_id, message)


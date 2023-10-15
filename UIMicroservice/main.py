from fastapi import FastAPI
from Services import ERService, Authentication, NotificationService, TriageDataGetter
from components import notification, booking
from fastapi.openapi.utils import get_openapi

app = FastAPI()
#notificationService = NotificationService()

#erService = erService()

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
async def create_notification(user_id: int, message: string):
    # NotificationService.create_notification(user_id, message) append to notification_list 
  return {"message": Notification was successfully created"}

@app.post("/er/loadTime/{hospital_id}")
async def check_er_load(hospital_id: int):
  return {"message": "Current wait time at Chilliwack General Hospital is 2 hours"}

@app.get("er/booking/{booking_id}):
async def get_er_booking(booking_id: int)
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
async def create_er_request(patient_id: int, ):
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

@app.post("/er/booking/{booking_id}/cancelbooking")
async def cancel_er_booking(booking_id: int):
  #clear booking from erqueue in erService
  return {
        "message": "Booking cancellation request successfull.",
        "booking_id": booking_id
        "user_id": user_id
  }

def custom_openapi():
    if app.openapi_schema:
        return app.openapi_schema
    openapi_schema = get_openapi(
        title="Custom title",
        version="2.5.0",
        summary="This is a very custom OpenAPI schema",
        description="Here's a longer description of the custom **OpenAPI** schema",
        routes=app.routes,
    )
    openapi_schema["info"]["x-logo"] = {
        "url": "https://fastapi.tiangolo.com/img/logo-margin/logo-teal.png"
    }
    app.openapi_schema = openapi_schema
    return app.openapi_schema



app.openapi = custom_openapi

    




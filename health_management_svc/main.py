from fastapi import Depends, FastAPI, HTTPException
from fastapi.responses import JSONResponse
from sql_app import models
from db import get_db, engine
import sql_app.models as models
import sql_app.schemas as schemas
from sql_app.repositories import ERBookingRepo, ERQueueRepo
from sqlalchemy.orm import Session
import uvicorn
from typing import List,Optional
from fastapi.encoders import jsonable_encoder


import random

app = FastAPI(
    title="Health Service Management Microservice",
    description="Sample Health Service Management Microservice",
    version="0.9.9"
)

models.Base.metadata.create_all(bind=engine)
### Helper functions for testing
def get_patient_location(patient_id: int):
    return "Victoria"

def get_hospital_in_location(location: str):
    return ["Royal Jubilee Hospital", "hospital2", "hospital3", "hospital4", "hospital5", "hospital6"]

@app.exception_handler(Exception)
def validation_exception_handler(request, err):
    base_error_message = f"Failed to execute: {request.method}: {request.url}"
    return JSONResponse(status_code=400, content={"message": f"{base_error_message}. Detail: {err}"})

@app.get("/")
async def homepage():
    return "Health Service Management"
    
# @app.get("/triage")
# async def get_triage(triage_id):
#     return {
#             "triage_id": triage_id,
#             "patient_id": 0,
#             "perform_date": "2021-01-01",
#             "status": "PROCESSING",
#             }

# @app.get("/triage/result")
# async def get_triage_result(triage_id):
#     return {
#             "triage_id": triage_id,
#             "perform_date": "2021-01-01",
#             "available_date": "2021-01-02",
#             "patient_name": "Alice Smith",
#             "summary": "Summary 1",
#             "detail": "Detail 1",
#             "suggestion": {
#                 "triage_id": triage_id,
#                 "suggestion": "Take medicine"
#             }
#             }

# @app.post("/triage/submit")
# async def submit_triage(patient_id: int, patient_name: str):
#     # triageManager.create_triage_result(patient_id, patient_name)
#     return {
#         "message": "Triage answer submitted successfully",
#     }

# @app.get("/triage/status")
# async def get_triage_status(triage_id: int):
#     # status = triageManager.get_triage_status(triage_id)
#     return {"message": "Triage status retrieved successfully", "triage_id": triage_id, "status": "PROCESSING"}

# @app.get("/triage/suggestion")
# async def get_triage_suggestion(triage_id: int):
#     # suggestion = triageManager.get_triage_suggestion(triage_id)
#     suggestion = "Take medicine"
#     return {"message": "Triage suggestion retrieved successfully", "triage_id": triage_id, "suggestion": suggestion}



@app.get("/er/booking", tags=["ERBooking"],response_model=schemas.ERBooking,status_code=201)
async def get_er_booking(booking_id: int, db: Session = Depends(get_db)):
    db_booking = ERBookingRepo.fetch_by_booking_id(db, booking_id=booking_id)
    if not db_booking:
        raise HTTPException(status_code=400, detail="Booking not found!")
    
    return db_booking

@app.get("/er/bookings", tags=["ERBooking"],response_model=List[schemas.ERBooking],status_code=201)
async def get_all_er_bookings(hospital_name: Optional[str] = None, db: Session = Depends(get_db)):
    if hospital_name:
        db_bookings = ERBookingRepo.fetch_by_hospital_name(db, hospital_name)
    else:
        db_bookings = ERBookingRepo.fetch_all(db)
    return db_bookings

@app.get("/er/bookings/patient", tags=["ERBooking"],response_model=List[schemas.ERBooking],status_code=201)
async def get_all_er_bookings(patient_id: int, db: Session = Depends(get_db)):
    db_bookings = ERBookingRepo.fetch_by_patient_id(db, patient_id)
    if not db_bookings:
        raise HTTPException(status_code=400, detail="No booking found for the patient!")
    return db_bookings

@app.get("/er/booking/status", tags=["ERBooking"],status_code=201)
async def get_er_booking_status(booking_id: int, db: Session = Depends(get_db)):
    db_booking = ERBookingRepo.fetch_by_booking_id(db, booking_id=booking_id)
    if not db_booking:
        raise HTTPException(status_code=400, detail="Booking not found!")
    
    return {
        "message": "Booking status retrieved successfully",
        "booking_id": booking_id,
        "status": db_booking.status
        }

@app.post("/er/booking/create", tags=["ERBooking"],response_model=schemas.ERBooking,status_code=201)
async def create_er_booking(patient_id: int, db: Session = Depends(get_db)):
    """
    Create an ER Booking and store it in the database
    """
    area = get_patient_location(patient_id)
    hospital_list = get_hospital_in_location(area)
    min_est_wait_time = None
    hospital_name = None
    slot_number = None

    for hospital in hospital_list:
        er_queue = ERQueueRepo.fetch_by_hospital_name(db, hospital)
        if not er_queue: continue
        if er_queue.current_capacity < er_queue.max_capacity:
            if min_est_wait_time is None:
                min_est_wait_time = er_queue.estimated_waiting_time
                hospital_name = hospital
                slot_number = er_queue.current_capacity + 1
            elif er_queue.estimated_waiting_time < min_est_wait_time:
                min_est_wait_time = er_queue.estimated_waiting_time
                hospital_name = hospital
                slot_number = er_queue.current_capacity + 1

    er_booking_request: schemas.ERBookingCreate = schemas.ERBookingCreate(
        patient_id=patient_id,
        status="waiting",
        estimated_time=min_est_wait_time,
        area=area,
        hospital_name=hospital_name,  
        slot_number=slot_number
    )
    db_booking = ERBookingRepo.fetch_by_patient_id(db, patient_id=er_booking_request.patient_id)
    if db_booking:
        raise HTTPException(status_code=400, detail="Patient already has a booking!")

    db_booking = await ERBookingRepo.create(db=db, booking=er_booking_request)

    db_queue = ERQueueRepo.fetch_by_hospital_name(db, hospital_name=db_booking.hospital_name)
    
    #^ update queue
    db_queue.current_capacity += 1
    db_queue.estimated_waiting_time = str(int(db_queue.estimated_waiting_time) + int(db_queue.estimated_waiting_time)/db_queue.current_capacity)
    
    await ERQueueRepo.update(db=db, er_queue_data=db_queue)
    
    return db_booking

@app.post("/er/booking/cancel", tags=["ERBooking"],status_code=201)
async def cancel_er_booking(booking_id: int, db: Session = Depends(get_db)):
    db_booking = ERBookingRepo.fetch_by_booking_id(db, booking_id=booking_id)
    if not db_booking:
        raise HTTPException(status_code=400, detail="Booking not found!")
    await ERBookingRepo.delete(db=db, booking_id=booking_id)
    return {
        "message": "Booking cancelled successfully",
        "booking_id": booking_id
        }
    
@app.get("/er/load", tags=["ERQueue"],status_code=201)
async def check_er_load_by_hospital(hospital_name: str, db: Session = Depends(get_db)):
    db_er_queue = ERQueueRepo.fetch_by_hospital_name(db, hospital_name)
    if not db_er_queue:
        raise HTTPException(status_code=400, detail="Hospital not found!")
    
    return {"message": f"Current ER Queue at {db_er_queue.hospital_name} ({db_er_queue.area}) is {db_er_queue.current_capacity}. The estimated wait time is {db_er_queue.estimated_waiting_time}."}


#! FOR TESTING PURPOSES ONLY
@app.post("/er/queue/create", tags=["ERQueue"],response_model=schemas.ERQueue,status_code=201)
async def create_er_queue(hospital_name: str, db: Session = Depends(get_db)):
    db_er_queue = ERQueueRepo.fetch_by_hospital_name(db, hospital_name)
    if db_er_queue:
        raise HTTPException(status_code=400, detail="Hospital's ER Queue already exist!")
    current_capacity=random.randint(100, 300)
    queue: schemas.ERQueueCreate = schemas.ERQueueCreate(
                                        estimated_waiting_time=str(random.randint(1, 10)*current_capacity),
                                        area="Victoria",
                                        hospital_name=hospital_name,
                                        current_capacity=current_capacity,
                                        max_capacity=300
                                    )
    return await ERQueueRepo.create(db=db, queue=queue)

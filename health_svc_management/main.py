from fastapi import FastAPI
# from services import TriageManament, ERService

app = FastAPI()
# triageManager = TriageManament()
# eRService = ERService()

@app.get("/triage/{triage_id}")
async def get_triage(triage_id):
    return {
            "triage_id": triage_id,
            "patient_id": 0,
            "perform_date": "2021-01-01",
            "status": "PROCESSING",
            }

@app.get("/triage/result/{triage_id}")
async def get_triage_result(triage_id):
    return {
            "triage_id": triage_id,
            "perform_date": "2021-01-01",
            "available_date": "2021-01-02",
            "patient_name": "Alice Smith",
            "summary": "Summary 1",
            "detail": "Detail 1",
            "suggestion": {
                "triage_id": triage_id,
                "suggestion": "Take medicine"
            }
            }

@app.post("/triage/submit")
async def submit_triage(patient_id: int, patient_name: str):
    # triageManager.create_triage_result(patient_id, patient_name)
    return {
        "message": "Triage answer submitted successfully",
    }

@app.get("/triage/status/{triage_id}")
async def get_triage_status(triage_id: int):
    # status = triageManager.get_triage_status(triage_id)
    return {"message": "Triage status retrieved successfully", "triage_id": triage_id, "status": "PROCESSING"}

@app.get("/triage/suggestion/{triage_id}")
async def get_triage_suggestion(triage_id: int):
    # suggestion = triageManager.get_triage_suggestion(triage_id)
    suggestion = "Take medicine"
    return {"message": "Triage suggestion retrieved successfully", "triage_id": triage_id, "suggestion": suggestion}

@app.get("/er/booking/{booking_id}")
async def get_er_booking(booking_id: int):
    # booking = eRService.get_booking(booking_id)
    return {
        "booking_id": booking_id,
        "booking_time": "2021-01-01",
        "status": "waiting",
        "last_updated": "2021-01-01",
        "estimated_time": "3 days",
        "area": "Victoria",
        "hospital_name": "Jubilee Hospital",  
        "slot_number": 23
    }

@app.get("/er/booking/status/{booking_id}")
async def get_er_booking_status(booking_id: int):
    # erService.get_booking_status(booking_id)
    return {
        "message": "Booking status retrieved successfully",
        "booking_id": booking_id,
        "status": "waiting"
        }

@app.post("/er/booking/create")
async def create_er_booking(priority: int, patient_id: int):
    # erService.create_booking(priority, patient_id)
    return {
        "message": "Booking created successfully",
        "priority": priority,
        "patient_id": patient_id,
        "booking": {
            "booking_id": 0,
            "booking_time": "2021-01-01",
            "status": "waiting",
            "last_updated": "2021-01-01",
            "estimated_time": "3 days",
            "area": "Victoria",
            "hospital_name": "Jubilee Hospital",  
            "slot_number": 23
        }
        }

@app.post("/er/booking/{booking_id}/cancel")
async def cancel_er_booking(booking_id: int):
    return {
        "message": "Booking cancelled successfully",
        "booking_id": booking_id
        }
    
@app.get("/er/load/{hospital_id}")
async def check_er_load_in_area(hospital_id: int):
    return {"message": "Current ER Queue at Jubilee Hospital is 10. The estimated wait time is 3 days."}
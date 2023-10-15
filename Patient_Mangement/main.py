import bcrypt
from fastapi import FastAPI, HTTPException, status
from pydantic import BaseModel
import random
import string
# from services import AccountInfoManagement, TriageManagement

app = FastAPI()
# manageTriage = TriageManagement()
# manageAccount = AccountInfoManagement()

class LoginData(BaseModel):
    username: str
    password: str

class UserHealthInfoCreation(BaseModel):
    height: float
    weight: float
    blood_type: str
    blood_pressure: float
    allergies: str
    complications: str

class AccountInformationCreation(BaseModel):
    username: str
    password: str
    first: str
    last: str
    phone: str
    email: str
    str_num: str
    str_name: str
    city: str
    province: str
    postal_code: str

class AccountCreationRequest(BaseModel):
    account_info: AccountInformationCreation
    health_info: UserHealthInfoCreation


def validate_user(username: str, password: str) -> dict:
    hashed_password = bcrypt.hashpw("js1544".encode('utf-8'), bcrypt.gensalt())
    if (username == "juliuscaesar") and (bcrypt.checkpw(password.encode('utf-8'), hashed_password)):
        return {"success": True, "message": "Login successful"}
    else:
        return {"success": False, "message": "Invalid username or password"}


@app.post("/login/")
async def user_validation(data: LoginData):
    #manageAccount.validate_user(username, password)
    result = validate_user(data.username, data.password)
    if result["success"]:
        return result
    else:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail=result["message"])
    

def generate_username(name: str) -> str:
    random_string = ''.join(random.choices(string.ascii_lowercase + string.digits, k=5))
    username = name.lower().replace(" ", "") + random_string
    return username

@app.post("/create-account/")
async def create_new_account(request: AccountCreationRequest):
    #manageAccount.create_account(patient_id)
    account_info = request.account_info
    
    if account_info.username == "existinguser":
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Username already exists.")
    
    if not account_info.username:
        account_info.username = generate_username(account_info.first + account_info.last)

    message = {
        "message": "Account created successfully.",
        "patient_id": f"{random.randint(10000, 99999)}",
        "user_name": f"{account_info.first} {account_info.last}",
        "username": account_info.username,
    }
    return message


@app.get("/{patient_id}/")
async def get_user_health_info(patient_id):
    #manageAccount.get_user_info(patient_id)
    return {
        "patient_id": patient_id,
        "height": 175.3,
        "weight": 68.5,
        "blood_type": "A+",
        "blood_pressure": 120.8,
        "allergies": "Peanuts, Shellfish",
        "complications": "Hypertension, Diabetes Type 2"
    }
    

@app.get("/{patient_id}/triages/")
async def get_triage_list(patient_id):
    #mangeTriage.getTriageRecordList(patient_id)
    return {"triage_history":
            [{
    "patient_id": "13479",
    "triage_id": "45382",
    "available_date": "1944-06-06",
    "summary": "44-year-old male with acute chest pain, shortness of breath, and sweating presented. Vital signs: BP 160/95 mmHg, HR 110 bpm, RR 22 breaths/min, Temp 98.6°F, O2 Sat 92%. Pain described as sharp, radiating to left arm, rated 8/10. ECG showed ST-segment elevation in leads II, III, aVF, categorized as Triage Level 2. Administered chewable aspirin, nitroglycerin, prepared for further emergency procedures. Family updated."
},
{
    "patient_id": "13479",
    "triage_id": "10439",
    "available_date": "1975-07-15",
    "summary": "75-year-old male, Triage Level 1, showed severe respiratory distress, cyanosis, altered consciousness. Immediate airway management, high-flow oxygen initiated, critical care team mobilized for advanced support."
},
{
    "patient_id": "13479",
    "triage_id": "86241",
    "available_date": "1980-03-23",
    "summary": "80-year-old male, Triage Level 2, with persistent chest pain, mild dyspnea, history of hypertension. Administered nitroglycerin, continuous ECG monitoring, cardiology alerted for comprehensive cardiac assessment."
}] }


@app.get("/{patient_id}/triages/{triage_id}")
async def get_specific_triage(patient_id, triage_id):
     #mangeTriage.getTriageRecord(patient_id, triage_id)
    return {
    "patient_id": "13479",
    "triage_id": "45382",
    "available_date": "1944-06-06",
    "summary": "44-year-old male with acute chest pain, shortness of breath, and sweating presented. Vital signs: BP 160/95 mmHg, HR 110 bpm, RR 22 breaths/min, Temp 98.6°F, O2 Sat 92%. Pain described as sharp, radiating to left arm, rated 8/10. ECG showed ST-segment elevation in leads II, III, aVF, categorized as Triage Level 2. Administered chewable aspirin, nitroglycerin, prepared for further emergency procedures. Family updated."
  }

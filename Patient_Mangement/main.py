import bcrypt
from fastapi import FastAPI, HTTPException, status
from fastapi.openapi.utils import get_openapi
from pydantic import BaseModel, Field
import random
import string
# from services import AccountInfoManagement, TriageManagement

app = FastAPI()
# manageTriage = TriageManagement()
# manageAccount = AccountInfoManagement()

class LoginResponse(BaseModel):
    success: bool = Field(example=True)
    message: str = Field(example="Login successful")

class AccountCreationResponse(BaseModel):
    message: str = Field(example="Account created successfully.")
    patient_id: str = Field(example="12345")
    user_name: str = Field(example="John Doe")
    username: str = Field(example="johndoe12345")

class UserHealthInfoResponse(BaseModel):
    patient_id: str = Field(example="12345")
    height: float = Field(example=175.3)
    weight: float = Field(example=68.5)
    blood_type: str = Field(example="A+")
    blood_pressure: float = Field(example=120.8)
    allergies: str = Field(example="Peanuts, Shellfish")
    complications: str = Field(example="Hypertension, Diabetes Type 2")

class TriageDetailResponse(BaseModel):
    patient_id: str = Field(example="12345")
    triage_id: str = Field(example="45382")
    available_date: str = Field(example="1944-06-06")
    summary: str = Field(example="44-year-old male with acute chest pain, ...")


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

class TriageHistoryItem(BaseModel):
    patient_id: str = Field(example="12345")
    triage_id: str = Field(example="45382")
    available_date: str = Field(example="1944-06-06")
    summary: str = Field(example=("44-year-old male with acute chest pain, shortness of breath, and sweating presented. Vital signs: BP 160/95 mmHg, HR 110 bpm, RR 22 breaths/min, Temp 98.6°F, O2 Sat 92%. Pain described as sharp, radiating to left arm, rated 8/10. ECG showed ST-segment elevation in leads II, III, aVF, categorized as Triage Level 2. Administered chewable aspirin, nitroglycerin, prepared for further emergency procedures. Family updated."))

class TriageListResponse(BaseModel):
    triage_history: list[TriageHistoryItem] = Field(
        example={"triage_history":[
            {
                "patient_id": "12345",
                "triage_id": "45382",
                "available_date": "1944-06-06",
                "summary": "44-year-old male with acute chest pain, shortness of breath, and sweating presented. Vital signs: BP 160/95 mmHg, HR 110 bpm, RR 22 breaths/min, Temp 98.6°F, O2 Sat 92%. Pain described as sharp, radiating to left arm, rated 8/10. ECG showed ST-segment elevation in leads II, III, aVF, categorized as Triage Level 2. Administered chewable aspirin, nitroglycerin, prepared for further emergency procedures. Family updated."
            
            },
            {
                "patient_id": "12345",
                 "triage_id": "10439",
                "available_date": "1975-07-15",
                "summary": "75-year-old male, Triage Level 1, showed severe respiratory distress, cyanosis, altered consciousness. Immediate airway management, high-flow oxygen initiated, critical care team mobilized for advanced support."
            },
            {
                "patient_id": "12345",
                "triage_id": "86241",
                "available_date": "1980-03-23",
                "summary": "80-year-old male, Triage Level 2, with persistent chest pain, mild dyspnea, history of hypertension. Administered nitroglycerin, continuous ECG monitoring, cardiology alerted for comprehensive cardiac assessment."
            }
        ]
        }
    )

class UpdateUserHealthInfoRequest(BaseModel):
    height: float = Field(None, example=175.3)
    weight: float = Field(None, example=68.5)
    blood_type: str = Field(None, example="A+")
    blood_pressure: float = Field(None, example=120.8)
    allergies: str = Field(None, example="Peanuts, Shellfish")
    complications: str = Field(None, example="Hypertension, Diabetes Type 2")

class UpdateAccountInformationRequest(BaseModel):
    # ... other fields as necessary ...
    phone: str = Field(None, example="555-1234")
    email: str = Field(None, example="johndoe@example.com")

class UpdateTriageRequest(BaseModel):
    available_date: str = Field(None, example="1944-06-06")
    summary: str = Field(None, example=(
        "44-year-old male with acute chest pain, shortness of breath, "
        "and sweating presented. Vital signs: BP 160/95 mmHg, HR 110 bpm, "
        "RR 22 breaths/min, Temp 98.6°F, O2 Sat 92%. Pain described as sharp, "
        "radiating to left arm, rated 8/10. ECG showed ST-segment elevation in "
        "leads II, III, aVF, categorized as Triage Level 2. Administered "
        "chewable aspirin, nitroglycerin, prepared for further emergency procedures. "
        "Family updated."
    ))

class ResponseMessage(BaseModel):
    message: str = Field(example="Operation successful.")



def validate_user(username: str, password: str) -> dict:
    hashed_password = bcrypt.hashpw("js1544".encode('utf-8'), bcrypt.gensalt())
    if (username == "juliuscaesar") and (bcrypt.checkpw(password.encode('utf-8'), hashed_password)):
        return {"success": True, "message": "Login successful"}
    else:
        return {"success": False, "message": "Invalid username or password"}


@app.post("/login/", response_model=LoginResponse)
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

@app.post("/create-account/", response_model=AccountCreationResponse)
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


@app.put("/{patient_id}/account-info/", response_model=ResponseMessage)
async def update_account_information(patient_id: str, request: UpdateAccountInformationRequest):
    return {"message": "Account information updated successfully."}


@app.delete("/{patient_id}/account-info/", response_model=ResponseMessage)
async def delete_account_information(patient_id: str):
    return {"message": "Account information deleted successfully."}


@app.get("/{patient_id}/", response_model=UserHealthInfoResponse)
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


@app.put("/{patient_id}/health-info/", response_model=ResponseMessage)
async def update_user_health_info(patient_id: str, request: UpdateUserHealthInfoRequest):
    return {"message": "User health information updated successfully."}


@app.delete("/{patient_id}/health-info/", response_model=ResponseMessage)
async def delete_user_health_info(patient_id: str):
    return {"message": "User health information deleted successfully."}
    

@app.get("/{patient_id}/triages/", response_model=TriageListResponse)
async def get_triage_list(patient_id):
    #mangeTriage.getTriageRecordList(patient_id)
    return {"triage_history":
            [{
    "patient_id": patient_id,
    "triage_id": "45382",
    "available_date": "1944-06-06",
    "summary": "44-year-old male with acute chest pain, shortness of breath, and sweating presented. Vital signs: BP 160/95 mmHg, HR 110 bpm, RR 22 breaths/min, Temp 98.6°F, O2 Sat 92%. Pain described as sharp, radiating to left arm, rated 8/10. ECG showed ST-segment elevation in leads II, III, aVF, categorized as Triage Level 2. Administered chewable aspirin, nitroglycerin, prepared for further emergency procedures. Family updated."
},
{
    "patient_id": patient_id,
    "triage_id": "10439",
    "available_date": "1975-07-15",
    "summary": "75-year-old male, Triage Level 1, showed severe respiratory distress, cyanosis, altered consciousness. Immediate airway management, high-flow oxygen initiated, critical care team mobilized for advanced support."
},
{
    "patient_id": patient_id,
    "triage_id": "86241",
    "available_date": "1980-03-23",
    "summary": "80-year-old male, Triage Level 2, with persistent chest pain, mild dyspnea, history of hypertension. Administered nitroglycerin, continuous ECG monitoring, cardiology alerted for comprehensive cardiac assessment."
}] }


@app.get("/{patient_id}/triages/{triage_id}", response_model=TriageDetailResponse)
async def get_specific_triage(patient_id, triage_id):
     #mangeTriage.getTriageRecord(patient_id, triage_id)
    return {
    "patient_id": patient_id,
    "triage_id": triage_id,
    "available_date": "1944-06-06",
    "summary": "44-year-old male with acute chest pain, shortness of breath, and sweating presented. Vital signs: BP 160/95 mmHg, HR 110 bpm, RR 22 breaths/min, Temp 98.6°F, O2 Sat 92%. Pain described as sharp, radiating to left arm, rated 8/10. ECG showed ST-segment elevation in leads II, III, aVF, categorized as Triage Level 2. Administered chewable aspirin, nitroglycerin, prepared for further emergency procedures. Family updated."
  }


@app.put("/{patient_id}/triages/{triage_id}", response_model=ResponseMessage)
async def update_triage(patient_id: str, triage_id: str, request: UpdateTriageRequest):
    return {"message": "Triage updated successfully."}


@app.delete("/{patient_id}/triages/{triage_id}", response_model=ResponseMessage)
async def delete_triage(patient_id: str, triage_id: str):
    return {"message": "Triage deleted successfully."}


def custom_openapi():
    if app.openapi_schema:
        return app.openapi_schema
    openapi_schema = get_openapi(
        title="Patient Management API",
        version="2.5.0",
        summary="The API for patient management for MisterEd system.",
        description="The API for patient management for MisterEd system.",
        routes=app.routes,
    )
    openapi_schema["info"]["x-logo"] = {
        "url": "https://fastapi.tiangolo.com/img/logo-margin/logo-teal.png"
    }
    app.openapi_schema = openapi_schema
    return app.openapi_schema


app.openapi = custom_openapi

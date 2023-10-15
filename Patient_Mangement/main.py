from fastapi import FastAPI
# from services import AccountInfoManagement, TriageManagement

app = FastAPI()
# manageTriage = TriageManagement()
# manageAccount = AccountInfoManagement()

        

@app.get("/{patient_id}/triages/")
async def get_triage_list(patient_id):
    #mangeTriage.getTriageRecordList(patient_id)
    return [
  {
    "patient_id": "13479",
    "triage_id": "45382",
    "available_date": "1944-06-06",
    "summary": "Upon initial assessment, the patient, a 44-year-old male, presented with acute chest pain, shortness of breath, and profuse sweating. Vital signs upon arrival: BP 160/95 mmHg, HR 110 bpm, RR 22 breaths/min, Temp 98.6°F (37°C), and O2 Sat 92%. The patient described the pain as sharp, radiating to the left arm, and rated it 8/10 on the pain scale. ECG revealed ST-segment elevation in leads II, III, and aVF. The patient was categorized as Triage Level 2 - Emergency, requiring rapid medical intervention. He was promptly administered a chewable aspirin, nitroglycerin, and was prepared for further emergency diagnostic and therapeutic procedures. The patient's family was updated regarding the situation and the next steps in medical management."
  },
  {
    "patient_id": "13479",
    "triage_id": "10439",
    "available_date": "1975-07-15",
    "summary": "The 75-year-old male patient was urgently categorized as Triage Level 1 following a rapid assessment that identified severe respiratory distress, cyanosis, and a significantly altered level of consciousness. Immediate interventions, including airway management and high-flow oxygen therapy, were initiated, and the critical care team was mobilized to ensure advanced support and ongoing management of her critical condition."
  },
  {
    "patient_id": "13479",
    "triage_id": "86241",
    "available_date": "1980-03-23",
    "summary": "The 80-year-old male patient was classified as Triage Level 2 after an evaluation revealed persistent chest pain, mild dyspnea, and a history of hypertension. Quick interventions, such as administering nitroglycerin and continuous ECG monitoring, were employed, and the cardiology department was alerted for a comprehensive cardiac assessment."
  }
]

@app.get("/{patient_id}/triages/{triage_id}")
async def get_specific_triage(patient_id, triage_id):
     #mangeTriage.getTriageRecord(patient_id, triage_id)
    return {
    "patient_id": "13479",
    "triage_id": "45382",
    "available_date": "1944-06-06",
    "summary": "Upon initial assessment, the patient, a 44-year-old male, presented with acute chest pain, shortness of breath, and profuse sweating. Vital signs upon arrival: BP 160/95 mmHg, HR 110 bpm, RR 22 breaths/min, Temp 98.6°F (37°C), and O2 Sat 92%. The patient described the pain as sharp, radiating to the left arm, and rated it 8/10 on the pain scale. ECG revealed ST-segment elevation in leads II, III, and aVF. The patient was categorized as Triage Level 2 - Emergency, requiring rapid medical intervention. He was promptly administered a chewable aspirin, nitroglycerin, and was prepared for further emergency diagnostic and therapeutic procedures. The patient's family was updated regarding the situation and the next steps in medical management."
  }

@app.get("/{patient_id}/{username}-{password}/")
async def user_validation(username, password):
    #manageAccount.validate_user(username, password)
    if (username == "juliuscaesar") and (password == "js1544"):
        return [True, "Login successful"]
    else:
        return [False, "Invalid username or password"]


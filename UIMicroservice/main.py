from fastapi import FastAPI
from Services import ERService, Authentication, NotificationService, TriageDataGetter

app = FastAPI()

#functions definition

@app.get("")

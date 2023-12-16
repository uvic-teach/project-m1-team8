# build a schema using pydantic
from pydantic import BaseModel
from typing import List, Optional
from datetime import datetime

class TriageBase(BaseModel):
    patient_id: str
    perform_date: str
    status: str
    
class TriageCreate(TriageBase):
    pass

class Triage(TriageBase):
    triage_id: int

    class Config:
        orm_mode = True
        
class TriageAnswerBase(BaseModel):
    triage_id: str
    question_id: str
    answer: str
    
class TriageAnswerCreate(TriageAnswerBase):
    pass

class TriageAnswer(TriageAnswerBase):
    triage_answer_id: int

    class Config:
        orm_mode = True
        
class TriageQuestionBase(BaseModel):
    question: str
    question_type: str
    question_category: str
    
class TriageQuestionCreate(TriageQuestionBase):
    pass

class TriageQuestion(TriageQuestionBase):
    question_id: int

    class Config:
        orm_mode = True
        
class TriageResultBase(BaseModel):
    triage_id: str
    patient_id: str

class TriageResultCreate(TriageResultBase):
    pass

class TriageResult(TriageResultBase):
    triage_result_id: int

    class Config:
        orm_mode = True
from sqlalchemy import Column, ForeignKey, Integer, String, Float, DateTime
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func

from db import Base
from enum import Enum

class TriageStatus(Enum):
    WAITING = "waiting"
    PROCESSING = "processing"
    COMPLETE = "complete"
    CANCELED = "canceled"
    ERROR = "error"

class Triage(Base):
    __tablename__ = "triages"
    triage_id = Column(Integer, primary_key=True,index=True)
    patient_id = Column(Integer, nullable=False, unique=False)
    perform_date = Column(DateTime(timezone=True), server_default=func.now())
    status = Column(String(100), nullable=False, unique=False)
    last_updated = Column(DateTime(timezone=True), server_default=func.now())
    triage_answers = relationship("triage_answers",primaryjoin="triages.triage_id == triage_answers.triage_id",cascade="all, delete-orphan")

    def __repr__(self):
        return f'Triage(triage_id={self.triage_id}, patient_id={self.patient_id}, perform_date={self.perform_date}, status={self.status}, last_updated={self.last_updated}, triage_answers={self.triage_answers})'
    
class TriageAnswer(Base):
    __tablename__ = "triage_answers"
    triage_answer_id = Column(Integer, primary_key=True,index=True)
    triage_id = Column(Integer, ForeignKey("triages.triage_id"), nullable=False, unique=False)
    question_id = Column(Integer, ForeignKey("triage_questions.question_id"), nullable=False, unique=False)
    answer = Column(String(200), nullable=False, unique=False)
    last_updated = Column(DateTime(timezone=True), server_default=func.now())
    
    def __repr__(self):
        return f'TriageAnswer(triage_answer_id={self.triage_answer_id}, triage_id={self.triage_id}, question_id={self.question_id}, answer={self.answer}, last_updated={self.last_updated})'

class TriageResult(Base):
    __tablename__ = "triage_results"
    triage_result_id = Column(Integer, primary_key=True,index=True)
    triage_id = Column(Integer, ForeignKey("triages.triage_id"), nullable=False, unique=False)
    available_date = Column(DateTime(timezone=True), server_default=func.now())
    patient_id = Column(Integer, nullable=False, unique=False)
    
    def __repr__(self):
        return f'TriageResult(triage_result_id={self.triage_result_id}, triage_id={self.triage_id}, available_date={self.available_date}, patient_id={self.patient_id})'
    
class TriageQuestion(Base):
    __tablename__ = "triage_questions"
    question_id = Column(Integer, primary_key=True,index=True)
    question = Column(String(200), nullable=False, unique=False)
    question_type = Column(String(80), nullable=False, unique=False)
    question_category = Column(String(80), nullable=True, unique=False)
    last_updated = Column(DateTime(timezone=True), server_default=func.now())
    
    def __repr__(self):
        return f'TriageQuestion(question_id={self.question_id}, question={self.question}, question_type={self.question_type}, question_category={self.question_category}, last_updated={self.last_updated})'
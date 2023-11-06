from datetime import date
from enum import Enum
from typing import Optional
from pydantic import BaseModel
from components import TriageResult


class TriageStatus(str, Enum):
    WAITING = "WAITING"
    PROCESSING = "PROCESSING"
    ERRORED = "ERRORED"
    FINISHED = "FINISHED"
    CANCELLED = "CANCELLED"
    UNKNOWN = "UNKNOWN"


class Triage(BaseModel):
    """
    Represents a triage for a patient.

    Attributes:
    patient_id (int): the ID of the patient who did the triage.
    perform_date (date): the date the patient did the triage.
    status (TriageStatus): the status of the triage.
    triage_results (Optional[TriageResult]): the results of the triage, if the status is FINISHED.
    """
    triage_id: int
    patient_id: int
    perform_date: date
    status: TriageStatus
    triage_results: Optional[TriageResult] = None

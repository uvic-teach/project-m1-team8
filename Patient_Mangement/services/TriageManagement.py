from components import TriageRecord
from typing import List

class ERService:
    def _init_(self):
        # Initialize any necessary variables or data structures
        pass

    def getTriageRecordList(self, patient_id) -> List:
        """
        Retrieve a list of triage instances from a patient's history.

        Args:
            patient_id (str): ID of patient to check
        
        Returns:
            List: A list of TriageRecord objects, each containing basic information about individual triage instances in the patient's history.
        """
        pass

    def get_triage_record(self, patient_id: str, triage_id: str) -> TriageRecord:
        """
        Retrieve a specific triage record from a patient's history.
    
        Args:
            patient_id (str): ID of the patient to check.
            triage_id (str): ID of the triage to retrieve.

        Returns:
            TriageRecord: An object containing basic information about the specified triage.
        """
        pass
       

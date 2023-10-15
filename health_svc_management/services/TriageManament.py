from typing import Dict
from components import TriageResult, TriageSuggestion, Triage

class TriageManagement:
    def __init__(self):
        self.triage_results: Dict[int, TriageResult] = {
            0: TriageResult(0, "2021-01-01", "2021-01-02", "Alice Smith", "Summary 1", "Detail 1", "Suggestion 1"),
            1: TriageResult(1, "2021-01-03", "2021-01-04", "Bob Johnson", "Summary 2", "Detail 2", "Suggestion 2"), 
            2: TriageResult(2, "2021-01-05", "2021-01-06", "Charlie Brown", "Summary 3", "Detail 3", "Suggestion 3"),
            3: TriageResult(3, "2021-01-07", "2021-01-08", "David Lee", "Summary 4", "Detail 4", "Suggestion 4"),
            4: TriageResult(4, "2021-01-09", "2021-01-10", "Emma Watson", "Summary 5", "Detail 5", "Suggestion 5"),
            5: TriageResult(5, "2021-01-11", "2021-01-12", "Frank Sinatra", "Summary 6", "Detail 6", "Suggestion 6"),
            6: TriageResult(6, "2021-01-13", "2021-01-14", "Grace Kelly", "Summary 7", "Detail 7", "Suggestion 7"),
            7: TriageResult(7, "2021-01-15", "2021-01-16", "Henry Ford", "Summary 8", "Detail 8", "Suggestion 8"),
            8: TriageResult(8, "2021-01-17", "2021-01-18", "Isaac Newton", "Summary 9", "Detail 9", "Suggestion 9"),
            9: TriageResult(9, "2021-01-19", "2021-01-20", "Jane Austen", "Summary 10", "Detail 10", "Suggestion 10")
        }

    def create_triage(self, patient_id: int, patient_name: str) -> int:
        return Triage(0, 0, "2021-01-01", "FINISHED", TriageResult(0, "2021-01-01", "2021-01-02", "Alice Smith", "Summary 1", "Detail 1", "Suggestion 1"))
    
    def get_triage(self, triage_id):
        return Triage(0, 0, "2021-01-01", "FINISHED", TriageResult(0, "2021-01-01", "2021-01-02", "Alice Smith", "Summary 1", "Detail 1", "Suggestion 1"))

    def calculate_triage_result(self, patient_id: int, patient_name: str) -> int:
        # Implementation to calculate triage result based on triage_id
        return 0 # triage_id

    def create_triage_result(self, triage_id: int, result: str) -> None:
        triage_result = TriageResult(triage_id, result)
        self.triage_results[triage_id%10] = triage_result

    def read_triage_result(self, triage_id: int) -> TriageResult:
        return self.triage_results[triage_id%10]

    def update_triage_result(self, triage_id: int, result: str) -> None:
        triage_result = TriageResult(triage_id, result)
        self.triage_results[triage_id%10] = triage_result # %10 to make sure the dummy code works

    def delete_triage_result(self, triage_id: int) -> None:
        del self.triage_results[triage_id%10]

    def get_triage_status(self, triage_id: int) -> str:
        # Implementation to get status of triage based on triage_id
        return "FINISHED"

    def get_triage_suggestion(self, triage_id: int) -> TriageSuggestion:
        # Implementation to get suggestion of a triage based on triage_id
        return TriageSuggestion(triage_id, "Take medicine")

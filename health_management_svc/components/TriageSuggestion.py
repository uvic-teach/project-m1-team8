from abc import ABC, abstractmethod

class TriageSuggestion(ABC):
    def __init__(self, triage_id, suggestion):
        self.triage_id = triage_id
        self.suggestion = suggestion

    @abstractmethod
    def suggest_action(self):
        pass

class TakeMedicineSuggestion(TriageSuggestion):
    def suggest_action(self):
        return f"Take medicine for triage {self.triage_id}: {self.suggestion}"

class NurseClinicianContactSuggestion(TriageSuggestion):
    def suggest_action(self):
        return f"Contact nurse or clinician for triage {self.triage_id}: {self.suggestion}"

class ERSuggestion(TriageSuggestion):
    def suggest_action(self):
        return f"Go to the emergency room for triage {self.triage_id}: {self.suggestion}"

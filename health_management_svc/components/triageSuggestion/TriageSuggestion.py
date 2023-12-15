class HealthSuggestion:
    self.patient_id = None
    self.suggestion_type = None
    self.suggestion_id = None
    self.additional_suggestion = None
    def display_info(self):
        pass

class Medicine(HealthSuggestion):
    def __init__ (self, patient_id, suggestion_id):
        self.patient_id = patient_id
        self.suggestion_type = "medicine"
        self.suggestion_id = suggestion_id
        self.additional_suggestion = None
        
    def display_info(self):
        print("Displaying medicine information.")

class Clinic(HealthSuggestion):
    def __init__ (self, patient_id, suggestion_id):
        self.patient_id = patient_id
        self.suggestion_type = "clinic"
        self.suggestion_id = suggestion_id
        self.additional_suggestion = None
        
    def display_info(self):
        print("Displaying clinic information.")

class ERVisit(HealthSuggestion):
    def __init__ (self, patient_id, suggestion_id):
        self.patient_id = patient_id
        self.suggestion_type = "er"
        self.suggestion_id = suggestion_id
        self.additional_suggestion = None
        
    def display_info(self):
        print("Displaying ER visit information.")
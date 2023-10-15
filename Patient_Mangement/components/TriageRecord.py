class TriageRecord():
    def _init_(self, patient_id, triage_id, available_date, summary):
        self.patient_id = patient_id
        self.triage_id = triage_id
        self.available_date = available_date
        self.summary = summary

    @property
    def triage_id(self):
        return self.triage_id
    
    def triage_id(self, value):
        self.triage_id = value



    



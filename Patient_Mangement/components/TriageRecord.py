class TriageRecord():

    def _init_(self, patient_id, triage_id, available_date, summary):
        self.patient_id = patient_id
        self.triage_id = triage_id
        self.available_date = available_date
        self.summary = summary

    @property
    def patient_id(self):
        return self.patient_id
    
    @patient_id.setter
    def patient_id(self, value):
        self.patient_id = value

    @property
    def triage_id(self):
        return self.triage_id
    
    @triage_id.setter
    def triage_id(self, value):
        self.triage_id = value

    @property
    def available_date(self):
        return self.available_date
    
    @available_date.setter
    def available_date(self, value):
        self.available_date = value

    @property
    def summary(self):
        return self.summary
    
    @summary.setter
    def summary(self, value):
        self.summary = value


    



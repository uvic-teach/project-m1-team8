class UserHealthInfo:

    def _init_(self, patient_id: str, height: float, weight: float, blood_type: str, blood_pressure: float, allergies: str, complications: str):
        self.patient_id = patient_id
        self.height = height
        self.weight = weight
        self.blood_type = blood_type
        self.blood_pressure = blood_pressure
        self.allergies = allergies
        self.complication = complications

    @property
    def patient_id(self):
        return self.patient_id

    @patient_id.setter
    def patient_id(self, value):
        self.patient_id = value

    @property
    def height(self):
        return self.height

    @height.setter
    def height(self, value):
        self.height = value

    @property
    def weight(self):
        return self.weight

    @weight.setter
    def weight(self, value):
        self.weight = value

    @property
    def blood_type(self):
        return self.blood_type

    @blood_type.setter
    def blood_type(self, value):
        self.blood_type = value

    @property
    def blood_pressure(self):
        return self.blood_pressure

    @blood_pressure.setter
    def blood_pressure(self, value):
        self.blood_pressure = value

    @property
    def allergies(self):
        return self.allergies

    @allergies.setter
    def allergies(self, value):
        self.allergies = value

    @property
    def complication(self):
        return self.complication

    @complication.setter
    def complication(self, value):
        self.complication = value


    

    

    



    
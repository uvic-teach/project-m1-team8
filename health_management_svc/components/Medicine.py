class Medicine:
    def __init__(self, med_id: int, main_purpose: str, side_effect: str, usage: str, is_required_prescription: bool, company: str, ingredients: str):
        self.med_id = med_id
        self.main_purpose = main_purpose
        self.side_effect = side_effect
        self.usage = usage
        self.is_required_prescription = is_required_prescription
        self.company = company
        self.ingredients = ingredients
    
    def get_med_id(self):
        return self.med_id
    
    def get_main_purpose(self):
        return self.main_purpose
    
    def get_side_effect(self):
        return self.side_effect
    
    def get_usage(self):
        return self.usage
    
    def get_is_required_prescription(self):
        return self.is_required_prescription
    
    def get_company(self):
        return self.company
    
    def get_ingredients(self):
        return self.ingredients

from TriageSuggestion import Medicine, Clinic, ERVisit

class HealthSuggestionFactory():
    @abstractmethod
    def create_suggestion(self, content: str) -> HealthSuggestion:
        pass
    
class MedicineFactory(HealthSuggestionFactory):
    def create_suggestion(self):
        return Medicine()

class ClinicFactory(HealthSuggestionFactory):
    def create_suggestion(self):
        return Clinic()

class ERVisitFactory(HealthSuggestionFactory):
    def create_suggestion(self):
        return ERVisit()
    
class HealthRecommendationSystem:
    def suggest_health_option(self, suggestion_type):
        factory = None

        if suggestion_type == 'medicine':
            factory = MedicineFactory()
        elif suggestion_type == 'clinic':
            factory = ClinicFactory()
        elif suggestion_type == 'er':
            factory = ERVisitFactory()

        if factory:
            suggestion = factory.create_suggestion()
            suggestion.display_info()
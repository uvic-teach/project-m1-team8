class TriageSuggestionBase(BaseModel):
    """Interface for Triage Suggestion."""
    @abstractmethod
    def createSuggestion(self, triage_id, suggestion):
        """Create Triage Suggestion"""

    @abstractmethod
    def getSuggestion(self, triage_id):
        """Get Suggestion for a triage"""
        
    
        

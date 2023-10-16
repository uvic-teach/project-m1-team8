class TriageDataHandler():
  def _init_(self):
    #initialize anything necessary
    pass
  def GrabnDisplayList(self, patient_id:str)-> None:
    """
    request the patients triage instances list from TriageManagement and 
    display it on the webpage
    Args:
      patient_id(str): ID of patient to check
    Changes to page:
      load triage history page a table containing the full 
      list of triage instances
    Returns:
      none
    """
    pass
   def GrabnDisplayElement(self, patient_id:str, triage_id:str )-> None:
    """
    request the patients triage instances list from TriageManagement and 
    display it on the webpage
    Args:
      patient_id(str): ID of patient to check
    Changes to page:
      load triage history page with a table containing the one selected
      element from the list of triage instances
    Returns:
      none
    """
    pass
  def performTriage(self, patient_id:str)->None:
    """
    request for a triage to occur using TriageManagement
    args:
    patient_id(str): the id of the patient
    Returns:
    none
    """
    pass
    


    


  





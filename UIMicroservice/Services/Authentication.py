class Authentication():
  def _init_(self):
    pass
    
  def request_validation(self,username:str,password: str)-> void:
    """
    Request a user validation from AccountInfoManagement then updates the page based on validity
    Args:
    username(str): Username of the user
    password(str): Password of the user
    changes to page:
    On Valid: enter user dashboard page
    On Invalid: reload login page with error notification
    Returns:
    none
    """
    pass
  def request_account_creation(self, account_info: AccountInformation, health_info: UserHealthInfo) -> void:
     """
    Request account creation from AccountInfoManagement, then load the login page 
    and send notification of account creation success failure
    Args:
    username(str): Username of the user
    password(str): Password of the user

    Changes to page:
    On success:
    load login page and display success notification
    On failure:
    load register page and display error notification
    Returns:
    none
    """
    
    
    pass


class AccountPersonalInfo():
  def _init_(self):
    pass
    
  def get_credentials_info(self)-> None:
    """
    Request user credentials and then loads page displaying user credentials and account information.
    changes to page:
    On success: enter account information page
    On failure: reload Account/Personal Info page with error notification
    Returns: none
    """
    pass
  def get_health_info(self) -> None:
    """

    Request user health info and then loads page displaying user credentials and account information.
    changes to page:
    
    Changes to page:
    On success: enter health information page
    On failure: load reload Account/Personal Info page and display error notification
    Returns: none
    """
    pass

    def requestion_account_information_update(self, account_info: AccountInformation, newAccountInformation) -> None:
      """
      Request account info update from AccountInfoManagement, then load the login page and send
      notification of account info update success failure
      Args:
      username(str): Username of the user
      password(str): Password of the user
      newPassword(str): new Password of the user || newUsername(str) new Username of user

      Changes to page:
      On success:
      load Account/Personal Info page and display success notification
      On failure:
      load Account/Personal Info page and display error notification
      Returns:
      none
      """
      pass

    def requestion_health_information_update(self, account_info: AccountInformation, health_info: newHealthInformation) -> None:
      """
      Request account info update from AccountInfoManagement, then load the login page and send
      notification of account info update success failure
      Args:
      username(str): Username of the user
      password(str): Password of the user
      HealthInformation()

      Changes to page:
      On success:
      load Account/Personal Info page and display success notification
      On failure:
      load Account/Personal Info page and display error notification
      Returns:
      none
      """
      pass
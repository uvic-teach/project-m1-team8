class Notification():
  
  def __init__(self, user_id: int, message: string):
    self.user_id = user_id
    self.message = message

  def get_message(self):
      return self.message

  def get_user_id(self):
    return self.user_id

    
    

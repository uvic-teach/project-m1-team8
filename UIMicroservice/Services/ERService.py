from components import booking

class ERService:
  def __init__(self):
    self.notification_list = []
    
  def create_booking(self, user_id: int) -> Booking
    #creates new Booking with unique booking id
    pass
    
  def get_booking(self, booking_id: int) -> Booking
      #returns corresponding Booking for booking_id
      pass

  def check_load(self, hospital_id) -> timedelta
      #looks up current load at hospital corresponding to hospital_id 
      #returns timedelta of expected wait time at hospital
      pass

  def cancel_booking(self, booking_id) -> void
      #deletes Booking from ERQueue and notifies user of successfull cancellation
      pass

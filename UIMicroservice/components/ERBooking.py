import datetime

class ERBooking:
    def __init__(self, user_id: int, medical_id: int, booking_time: string, booking_location: Hospital):
      self.user_id = user_id
      self.medical_id = medical_id   
      self.booking_time = booking_time
      self.booking_location = booking_location
      booking_info = str(booking_time) + "at" + str(booking_location)
      NotificationService.create_notification(user_id, "Your ER Booking time is" + booking_info)

    
      

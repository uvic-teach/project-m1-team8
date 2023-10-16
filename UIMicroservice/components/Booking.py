class Booking:
    def __init__(self, user_id: int, medical_id: int, booking_id: int, booking_time: timedelta, booking_location: string):
      self.user_id = user_id
      self.medical_id = medical_id   
      self.booking_id = booking_id
      self.booking_time = booking_time
      self.hospital_id = hospital_id
      self.hospital_location = booking_location #String of Hospital name/address
      booking_info = str(booking_time) + "at" + booking_location
      NotificationService.create_notification(user_id, "Your ER Booking time is" + booking_info)

    def get_user_id(self):
        return self.user_id

    def get_medical_id(self):
        return self.medical_id

    def get_booking_id(self):
        return self.booking_id

    def get_booking_location(self):
        return self.booking_location

    
    
      

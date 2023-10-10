from components import ERBooking, ERQueue, ERBookingStatus
class ERService:
    def __init__(self):
        # Initialize any necessary variables or data structures
        pass
    
    def check_load(self, hospital_id: int) -> int:
        """
        Check the load of the ER queue based on the hospital's ER availability in the neighborhood.
        
        Args:
            hospital_id (int): The ID of the hospital to check.
        
        Returns:
            int: The number of patients currently in the ER queue.
        """
        pass
    
    def create_booking(self, priority: int, patient_id: int) -> int:
        """
        Create a new ER booking with the given priority and patient ID.
        
        Args:
            priority (int): The priority level of the booking (1-5, with 1 being the highest priority).
            patient_id (int): The ID of the patient making the booking.
        
        Returns:
            int: The ID of the newly created booking.
        """
        pass
    
    def get_booking(self, booking_id: int) -> ERBooking:
            """Gets the details of an existing ER booking.

            Args:
                booking_id (int): The ID of the booking to read.

            Returns:
                ERBooking: An object containing the details of the booking, including priority, patient ID, and status.
            """
            pass
    
    def update_booking(self, booking_id: int, priority: int, patient_id: int, status: str) -> bool:
        """
        Update the details of an existing ER booking.
        
        Args:
            booking_id (int): The ID of the booking to update.
            priority (int): The new priority level of the booking (1-5, with 1 being the highest priority).
            patient_id (int): The new ID of the patient making the booking.
            status (str): The new status of the booking (e.g. "waiting", "in progress", "completed").
        
        Returns:
            bool: True if the booking was successfully updated, False otherwise.
        """
        pass
    
    def delete_booking(self, booking_id: int) -> bool:
        """
        Delete (cancel) an existing ER booking.
        
        Args:
            booking_id (int): The ID of the booking to delete.
        
        Returns:
            bool: True if the booking was successfully deleted, False otherwise.
        """
        pass
    
    def get_booking_status(self, booking_id: int) -> ERBookingStatus:
        """
        Get the status of an existing ER booking.
        
        Args:
            booking_id (int): The ID of the booking to check.
        
        Returns:
            str: The status of the booking (e.g. "waiting", "in progress", "completed").
        """
        return get_booking(booking_id).status

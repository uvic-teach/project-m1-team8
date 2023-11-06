from enum import Enum
from datetime import datetime, timedelta

class ERBookingStatus(Enum):
    WAITING = "waiting"
    PROCESSING = "processing"
    CONFIRMED = "confirmed"
    CANCELED = "canceled"
    OVERDUE = "overdue"

class ERBooking:
    def __init__(self, patient_id: int, booking_time: datetime, status: ERBookingStatus, last_updated: datetime, estimated_time: timedelta, area: str, hospital_name: str, slot_number: int = None):
        self._patient_id = patient_id
        self.booking_time = booking_time
        self.status = status
        self.last_updated = last_updated
        self.estimated_time = estimated_time
        self._area = area
        self.hospital_name = hospital_name
        self.slot_number = slot_number

    @property
    def booking_time(self):
        return self._booking_time

    @booking_time.setter
    def booking_time(self, value):
        self._booking_time = value

    @property
    def status(self):
        return self._status

    @status.setter
    def status(self, value):
        if not isinstance(value, ERBookingStatus):
            raise ValueError("Invalid status value")
        self._status = value

    @property
    def last_updated(self):
        return self._last_updated

    @last_updated.setter
    def last_updated(self, value):
        self._last_updated = value

    @property
    def estimated_time(self):
        return self._estimated_time

    @estimated_time.setter
    def estimated_time(self, value):
        self._estimated_time = value

    @property
    def hospital_name(self):
        return self._hospital_name

    @hospital_name.setter
    def hospital_name(self, value):
        self._hospital_name = value

    @property
    def slot_number(self):
        return self._slot_number

    @slot_number.setter
    def slot_number(self, value):
        self._slot_number = value

    @property
    def patient_id(self):
        return self._patient_id

    @property
    def area(self):
        return self._area


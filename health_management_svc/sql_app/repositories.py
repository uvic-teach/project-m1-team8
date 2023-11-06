from sqlalchemy.orm import Session

from . import models, schemas


class ERBookingRepo:
    
    async def create(db: Session, booking: schemas.ERBookingCreate):
        db_booking = models.ERBooking(
            patient_id=booking.patient_id,
            status=booking.status,
            estimated_time=booking.estimated_time,
            area=booking.area,
            hospital_name=booking.hospital_name,
            slot_number=booking.slot_number
        )
        db.add(db_booking)
        db.commit()
        db.refresh(db_booking)
        return db_booking
    
    def fetch_by_booking_id(db: Session,booking_id):
        return db.query(models.ERBooking).filter(models.ERBooking.booking_id == booking_id).first()
 
    def fetch_by_patient_id(db: Session,patient_id):
        return db.query(models.ERBooking).filter(models.ERBooking.patient_id == patient_id).all()
 
    def fetch_by_hospital_name(db: Session,hospital_name):
        return db.query(models.ERBooking).filter(models.ERBooking.hospital_name == hospital_name).all()
 
    def fetch_all(db: Session, skip: int = 0, limit: int = 100):
        return db.query(models.ERBooking).offset(skip).limit(limit).all()
 
    async def delete(db: Session,booking_id):
        db_item= db.query(models.ERBooking).filter_by(booking_id=booking_id).first()
        db.delete(db_item)
        db.commit()
        
    async def update(db: Session,booking_data):
        updated_item = db.merge(booking_data)
        db.commit()
        return updated_item
        
class ERQueueRepo:
    async def create(db: Session, queue: schemas.ERQueueCreate):
        db_er_queue = models.ERQueue(
            estimated_waiting_time=queue.estimated_waiting_time,
            area=queue.area,
            hospital_name=queue.hospital_name,
            current_capacity=queue.current_capacity,
            max_capacity=queue.max_capacity
        )
        db.add(db_er_queue)
        db.commit()
        db.refresh(db_er_queue)
        return db_er_queue
        
    def fetch_by_id(db: Session,queue_id:int):
        return db.query(models.ERQueue).filter(models.ERQueue.queue_id == queue_id).first()
    
    def fetch_by_hospital_name(db: Session,hospital_name:str):
        return db.query(models.ERQueue).filter(models.ERQueue.hospital_name == hospital_name).first()
    
    def fetch_all(db: Session, skip: int = 0, limit: int = 100):
        return db.query(models.ERQueue).offset(skip).limit(limit).all()
    
    async def delete(db: Session,queue_id:int):
        db_er_queue= db.query(models.ERQueue).filter_by(queue_id=queue_id).first()
        db.delete(db_er_queue)
        db.commit()
        
    async def update(db: Session,er_queue_data):
        updated_queue = db.merge(er_queue_data)
        db.commit()
        return updated_queue
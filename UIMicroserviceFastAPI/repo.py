from sqlalchemy.orm import Session
import models, schemas
import sqlalchemy


class NotificationRepo:
    
    async def create(db: Session, notification: schemas.NotificationCreate):
        db_booking = models.Notification(
            user_id=notification.user_id,
            message=notification.message,
            time_sent=notification.time_sent
        )
        try:
            db.add(db_booking)
            db.commit()
            db.refresh(db_booking)
        except sqlalchemy.exc.IntegrityError as e:
            print(f"IntegrityError: {e}")
            db.rollback()
        return db_booking
    
    def fetch_by_user_id(db: Session,user_id):
        return db.query(models.Notification).filter(models.Notification.user_id == user_id).all()
 
    def fetch_by_notification_id(db: Session,notification_id):
        return db.query(models.Notification).filter(models.Notification.notification_id == notification_id).all()
 
    def fetch_all(db: Session, skip: int = 0, limit: int = 100):
        return db.query(models.Notification).offset(skip).limit(limit).all()
 
    async def delete(db: Session,booking_id):
        db_item= db.query(models.Notification).filter_by(booking_id=booking_id).first()
        db.delete(db_item)
        db.commit()
        
    async def update(db: Session,booking_data):
        updated_item = db.merge(booking_data)
        db.commit()
        return updated_item
        

from sqlalchemy.orm import Session

from. import models, schemas

class UserHealthInfoRepo:

    async def create(db: Session, user: schemas.UserHealthInfoCreate):
        db_patient = models.UserHealthInfo(
            patient_name = user.patient_name,
            patient_id = user.patient_id,
            height = user.height, 
            weight = user.weight,
            blood_type = user.blood_type,
            blood_pressure = user.blood_pressure,
            allergies = user.allergies,
            complication = user.allergies )


        db.add(db_patient)
        db.commit()
        db.refresh(db_patient)
        return db_patient

    def fetch_patient_id(db: Session, _patient_id):
        return db.query(models.UserHealthInfo).filter(models.UserHealthInfo.patient_id == _patient_id).first()

    
    def fetch_patient_name(db: Session, _patient_name):
        return db.query(models.UserHealthInfo).filter(models.UserHealthInfo.patient_name == _patient_name).first()


    def fetch_all_patient_info(db: Session, skip: int = 0, limit: int = 100):
        return db.query(models.UserHealthInfo).offset(skip).limit(limit).all()

    async def delete(db: Session, patient_id):
        db_patient= db.query(models.UserHealthInfo).filter_by(patient_id=patient_id_id).first()
        db.delete(db_patient)
        db.commit()

    async def update(db: Session, patient_data):
        updated_patient = db.merge(patient_data)
        db.commit()
        return updated_patient


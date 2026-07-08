from sqlalchemy.orm import Session
from . import models, schemas


def get_user_by_email(db: Session, email: str):
    return db.query(models.User).filter(
        models.User.email == email
    ).first()


def create_user(db: Session, user: schemas.UserCreate):
    new_user = models.User(
        name=user.name,
        email=user.email,
        password=user.password
    )

    db.add(new_user)
    db.commit()
    db.refresh(new_user)

    return new_user
def create_medicine(db: Session, medicine: schemas.MedicineCreate):
    new_medicine = models.Medicine(
        name=medicine.name,
        dosage=medicine.dosage,
        time=medicine.time,
        user_id=medicine.user_id
    )

    db.add(new_medicine)
    db.commit()
    db.refresh(new_medicine)

    return new_medicine


def get_medicines(db: Session):
    return db.query(models.Medicine).all()
def delete_medicine(db: Session, medicine_id: int):
    medicine = db.query(models.Medicine).filter(
        models.Medicine.id == medicine_id
    ).first()

    if not medicine:
        return None

    db.delete(medicine)
    db.commit()

    return medicine
def mark_medicine_taken(
    db: Session,
    medicine_id: int
):
    medicine = db.query(models.Medicine).filter(
        models.Medicine.id == medicine_id
    ).first()

    if not medicine:
        return None

    medicine.taken = True
    db.commit()
    db.refresh(medicine)

    return medicine
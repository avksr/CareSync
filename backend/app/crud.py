from sqlalchemy.orm import Session
from . import models, schemas


# Create a new user
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
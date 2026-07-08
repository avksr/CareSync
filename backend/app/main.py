from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from .database import engine, Base, SessionLocal
from . import models, schemas, crud
from fastapi.middleware.cors import CORSMiddleware


# Create database tables
Base.metadata.create_all(bind=engine)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
def home():
    return {
        "message": "Welcome to CareSync!"
    }
@app.post(
    "/signup",
    response_model=schemas.UserResponse
)
def signup(
    user: schemas.UserCreate,
    db: Session = Depends(get_db)
):
    existing_user = crud.get_user_by_email(
        db,
        user.email
    )

    if existing_user:
        raise HTTPException(
            status_code=400,
            detail="Email already registered"
        )

    return crud.create_user(db, user)
@app.post("/login")
def login(
    user: schemas.UserLogin,
    db: Session = Depends(get_db)
):
    existing_user = crud.get_user_by_email(
        db,
        user.email
    )

    if not existing_user:
        raise HTTPException(
            status_code=400,
            detail="Invalid email or password"
        )

    if existing_user.password != user.password:
        raise HTTPException(
            status_code=400,
            detail="Invalid email or password"
        )

    return {
        "message": "Login successful"
    }
@app.post(
    "/medicines",
    response_model=schemas.MedicineResponse
)
def add_medicine(
    medicine: schemas.MedicineCreate,
    db: Session = Depends(get_db)
):
    return crud.create_medicine(db, medicine)


@app.get(
    "/medicines",
    response_model=list[schemas.MedicineResponse]
)
def get_all_medicines(
    db: Session = Depends(get_db)
):
    return crud.get_medicines(db)
@app.delete("/medicines/{medicine_id}")
def delete_medicine(
    medicine_id: int,
    db: Session = Depends(get_db)
):
    medicine = crud.delete_medicine(
        db,
        medicine_id
    )

    if not medicine:
        return {
            "message": "Medicine not found"
        }

    return {
        "message": "Medicine deleted successfully"
    }
@app.patch(
    "/medicines/{medicine_id}/taken",
    response_model=schemas.MedicineResponse
)
def mark_taken(
    medicine_id: int,
    db: Session = Depends(get_db)
):
    medicine = crud.mark_medicine_taken(
        db,
        medicine_id
    )

    if not medicine:
        return {
            "message": "Medicine not found"
        }

    return medicine

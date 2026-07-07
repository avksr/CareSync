from fastapi import FastAPI
from .database import engine, Base
from . import models


# Create database tables
Base.metadata.create_all(bind=engine)


app = FastAPI()


@app.get("/")
def home():
    return {
        "message": "Welcome to CareSync!"
    }
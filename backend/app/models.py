from sqlalchemy import Column, Integer, String, Boolean, ForeignKey
from .database import Base


# User table
class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    email = Column(String, unique=True, index=True)
    password = Column(String)


# Medicine table
class Medicine(Base):
    __tablename__ = "medicines"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    dosage = Column(String)
    time = Column(String)
    taken = Column(Boolean, default=False)
    user_id = Column(Integer, ForeignKey("users.id"))
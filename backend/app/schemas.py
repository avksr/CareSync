from pydantic import BaseModel


# Data coming from user during signup
class UserCreate(BaseModel):
    name: str
    email: str
    password: str


# Data returned by API
class UserResponse(BaseModel):
    id: int
    name: str
    email: str

    class Config:
        from_attributes = True


# Data coming from user during login
class UserLogin(BaseModel):
    email: str
    password: str

class MedicineCreate(BaseModel):
    name: str
    dosage: str
    time: str
    user_id: int


class MedicineResponse(BaseModel):
    id: int
    name: str
    dosage: str
    time: str
    taken: bool
    user_id: int

    class Config:
        from_attributes = True
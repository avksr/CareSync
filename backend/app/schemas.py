from pydantic import BaseModel


# Data coming from user
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
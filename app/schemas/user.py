from pydantic import BaseModel, EmailStr

class UserCreate(BaseModel):
    """Shape of the data we expect when someone registers."""
    household_id: int
    name: str
    email: EmailStr
    password: str
    role: str
    
class UserResponse(BaseModel):
    """Shape of the data we send back - notice: no password_hash!"""
    id: int
    household_id: int
    name: str
    email: EmailStr
    role: str
    
    class Config:
        from_attributes = True
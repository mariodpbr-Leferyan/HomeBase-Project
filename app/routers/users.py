from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.database import get_db
from app.models.user import User
from app.schemas.user import UserCreate, UserResponse
from app.security import hash_password

router = APIRouter(prefix="/users", tags=["users"])

@router.post("/register", response_model=UserResponse)
def register_user(user_data: UserCreate, db: Session = Depends(get_db)):
    
    hashed_password = hash_password(user_data.password)

    new_user = User(
        household_id=user_data.household_id,
        name=user_data.name,
        email=user_data.email,
        password_hash=hashed_password,
        role=user_data.role,
    )
    
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user


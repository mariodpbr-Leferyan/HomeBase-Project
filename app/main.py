from fastapi import FastAPI

from app.database import Base, engine
from app.models.household import Household
from app.models.user import User
from app.routers import auth, users 

# This line reads every model that inherits from Base (Household, User, ...)
# and creates the corresponding tables in the database, if they don't exist yet.
Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(users.router)
app.include_router(auth.router)

@app.get("/health")
def health_check():
    return {"status": "ok"}

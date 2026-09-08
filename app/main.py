from fastapi import FastAPI

from app.database import Base, engine
from app.models.household import Household

# This line reads every model that inherits from Base (so far, just Household)
# and creates the corresponding tables in the database, if they don't exist yet.
Base.metadata.create_all(bind=engine)

app = FastAPI()

@app.get("/health")
def health_check():
    return {"status": "ok"}
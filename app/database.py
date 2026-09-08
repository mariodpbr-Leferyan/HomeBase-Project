# app/database.py

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

# This is the connection string. "sqlite:///./homebase.db" means:
# use SQLite, and store the data in a file called homebase.db,
# in the same folder where the app runs.
SQLALCHEMY_DATABASE_URL = "sqlite:///./homebase.db"

# The engine is the actual connection to that database file.
# connect_args is a SQLite-specific quirk: it allows the connection
# to be used across different threads, which FastAPI needs.
engine = create_engine(
    SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}
)

# SessionLocal is a "factory" that creates new database sessions
# whenever a route needs to read or write data.
SessionLocal = sessionmaker (autocommit=False, autoflush=False, bind=engine)

# Base is what every model class will inherit from.
Base = declarative_base()

# This function creates a new session, hands it to whoever needs it,
# and makes sure it's properly closed afterward — even if an error happens.
# We'll use this in our routes later via FastAPI's "Depends" system.
def get_db():
    db = SessionLocal()
    try:
        yield db # create the dadabase session for one request
    finally:
        db.close()
        

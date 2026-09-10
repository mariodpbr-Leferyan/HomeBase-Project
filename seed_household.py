# seed_household.py
# Temporary script to insert one test household, so we can test
# user registration before the real POST /households route exists.
# Safe to delete once that route is built.

from app.database import SessionLocal
from app.models.household import Household

db = SessionLocal()

test_household = Household(name="Test Household")
db.add(test_household)
db.commit()
db.refresh(test_household)

print(f"Created houseld with id={test_household.id}, name='{test_household.name}'")
db.close()

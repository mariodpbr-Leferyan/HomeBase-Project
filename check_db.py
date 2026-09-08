# check_db.py
# Temporary script to verify tables exist in the database.
# Not part of the app itself — safe to delete after use.

import sqlite3

conn= sqlite3.connect("homebase.db")
tables = conn.execute("SELECT name FROM sqlite_master WHERE type='table';").fetchall()
print(tables)
conn.close()
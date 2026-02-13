import os
import sqlite3

def get_connection():
    """
    Returns a consistent SQLite connection for the FGG project.
    Ensures all scripts point to the same database location.
    """
    db_path = os.path.join(os.path.dirname(__file__), "..", "bayou_doe.db")
    print(f"Connecting to DB: {os.path.abspath(db_path)}")
    return sqlite3.connect(db_path)

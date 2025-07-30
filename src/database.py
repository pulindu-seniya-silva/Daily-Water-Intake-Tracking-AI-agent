import sqlite3
from datetime import datetime

DB_NAME = "water_tracker.db"

def create_tables():
    conn = sqlite3.connect(DB_NAME)
    
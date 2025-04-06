import sqlite3
from pathlib import Path

DB_PATH = Path(__file__).parent / "recipe_stats.db"

def init_db():
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS calculations (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            recipe_name TEXT NOT NULL,
            calories REAL NOT NULL,
            cost REAL NOT NULL,
            timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
        )
    """)
    conn.commit()
    conn.close()

def save_calculation(recipe_name, calories, cost):
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO calculations (recipe_name, calories, cost) VALUES (?, ?, ?)",
        (recipe_name, calories, cost)
    )
    conn.commit()
    conn.close()

def get_stats():
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute("""
        SELECT 
            recipe_name, 
            COUNT(*) as count, 
            AVG(calories) as avg_calories, 
            AVG(cost) as avg_cost
        FROM calculations
        GROUP BY recipe_name
    """)
    stats = cursor.fetchall()
    conn.close()
    return stats